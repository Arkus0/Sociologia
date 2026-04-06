"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";

interface GraphNode {
  id: string;
  title: string;
  type: string;
  path: string | null;
  x?: number;
  y?: number;
  vx?: number;
  vy?: number;
}

interface GraphEdge {
  source: string | GraphNode;
  target: string | GraphNode;
  type: string;
}

interface GraphData {
  nodes: GraphNode[];
  edges: GraphEdge[];
}

const NODE_COLORS: Record<string, string> = {
  concept: "#3b82f6",
  author: "#22c55e",
  course: "#f59e0b",
  source: "#8b5cf6",
  semester: "#ef4444",
};

const NODE_LABELS: Record<string, string> = {
  concept: "Concepto",
  author: "Autor",
  course: "Curso",
  source: "Fuente",
  semester: "Semestre",
};

const NODE_RADIUS: Record<string, number> = {
  concept: 5,
  author: 6,
  course: 10,
  source: 4,
  semester: 12,
};

const ROUTE_PREFIX: Record<string, string> = {
  concept: "/conceptos/",
  author: "/autores/",
  course: "/cursos/",
  source: "/fuentes/",
};

function nodeRoute(node: GraphNode): string | null {
  const prefix = ROUTE_PREFIX[node.type];
  if (!prefix) return null;
  const slug = node.id.split("::")[1];
  if (!slug) return null;
  return `${prefix}${slug}`;
}

export function KnowledgeGraph() {
  const router = useRouter();
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [data, setData] = useState<GraphData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [activeTypes, setActiveTypes] = useState<Set<string>>(
    new Set(["concept", "author", "course", "source", "semester"]),
  );
  const [hoveredNode, setHoveredNode] = useState<GraphNode | null>(null);
  const [settled, setSettled] = useState(false);

  // Refs for the render loop (avoid re-creating simulation on hover)
  const hoveredRef = useRef<GraphNode | null>(null);
  const needsRedrawRef = useRef(false);
  const settledRef = useRef(false);

  const simulationRef = useRef<{
    nodes: GraphNode[];
    edges: GraphEdge[];
    alpha: number;
  } | null>(null);
  const transformRef = useRef({ x: 0, y: 0, scale: 1 });
  const dragRef = useRef<{
    node: GraphNode | null;
    startX: number;
    startY: number;
    panning: boolean;
  }>({ node: null, startX: 0, startY: 0, panning: false });
  const animRef = useRef<number>(0);
  const canvasSizeRef = useRef({ w: 0, h: 0 });

  useEffect(() => {
    let cancelled = false;
    fetch("/generated/atlas_graph.json")
      .then((res) => {
        if (!res.ok) throw new Error("No se pudo cargar el grafo");
        return res.json();
      })
      .then((raw: GraphData) => {
        if (!cancelled) setData(raw);
      })
      .catch((err) => {
        if (!cancelled) setError(err instanceof Error ? err.message : "Error");
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const toggleType = useCallback((type: string) => {
    setActiveTypes((prev) => {
      const next = new Set(prev);
      if (next.has(type)) {
        if (next.size > 1) next.delete(type);
      } else {
        next.add(type);
      }
      return next;
    });
  }, []);

  /* ---- draw frame (visual only, no physics) ---- */
  const drawFrame = useCallback(() => {
    const canvas = canvasRef.current;
    const sim = simulationRef.current;
    if (!sim || !canvas) return;

    const { w: width, h: height } = canvasSizeRef.current;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const dpr = window.devicePixelRatio;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, width, height);

    const t = transformRef.current;
    ctx.save();
    ctx.translate(t.x, t.y);
    ctx.scale(t.scale, t.scale);

    const hovered = hoveredRef.current;

    // edges
    ctx.strokeStyle = "rgba(160,164,171,0.25)";
    ctx.lineWidth = 0.5;
    for (const e of sim.edges) {
      const s = e.source as GraphNode;
      const tgt = e.target as GraphNode;
      ctx.beginPath();
      ctx.moveTo(s.x!, s.y!);
      ctx.lineTo(tgt.x!, tgt.y!);
      ctx.stroke();
    }

    // nodes
    for (const n of sim.nodes) {
      const r = NODE_RADIUS[n.type] ?? 5;
      const color = NODE_COLORS[n.type] ?? "#888";
      ctx.beginPath();
      ctx.arc(n.x!, n.y!, r, 0, Math.PI * 2);
      ctx.fillStyle = n === hovered ? "#fff" : color;
      ctx.fill();
      if (n === hovered) {
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.fillStyle =
          document.documentElement.getAttribute("data-theme") === "dark"
            ? "#e0e0e0"
            : "#202122";
        ctx.font = "11px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(n.title, n.x!, n.y! - r - 5);
      }
    }

    ctx.restore();
  }, []);

  /* ---- physics tick ---- */
  const tick = useCallback(() => {
    const sim = simulationRef.current;
    if (!sim || sim.alpha < 0.001) return;

    const { w: width, h: height } = canvasSizeRef.current;
    sim.alpha *= 0.98; // fast convergence (~5 s)
    const centerX = width / 2;
    const centerY = height / 2;

    // strong velocity damping
    for (const n of sim.nodes) {
      n.vx = (n.vx ?? 0) * 0.6;
      n.vy = (n.vy ?? 0) * 0.6;
    }

    // center gravity
    for (const n of sim.nodes) {
      n.vx! += (centerX - n.x!) * 0.0005 * sim.alpha;
      n.vy! += (centerY - n.y!) * 0.0005 * sim.alpha;
    }

    // repulsion
    for (let i = 0; i < sim.nodes.length; i++) {
      for (let j = i + 1; j < sim.nodes.length; j++) {
        const a = sim.nodes[i];
        const b = sim.nodes[j];
        let dx = b.x! - a.x!;
        let dy = b.y! - a.y!;
        const dist2 = dx * dx + dy * dy;
        const minDist = 400;
        if (dist2 < minDist * minDist && dist2 > 0) {
          const dist = Math.sqrt(dist2);
          const force = (80 * sim.alpha) / dist;
          dx /= dist;
          dy /= dist;
          a.vx! -= dx * force;
          a.vy! -= dy * force;
          b.vx! += dx * force;
          b.vy! += dy * force;
        }
      }
    }

    // attraction along edges
    for (const e of sim.edges) {
      const s = e.source as GraphNode;
      const tNode = e.target as GraphNode;
      const dx = tNode.x! - s.x!;
      const dy = tNode.y! - s.y!;
      const dist = Math.sqrt(dx * dx + dy * dy) || 1;
      const force = (dist - 60) * 0.003 * sim.alpha;
      const fx = (dx / dist) * force;
      const fy = (dy / dist) * force;
      s.vx! += fx;
      s.vy! += fy;
      tNode.vx! -= fx;
      tNode.vy! -= fy;
    }

    // apply velocities
    for (const n of sim.nodes) {
      if (dragRef.current.node === n) continue;
      n.x! += n.vx!;
      n.y! += n.vy!;
      n.x = Math.max(20, Math.min(width - 20, n.x!));
      n.y = Math.max(20, Math.min(height - 20, n.y!));
    }
  }, []);

  /* ---- animation loop ---- */
  const startLoop = useCallback(() => {
    if (animRef.current) cancelAnimationFrame(animRef.current);
    settledRef.current = false;
    setSettled(false);

    const loop = () => {
      tick();
      drawFrame();
      const sim = simulationRef.current;
      if (sim && sim.alpha >= 0.001) {
        animRef.current = requestAnimationFrame(loop);
      } else {
        // simulation settled — stop the loop
        settledRef.current = true;
        setSettled(true);
        drawFrame();
        animRef.current = 0;
      }
    };
    animRef.current = requestAnimationFrame(loop);
  }, [tick, drawFrame]);

  /* ---- single redraw when physics are settled ---- */
  const scheduleRedraw = useCallback(() => {
    if (!settledRef.current) return;
    if (needsRedrawRef.current) return;
    needsRedrawRef.current = true;
    requestAnimationFrame(() => {
      needsRedrawRef.current = false;
      drawFrame();
    });
  }, [drawFrame]);

  /* ---- hover helper (never restarts physics) ---- */
  const setHover = useCallback(
    (node: GraphNode | null) => {
      hoveredRef.current = node;
      setHoveredNode(node);
      scheduleRedraw();
    },
    [scheduleRedraw],
  );

  /* ---- simulation setup (NO hoveredNode in deps) ---- */
  useEffect(() => {
    if (!data || !canvasRef.current) return;

    const canvas = canvasRef.current;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    canvas.width = width * window.devicePixelRatio;
    canvas.height = height * window.devicePixelRatio;
    canvasSizeRef.current = { w: width, h: height };

    const filteredNodeIds = new Set(
      data.nodes.filter((n) => activeTypes.has(n.type)).map((n) => n.id),
    );
    const nodes: GraphNode[] = data.nodes
      .filter((n) => filteredNodeIds.has(n.id))
      .map((n) => ({
        ...n,
        x: n.x ?? width / 2 + (Math.random() - 0.5) * width * 0.8,
        y: n.y ?? height / 2 + (Math.random() - 0.5) * height * 0.8,
        vx: 0,
        vy: 0,
      }));

    const nodeMap = new Map(nodes.map((n) => [n.id, n]));
    const edges: GraphEdge[] = data.edges
      .filter((e) => {
        const sId = typeof e.source === "string" ? e.source : e.source.id;
        const tId = typeof e.target === "string" ? e.target : e.target.id;
        return nodeMap.has(sId) && nodeMap.has(tId);
      })
      .map((e) => ({
        source: nodeMap.get(
          typeof e.source === "string" ? e.source : e.source.id,
        )!,
        target: nodeMap.get(
          typeof e.target === "string" ? e.target : e.target.id,
        )!,
        type: e.type,
      }));

    simulationRef.current = { nodes, edges, alpha: 1 };
    transformRef.current = { x: 0, y: 0, scale: 1 };
    hoveredRef.current = null;

    startLoop();

    return () => {
      cancelAnimationFrame(animRef.current);
      animRef.current = 0;
    };
  }, [data, activeTypes, startLoop]);

  /* ---- mouse interaction ---- */
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    function toWorld(clientX: number, clientY: number) {
      const rect = canvas!.getBoundingClientRect();
      const t = transformRef.current;
      return {
        x: (clientX - rect.left - t.x) / t.scale,
        y: (clientY - rect.top - t.y) / t.scale,
      };
    }

    function findNode(wx: number, wy: number): GraphNode | null {
      const sim = simulationRef.current;
      if (!sim) return null;
      for (let i = sim.nodes.length - 1; i >= 0; i--) {
        const n = sim.nodes[i];
        const r = (NODE_RADIUS[n.type] ?? 5) + 3;
        if ((n.x! - wx) ** 2 + (n.y! - wy) ** 2 < r * r) return n;
      }
      return null;
    }

    function restartIfSettled(alpha: number) {
      const sim = simulationRef.current;
      if (!sim) return;
      sim.alpha = Math.max(sim.alpha, alpha);
      if (settledRef.current) startLoop();
    }

    function handleMouseMove(e: MouseEvent) {
      const { x, y } = toWorld(e.clientX, e.clientY);
      if (dragRef.current.node) {
        dragRef.current.node.x = x;
        dragRef.current.node.y = y;
        restartIfSettled(0.1);
      } else if (dragRef.current.panning) {
        transformRef.current.x += e.movementX;
        transformRef.current.y += e.movementY;
        scheduleRedraw();
      } else {
        const node = findNode(x, y);
        setHover(node);
        canvas!.style.cursor = node ? "pointer" : "grab";
      }
    }

    function handleMouseDown(e: MouseEvent) {
      const { x, y } = toWorld(e.clientX, e.clientY);
      const node = findNode(x, y);
      if (node) {
        dragRef.current = { node, startX: x, startY: y, panning: false };
        restartIfSettled(0.3);
      } else {
        dragRef.current = {
          node: null,
          startX: e.clientX,
          startY: e.clientY,
          panning: true,
        };
      }
    }

    function handleMouseUp(e: MouseEvent) {
      if (dragRef.current.node) {
        const { x, y } = toWorld(e.clientX, e.clientY);
        const dist =
          Math.abs(x - dragRef.current.startX) +
          Math.abs(y - dragRef.current.startY);
        if (dist < 5) {
          const route = nodeRoute(dragRef.current.node);
          if (route) router.push(route);
        }
      }
      dragRef.current = { node: null, startX: 0, startY: 0, panning: false };
    }

    function handleWheel(e: WheelEvent) {
      e.preventDefault();
      const rect = canvas!.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;
      const t = transformRef.current;
      const zoom = e.deltaY < 0 ? 1.1 : 0.9;
      const newScale = Math.max(0.2, Math.min(5, t.scale * zoom));
      t.x = mx - (mx - t.x) * (newScale / t.scale);
      t.y = my - (my - t.y) * (newScale / t.scale);
      t.scale = newScale;
      scheduleRedraw();
    }

    function handleMouseLeave() {
      dragRef.current = { node: null, startX: 0, startY: 0, panning: false };
      setHover(null);
    }

    canvas.addEventListener("mousemove", handleMouseMove);
    canvas.addEventListener("mousedown", handleMouseDown);
    canvas.addEventListener("mouseup", handleMouseUp);
    canvas.addEventListener("mouseleave", handleMouseLeave);
    canvas.addEventListener("wheel", handleWheel, { passive: false });

    return () => {
      canvas.removeEventListener("mousemove", handleMouseMove);
      canvas.removeEventListener("mousedown", handleMouseDown);
      canvas.removeEventListener("mouseup", handleMouseUp);
      canvas.removeEventListener("mouseleave", handleMouseLeave);
      canvas.removeEventListener("wheel", handleWheel);
    };
  }, [router, setHover, startLoop, scheduleRedraw]);

  return (
    <section className="graph-page">
      <header className="page-header">
        <h1>Grafo de conocimiento</h1>
        <p>
          Visualizacion interactiva de las conexiones entre conceptos, autores,
          cursos y fuentes. Haz clic en un nodo para ir al articulo. Arrastra
          para mover, scroll para zoom.
        </p>
      </header>

      <div className="graph-filters">
        {Object.entries(NODE_LABELS).map(([type, label]) => (
          <button
            key={type}
            className={activeTypes.has(type) ? "is-active" : undefined}
            onClick={() => toggleType(type)}
            style={{ borderLeft: `4px solid ${NODE_COLORS[type]}` }}
          >
            {label}
          </button>
        ))}
      </div>

      <div className="graph-legend">
        {Object.entries(NODE_LABELS).map(([type, label]) => (
          <span key={type} className="graph-legend__item">
            <span
              className="graph-legend__dot"
              style={{ background: NODE_COLORS[type] }}
            />
            {label}
          </span>
        ))}
        {data ? (
          <span
            style={{
              marginLeft: "auto",
              color: "var(--muted)",
              fontSize: "0.85rem",
            }}
          >
            {data.nodes.length} nodos · {data.edges.length} conexiones
            {settled ? " · Estabilizado ✓" : " · Calculando…"}
          </span>
        ) : null}
      </div>

      {error ? (
        <p className="empty-state">{error}</p>
      ) : !data ? (
        <p className="empty-state">Cargando grafo...</p>
      ) : null}

      <div className="graph-container" style={{ height: "70vh" }}>
        <canvas
          ref={canvasRef}
          style={{ width: "100%", height: "100%", cursor: "grab" }}
        />
      </div>
    </section>
  );
}
