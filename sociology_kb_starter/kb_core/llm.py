from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from typing import Optional

from kb_core.config import SETTINGS

logger = logging.getLogger(__name__)

_MAX_RETRIES = 3
_INITIAL_BACKOFF = 2.0  # seconds


@dataclass(slots=True)
class LLMResult:
    content: str
    provider: str
    model: str


def _is_retryable(exc: Exception) -> bool:
    """Return True for transient errors worth retrying (rate-limit, network, timeout)."""
    exc_type = type(exc).__name__
    if exc_type in ("RateLimitError", "APIConnectionError", "APITimeoutError"):
        return True
    status = getattr(exc, "status_code", None) or getattr(exc, "status", None)
    if status in (429, 502, 503, 504):
        return True
    return False


class LLMClient:
    def __init__(self) -> None:
        self.provider = SETTINGS.llm_provider

    def available(self) -> bool:
        if self.provider == "groq":
            return bool(SETTINGS.groq_api_key)
        if self.provider == "openai":
            return bool(SETTINGS.openai_api_key)
        if self.provider == "anthropic":
            return bool(SETTINGS.anthropic_api_key)
        return False

    def complete(self, system_prompt: str, user_prompt: str, max_tokens: int = 1800) -> Optional[LLMResult]:
        if self.provider == "groq" and SETTINGS.groq_api_key:
            return self._call_with_retry(self._groq, system_prompt, user_prompt, max_tokens)
        if self.provider == "openai" and SETTINGS.openai_api_key:
            return self._call_with_retry(self._openai, system_prompt, user_prompt, max_tokens)
        if self.provider == "anthropic" and SETTINGS.anthropic_api_key:
            return self._call_with_retry(self._anthropic, system_prompt, user_prompt, max_tokens)
        return None

    # -- provider implementations --

    @staticmethod
    def _groq(system_prompt: str, user_prompt: str, max_tokens: int) -> LLMResult:
        from openai import OpenAI as _OpenAI

        client = _OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=SETTINGS.groq_api_key,
        )
        response = client.chat.completions.create(
            model=SETTINGS.groq_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=max_tokens,
            response_format={"type": "json_object"},
        )
        return LLMResult(
            content=(response.choices[0].message.content or "").strip(),
            provider="groq",
            model=SETTINGS.groq_model,
        )

    @staticmethod
    def _openai(system_prompt: str, user_prompt: str, max_tokens: int) -> LLMResult:
        from openai import OpenAI

        client = OpenAI(api_key=SETTINGS.openai_api_key)
        response = client.responses.create(
            model=SETTINGS.openai_model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_output_tokens=max_tokens,
            text={"format": {"type": "json_object"}},
        )
        return LLMResult(content=response.output_text.strip(), provider="openai", model=SETTINGS.openai_model)

    @staticmethod
    def _anthropic(system_prompt: str, user_prompt: str, max_tokens: int) -> LLMResult:
        from anthropic import Anthropic

        client = Anthropic(api_key=SETTINGS.anthropic_api_key)
        response = client.messages.create(
            model=SETTINGS.anthropic_model,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        text = "".join(block.text for block in response.content if getattr(block, "type", "") == "text")
        return LLMResult(content=text.strip(), provider="anthropic", model=SETTINGS.anthropic_model)

    # -- retry wrapper --

    @staticmethod
    def _call_with_retry(fn, system_prompt: str, user_prompt: str, max_tokens: int) -> Optional[LLMResult]:
        last_exc: Exception | None = None
        for attempt in range(_MAX_RETRIES):
            try:
                return fn(system_prompt, user_prompt, max_tokens)
            except Exception as exc:
                last_exc = exc
                if not _is_retryable(exc) or attempt == _MAX_RETRIES - 1:
                    logger.warning("LLM call failed (attempt %d/%d): %s", attempt + 1, _MAX_RETRIES, exc)
                    break
                wait = _INITIAL_BACKOFF * (2 ** attempt)
                logger.info("LLM call retryable error (attempt %d/%d), retrying in %.1fs: %s", attempt + 1, _MAX_RETRIES, wait, exc)
                time.sleep(wait)
        return None
