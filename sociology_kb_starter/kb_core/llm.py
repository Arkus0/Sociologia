from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from kb_core.config import SETTINGS


@dataclass(slots=True)
class LLMResult:
    content: str
    provider: str
    model: str


class LLMClient:
    def __init__(self) -> None:
        self.provider = SETTINGS.llm_provider

    def available(self) -> bool:
        if self.provider == "openai":
            return bool(SETTINGS.openai_api_key)
        if self.provider == "anthropic":
            return bool(SETTINGS.anthropic_api_key)
        return False

    def complete(self, system_prompt: str, user_prompt: str, max_tokens: int = 1800) -> Optional[LLMResult]:
        if self.provider == "openai" and SETTINGS.openai_api_key:
            from openai import OpenAI

            client = OpenAI(api_key=SETTINGS.openai_api_key)
            response = client.responses.create(
                model=SETTINGS.openai_model,
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_output_tokens=max_tokens,
            )
            return LLMResult(content=response.output_text.strip(), provider="openai", model=SETTINGS.openai_model)

        if self.provider == "anthropic" and SETTINGS.anthropic_api_key:
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

        return None
