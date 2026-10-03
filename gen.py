import math, os

OUT = "/home/claude/profile/assets"
os.makedirs(OUT, exist_ok=True)

MONO = "'JetBrains Mono','Fira Code',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SERIF = "Georgia,'Times New Roman',serif"
INK, PANEL, LINE = "#0b1020", "#121a33", "#26335f"
SIG, LAG, AMB, TXT, MUT = "#7dd3fc", "#fb7185", "#fbbf24", "#e6e9f5", "#8b95b8"


def wave(x0, x1, base, amp, step=6, phase=0.0):
    pts = []
    x = x0
    while x <= x1:
        t = x / 1200 * 2 * math.pi
        y = base - amp * (0.62 * math.sin(2 * t + phase) + 0.28 * math.sin(5 * t + 1.1 + phase) + 0.10 * math.sin(11 * t))
        pts.append(f"{x:.0f},{y:.1f}")
        x += step
    return "M" + " L".join(pts)


def write(name, body):
    with open(f"{OUT}/{name}", "w") as f:
        f.write(body)


def grid(w, h, gap=40, op=0.05):
    s = []
    for x in range(0, w + 1, gap):
        s.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>')
    for y in range(0, h + 1, gap):
        s.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>')
    return f'<g stroke="#fff" stroke-opacity="{op}" stroke-width="1">' + "".join(s) + "</g>"


# ---------------------------------------------------------------- HERO
def hero():
    W, H = 1200, 460
    real = wave(0, 1200, 370, 52)
    phrases = [
        "I make ML small enough to live inside the kernel.",
        "Predictive autoscaling that spends less energy.",
        "Digital twins, and what breaks when they go stale.",
        "Papers, hackathons, and things that ship.",
    ]
    ph = ""
    for i, p in enumerate(phrases):
        ph += (
            f'<text x="64" y="246" font-family="{MONO}" font-size="21" fill="{AMB}" opacity="0">{p}'
            f'<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.03;0.22;0.25;1" dur="14s" begin="{i*3.5}s" repeatCount="indefinite"/></text>'
        )
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Yash Lund, AI and systems researcher">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1020"/><stop offset="1" stop-color="#141b3a"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7dd3fc" stop-opacity="0"/><stop offset=".5" stop-color="#7dd3fc" stop-opacity=".9"/><stop offset="1" stop-color="#7dd3fc" stop-opacity="0"/></linearGradient>
<clipPath id="c"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#c)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
{grid(W, H)}
<line x1="0" y1="370" x2="{W}" y2="370" stroke="#fff" stroke-opacity=".12" stroke-dasharray="2 8"/>
<text x="64" y="64" font-family="{MONO}" font-size="15" fill="{MUT}">B.Tech, AI &amp; ML, year 3. Open to research and ML-systems roles.</text>
<g font-family="{SERIF}" font-weight="700" font-size="112" letter-spacing="-2">
<text x="60" y="176" fill="{LAG}" opacity=".55"><animateTransform attributeName="transform" type="translate" values="0 0;-5 0;4 0;0 0;0 0" keyTimes="0;0.015;0.03;0.045;1" dur="7s" repeatCount="indefinite"/>Yash Lund</text>
<text x="60" y="176" fill="{SIG}" opacity=".55"><animateTransform attributeName="transform" type="translate" values="0 0;5 0;-4 0;0 0;0 0" keyTimes="0;0.015;0.03;0.045;1" dur="7s" repeatCount="indefinite"/>Yash Lund</text>
<text x="60" y="176" fill="{TXT}">Yash Lund</text>
</g>
{ph}
<path d="{real}" fill="none" stroke="{SIG}" stroke-width="2.6" stroke-linejoin="round"/>
<g>
<animateTransform attributeName="transform" type="translate" values="30 0;110 0;30 0" dur="9s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".4 0 .6 1;.4 0 .6 1"/>
<path d="{real}" fill="none" stroke="{LAG}" stroke-width="2.2" stroke-dasharray="7 6" stroke-linejoin="round"/>
</g>
<rect y="300" width="90" height="140" fill="url(#fade)" opacity=".16"><animate attributeName="x" values="-90;1200" dur="8s" repeatCount="indefinite"/></rect>
<g font-family="{MONO}" font-size="13">
<circle cx="1010" cy="60" r="4" fill="{SIG}"/><text x="1022" y="65" fill="{MUT}">live</text>
<circle cx="1082" cy="60" r="4" fill="{LAG}"/><text x="1094" y="65" fill="{MUT}">twin, stale</text>
</g>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{LINE}"/>
</svg>'''
    write("hero.svg", s)


# ---------------------------------------------------------------- TERMINAL
def terminal():
    W, H, C = 1000, 300, 18.0
    lines = [
        ("cmd", "whoami"),
        ("out", "yash: B.Tech AI &amp; ML, systems-AI researcher"),
        ("cmd", "cat focus.txt"),
        ("out", "ML that is cheap enough to run in the scheduler, the kernel, the grid"),
        ("cmd", "ls research/"),
        ("out", "aegis/   neuroos-lite/   digital-twin-staleness/"),
        ("cmd", "status"),
        ("out", "3 papers in progress. Open to collaborations."),
    ]
    fs, cw = 16, 9.6
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Terminal summary of Yash Lund">']
    s.append(f'<rect width="{W}" height="{H}" rx="14" fill="{PANEL}" stroke="{LINE}"/>')
    s.append(f'<path d="M0 14a14 14 0 0 1 14-14h{W-28}a14 14 0 0 1 14 14v26H0z" fill="#1a2447"/>')
    for i, c in enumerate(["#fb7185", "#fbbf24", "#7dd3fc"]):
        s.append(f'<circle cx="{26+i*20}" cy="20" r="6" fill="{c}"/>')
    s.append(f'<text x="{W/2}" y="25" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{MUT}">yash@lab: ~</text>')
    y0, dy, t = 76, 28, 0.6
    defs = []
    body = []
    for i, (kind, txt) in enumerate(lines):
        plain = txt.replace("&amp;", "&")
        n = len(plain)
        prefix = "$ " if kind == "cmd" else ""
        full = (len(prefix) + n) * cw
        d = n * 0.045 if kind == "cmd" else 0.5
        steps = n
        ks = [0.0, t / C]
        vs = [0.0, 0.0]
        for k in range(1, steps + 1):
            ks.append((t + d * k / steps) / C)
            vs.append(round(full * k / steps + 2, 1) if k < steps else round(full + 6, 1))
        ks.append(1.0)
        vs.append(round(full + 6, 1))
        y = y0 + i * dy
        defs.append(
            f'<clipPath id="l{i}"><rect x="28" y="{y-18}" width="0" height="26">'
            f'<animate attributeName="width" values="{";".join(str(v) for v in vs)}" keyTimes="{";".join(f"{k:.4f}" for k in ks)}" calcMode="discrete" dur="{C}s" repeatCount="indefinite"/></rect></clipPath>'
        )
        col = TXT if kind == "cmd" else (SIG if i in (1, 3) else AMB if i == 5 else MUT)
        if kind == "cmd":
            body.append(f'<g clip-path="url(#l{i})"><text x="28" y="{y}" font-family="{MONO}" font-size="{fs}"><tspan fill="{LAG}">$ </tspan><tspan fill="{TXT}">{txt}</tspan></text></g>')
        else:
            body.append(f'<g clip-path="url(#l{i})"><text x="28" y="{y}" font-family="{MONO}" font-size="{fs}" fill="{col}">{txt}</text></g>')
        t += d + 0.9
    s.append("<defs>" + "".join(defs) + "</defs>")
    s += body
    cy = y0 + len(lines) * dy - 20
    s.append(f'<rect x="28" y="{cy}" width="10" height="20" fill="{AMB}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
    s.append("</svg>")
    write("terminal.svg", "\n".join(s))


# ---------------------------------------------------------------- card helpers
def card_open(W, H, title, sub, tag):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}: {sub}">'
        f'<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{MUT}"/></marker></defs>'
        f'<rect width="{W}" height="{H}" rx="16" fill="{INK}" stroke="{LINE}"/>'
        f'{grid(W, H, 40, 0.035)}'
        f'<text x="32" y="52" font-family="{SERIF}" font-size="34" font-weight="700" fill="{TXT}">{title}</text>'
        f'<text x="32" y="80" font-family="{MONO}" font-size="14" fill="{MUT}">{sub}</text>'
        f'<text x="{W-32}" y="48" text-anchor="end" font-family="{MONO}" font-size="12" fill="{AMB}">{tag}</text>'
    )


def node(x, y, w, h, a, b, col=SIG):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{PANEL}" stroke="{col}" stroke-opacity=".7"/>'
        f'<text x="{x+w/2}" y="{y+h/2-3}" text-anchor="middle" font-family="{MONO}" font-size="15" font-weight="700" fill="{TXT}">{a}</text>'
        f'<text x="{x+w/2}" y="{y+h/2+17}" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{MUT}">{b}</text>'
    )


def chips(x, y, items, col=AMB):
    out, cx = [], x
    for it in items:
        c = col
        if isinstance(it, tuple):
            it, c = it
        plain = it.replace("&amp;", "&").replace("&lt;", "<")
        w = len(plain) * 7.6 + 26
        out.append(
            f'<rect x="{cx}" y="{y}" width="{w:.0f}" height="30" rx="15" fill="none" stroke="{c}" stroke-opacity=".6"/>'
            f'<text x="{cx+w/2:.0f}" y="{y+20}" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="{c}">{it}</text>'
        )
        cx += w + 10
    return "".join(out)


def pulse(path, dur, begin, col=AMB, r=4):
    return (
        f'<circle r="{r}" fill="{col}"><animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" path="{path}"/></circle>'
    )


# ---------------------------------------------------------------- AEGIS
def aegis():
    W, H = 1000, 340
    s = [card_open(W, H, "Aegis", "Predictive, energy-aware Kubernetes orchestration", "IEEE semester project")]
    xs = [32, 222, 412, 602, 792]
    labels = [("Telemetry", "Prometheus, Kepler"), ("Forecast", "LightGBM p10/p50/p90"), ("Optimize", "OR-Tools CP-SAT"), ("Schedule", "Go scheduler plugin"), ("Cluster", "Kubernetes")]
    for x, (a, b) in zip(xs, labels):
        s.append(node(x, 118, 176, 74, a, b))
    for i in range(4):
        x1, x2 = xs[i] + 176, xs[i + 1]
        s.append(f'<line x1="{x1}" y1="155" x2="{x2-2}" y2="155" stroke="{MUT}" stroke-width="1.6" marker-end="url(#ar)"/>')
        s.append(pulse(f"M{x1} 155 L{x2} 155", 1.4, i * 0.35, AMB))
    loop = f"M{xs[4]+88} 192 V250 H{xs[0]+88} V192"
    s.append(f'<path d="{loop}" fill="none" stroke="{LAG}" stroke-width="1.6" stroke-dasharray="6 6" marker-end="url(#ar)"><animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.2s" repeatCount="indefinite"/></path>')
    s.append(f'<text x="{W/2}" y="244" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="{LAG}">decision loop every 30 to 60 s, replaces reactive HPA</text>')
    s.append(chips(32, 284, ["15-25% less energy (target)", "20-35% fewer SLO violations (target)", "&lt;50 ms scheduling (target)"]))
    s.append("</svg>")
    write("aegis.svg", "\n".join(s))


# ---------------------------------------------------------------- NEUROOS
def neuroos():
    W, H = 1000, 404
    s = [card_open(W, H, "NeuroOS-Lite", "Learned preemption and memory partitioning inside the kernel", "systems AI, SOSP / IEEE Trans. target")]
    s.append(f'<text x="32" y="118" font-family="{MONO}" font-size="12.5" fill="{MUT}">off-path, local GPU: slow and heavy</text>')
    s.append(node(32, 130, 220, 62, "RL policy training", "PyTorch", LAG))
    s.append(node(322, 130, 260, 62, "Distill and quantize", "TensorRT to fixed-point", LAG))
    s.append(f'<line x1="252" y1="161" x2="320" y2="161" stroke="{MUT}" stroke-width="1.6" marker-end="url(#ar)"/>')
    s.append(pulse("M252 161 L320 161", 3.2, 0, LAG))
    s.append(f'<line x1="32" y1="226" x2="{W-32}" y2="226" stroke="{AMB}" stroke-opacity=".7" stroke-dasharray="3 7"/>')
    s.append(f'<text x="{W-32}" y="218" text-anchor="end" font-family="{MONO}" font-size="12" fill="{AMB}">kernel boundary</text>')
    s.append(f'<line x1="452" y1="192" x2="452" y2="262" stroke="{LAG}" stroke-width="1.6" stroke-dasharray="5 5" marker-end="url(#ar)"/>')
    s.append(f'<text x="464" y="236" font-family="{MONO}" font-size="12" fill="{LAG}">ship weights</text>')
    s.append(f'<text x="32" y="254" font-family="{MONO}" font-size="12.5" fill="{MUT}">in-kernel fast path: no floats, no GPU</text>')
    s.append(node(32, 264, 220, 62, "Run-queue state", "sched_ext, eBPF"))
    s.append(node(322, 264, 260, 62, "SIMD policy, &lt;45 ns", "AVX2 / NEON fixed-point"))
    s.append(node(652, 264, 220, 62, "Dispatch", "pick next task"))
    for x1, x2 in [(252, 320), (582, 650)]:
        s.append(f'<line x1="{x1}" y1="295" x2="{x2}" y2="295" stroke="{MUT}" stroke-width="1.6" marker-end="url(#ar)"/>')
        for k in range(3):
            s.append(pulse(f"M{x1} 295 L{x2} 295", 0.45, k * 0.15, SIG, 3.5))
    s.append(chips(32, 352, ["-28.4% mean turnaround", "-41.2% p99 wait", "-38.9% memory fragmentation"], SIG))
    s.append("</svg>")
    write("neuroos.svg", "\n".join(s))


# ---------------------------------------------------------------- DIGITAL TWIN
def twin():
    W, H = 1000, 366
    s = [card_open(W, H, "Digital Twin Staleness", "How a lagging twin degrades load estimation and anomaly detection", "IEEE research spec v2")]
    cx, cy, cw, ch = 32, 104, 600, 170
    s.append(f'<clipPath id="cp"><rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="8"/></clipPath>')
    s.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="8" fill="{PANEL}" stroke="{LINE}"/>')
    pts = []
    for x in range(0, cw + 1, 5):
        t = x / cw * 2 * math.pi
        y = cy + ch / 2 - 46 * (0.6 * math.sin(2 * t) + 0.3 * math.sin(5 * t + 1) + 0.1 * math.sin(11 * t))
        pts.append(f"{cx+x},{y:.1f}")
    p = "M" + " L".join(pts)
    s.append('<g clip-path="url(#cp)">')
    s.append(f'<path d="{p}" fill="none" stroke="{SIG}" stroke-width="2.4"/>')
    s.append(f'<g><animateTransform attributeName="transform" type="translate" values="12 0;70 0;12 0" dur="8s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".4 0 .6 1;.4 0 .6 1"/><path d="{p}" fill="none" stroke="{LAG}" stroke-width="2.2" stroke-dasharray="6 5"/></g>')
    s.append("</g>")
    s.append(f'<circle cx="{cx+16}" cy="{cy+18}" r="4" fill="{SIG}"/><text x="{cx+28}" y="{cy+22}" font-family="{MONO}" font-size="12" fill="{MUT}">feeder load, live</text>')
    s.append(f'<circle cx="{cx+170}" cy="{cy+18}" r="4" fill="{LAG}"/><text x="{cx+182}" y="{cy+22}" font-family="{MONO}" font-size="12" fill="{MUT}">twin, staleness as the controlled variable</text>')
    s.append(f'<text x="{cx+cw/2}" y="{cy+ch+22}" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{AMB}">sweep the lag, measure what breaks</text>')
    models = ["LSTM", "LSTM Autoencoder", "Isolation Forest", "XGBoost"]
    s.append(f'<text x="672" y="122" font-family="{MONO}" font-size="12.5" fill="{MUT}">models under test</text>')
    for i, m in enumerate(models):
        y = 134 + i * 36
        s.append(f'<rect x="672" y="{y}" width="296" height="28" rx="8" fill="{PANEL}" stroke="{LINE}"/><text x="688" y="{y+19}" font-family="{MONO}" font-size="13.5" fill="{TXT}">{m}</text>')
    s.append(chips(32, 312, ["IEEE 33-bus", "OpenDSS + pandapower", "Pecan Street loads", "fault injection", "SHAP"], SIG))
    s.append("</svg>")
    write("twin.svg", "\n".join(s))


# ---------------------------------------------------------------- STACK
def stack():
    W = 1000
    rows = [
        ("GenAI and RAG", SIG, "LangChain  HuggingFace  FAISS  ChromaDB  Pinecone  Ollama  OpenAI API"),
        ("Learning", "#a78bfa", "PyTorch  TensorFlow/Keras  scikit-learn  LightGBM  XGBoost  SHAP  Federated Learning"),
        ("Optimization", AMB, "OR-Tools CP-SAT  RL policy distillation  quantile forecasting"),
        ("Systems", LAG, "C  Go  Linux sched_ext  eBPF  AVX2/NEON SIMD  TensorRT"),
        ("Platform", "#34d399", "Kubernetes  Docker  Prometheus  Kepler  Grafana  FastAPI  Redis  MLflow"),
        ("Domain", "#f0abfc", "OpenDSS  pandapower  Pecan Street  medical time-series  agri-tech"),
    ]
    rh, gap = 52, 10
    H = 24 + len(rows) * (rh + gap) + 14
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Technology stack by layer">']
    s.append(f'<rect width="{W}" height="{H}" rx="16" fill="{INK}" stroke="{LINE}"/>')
    for i, (name, col, items) in enumerate(rows):
        y = 24 + i * (rh + gap)
        s.append(f'<rect x="24" y="{y}" width="{W-48}" height="{rh}" rx="10" fill="{col}" fill-opacity=".07" stroke="{col}" stroke-opacity=".45"/>')
        s.append(f'<rect x="24" y="{y}" width="176" height="{rh}" rx="10" fill="{col}" fill-opacity=".22"><animate attributeName="fill-opacity" values=".16;.34;.16" dur="5s" begin="{i*0.7}s" repeatCount="indefinite"/></rect>')
        s.append(f'<text x="112" y="{y+rh/2+5}" text-anchor="middle" font-family="{SERIF}" font-size="18" font-weight="700" fill="{TXT}">{name}</text>')
        s.append(f'<text x="220" y="{y+rh/2+5}" font-family="{MONO}" font-size="13.5" fill="{TXT}" xml:space="preserve">{items}</text>')
    s.append("</svg>")
    write("stack.svg", "\n".join(s))


# ---------------------------------------------------------------- DIVIDER
def divider():
    W = 1000
    p = "M0 20 H380 l10 -3 l8 3 H440 l6 0 l7 -15 l9 30 l9 -24 l6 9 H640 l10 -3 l8 3 H1000"
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 40" width="{W}" height="40" role="presentation">
<path d="{p}" fill="none" stroke="{LINE}" stroke-width="1.5"/>
<path d="{p}" fill="none" stroke="{SIG}" stroke-width="2" stroke-dasharray="140 1400" pathLength="1540"><animate attributeName="stroke-dashoffset" from="140" to="-1540" dur="5s" repeatCount="indefinite"/></path>
</svg>'''
    write("divider.svg", s)


if __name__ == "__main__":
    for f in (hero, stack, divider):
        f()
