from gen import *

# ---------------------------------------------------------------- TERMINAL
def terminal():
    W, H, C = 1000, 300, 18.0
    lines = [
        ("cmd", "whoami"),
        ("out", "yash: B.Tech AI &amp; ML, systems-AI researcher"),
        ("cmd", "cat focus.txt"),
        ("out", "ML that is cheap and fast enough to run in the scheduler, the kernel, the grid"),
        ("cmd", "ls research/"),
        ("out", "aegis-cloud/   os-subsystem/   digital-twins-ieee/"),
        ("cmd", "git log --since='30 days' --format=%h | wc -l"),
        ("out", "7 repos active this month. Open to collaborations."),
    ]
    fs, cw = 16, 9.6
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Terminal summary of Yash Lund">']
    s.append(f'<rect width="{W}" height="{H}" rx="14" fill="{PANEL}" stroke="{LINE}"/>')
    s.append(f'<path d="M0 14a14 14 0 0 1 14-14h{W-28}a14 14 0 0 1 14 14v26H0z" fill="#1a2447"/>')
    for i, c in enumerate(["#fb7185", "#fbbf24", "#7dd3fc"]):
        s.append(f'<circle cx="{26+i*20}" cy="20" r="6" fill="{c}"/>')
    s.append(f'<text x="{W/2}" y="25" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{MUT}">yash@lab: ~</text>')
    y0, dy, t = 76, 28, 0.6
    defs, body = [], []
    for i, (kind, txt) in enumerate(lines):
        plain = txt.replace("&amp;", "&")
        n = len(plain)
        full = (n + (2 if kind == "cmd" else 0)) * cw
        d = n * 0.04 if kind == "cmd" else 0.6
        ks, vs = [0.0, t / C], [0.0, 0.0]
        for k in range(1, n + 1):
            ks.append((t + d * k / n) / C)
            vs.append(round(full * k / n + 2, 1) if k < n else round(full + 6, 1))
        ks.append(1.0); vs.append(round(full + 6, 1))
        y = y0 + i * dy
        defs.append(f'<clipPath id="l{i}"><rect x="28" y="{y-18}" width="{full+6:.0f}" height="26"><animate attributeName="width" values="{";".join(str(v) for v in vs)}" keyTimes="{";".join(f"{k:.4f}" for k in ks)}" calcMode="discrete" dur="{C}s" repeatCount="indefinite"/></rect></clipPath>')
        col = SIG if i in (1, 3) else AMB if i in (5, 7) else MUT
        if kind == "cmd":
            body.append(f'<g clip-path="url(#l{i})"><text x="28" y="{y}" font-family="{MONO}" font-size="{fs}" xml:space="preserve"><tspan fill="{LAG}">$ </tspan><tspan fill="{TXT}">{txt}</tspan></text></g>')
        else:
            body.append(f'<g clip-path="url(#l{i})"><text x="28" y="{y}" font-family="{MONO}" font-size="{fs}" fill="{col}">{txt}</text></g>')
        t += d + 0.9
    s.append("<defs>" + "".join(defs) + "</defs>"); s += body
    cy = y0 + len(lines) * dy - 20
    s.append(f'<rect x="28" y="{cy}" width="10" height="20" fill="{AMB}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect></svg>')
    write("terminal.svg", "\n".join(s))

# ---------------------------------------------------------------- TICKER
def ticker():
    items = [
        "Aegis: p90 forecast coverage 90.0% on 20 unseen Azure apps",
        "Aegis: 38.8 kWh less than Cluster Autoscaler at 0% shortfall",
        "NeuroOS student: 7 to 24% lower mean wait than MLFQ on heavy-tailed loads",
        "Digital twin: detector F1 0.978 falls to about 0.1 past 5 s of staleness",
        "Sonar: mAP@0.5 80.7%, 44.6 ms per frame on CPU",
        "Network twin: root cause top-1 84.6% on single faults",
        "Weather blend: 7.9% better rain RMSE, 6.2% better wind RMSE than naive",
    ]
    sep = "   //   "
    txt = sep.join(items) + sep
    cw = 8.4
    W = 1000
    tw = len(txt) * cw
    dur = tw / 55
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 46" width="{W}" height="46" role="img" aria-label="Verified results from recent projects">
<defs><clipPath id="tc"><rect width="{W}" height="46" rx="10"/></clipPath>
<linearGradient id="ef" x1="0" x2="1"><stop offset="0" stop-color="{INK}"/><stop offset=".06" stop-color="{INK}" stop-opacity="0"/><stop offset=".94" stop-color="{INK}" stop-opacity="0"/><stop offset="1" stop-color="{INK}"/></linearGradient></defs>
<rect width="{W}" height="46" rx="10" fill="{PANEL}" stroke="{LINE}"/>
<g clip-path="url(#tc)">
<g font-family="{MONO}" font-size="14" fill="{AMB}" xml:space="preserve">
<animateTransform attributeName="transform" type="translate" from="0 0" to="-{tw:.0f} 0" dur="{dur:.1f}s" repeatCount="indefinite"/>
<text x="0" y="28">{txt}</text><text x="{tw:.0f}" y="28">{txt}</text>
</g>
<rect width="{W}" height="46" fill="url(#ef)"/></g></svg>'''
    write("ticker.svg", s)

# ---------------------------------------------------------------- AEGIS
def aegis():
    W, H = 1000, 340
    s = [card_open(W, H, "Aegis", "Quantile forecasting + CP-SAT scheduling for Kubernetes", "trace-driven, Azure Functions 2019")]
    xs = [32, 222, 412, 602, 792]
    labels = [("Telemetry", "Prometheus, Kepler"), ("Forecast", "LightGBM + conformal"), ("Optimize", "OR-Tools CP-SAT"), ("Schedule", "Go plugin, autoscaler"), ("Cluster", "Kubernetes")]
    for x, (a, b) in zip(xs, labels):
        s.append(node(x, 118, 176, 74, a, b))
    for i in range(4):
        x1, x2 = xs[i] + 176, xs[i + 1]
        s.append(f'<line x1="{x1}" y1="155" x2="{x2-2}" y2="155" stroke="{MUT}" stroke-width="1.6" marker-end="url(#ar)"/>')
        s.append(pulse(f"M{x1} 155 L{x2} 155", 1.4, i * 0.35, AMB))
    loop = f"M{xs[4]+88} 192 V250 H{xs[0]+88} V192"
    s.append(f'<path d="{loop}" fill="none" stroke="{LAG}" stroke-width="1.6" stroke-dasharray="6 6" marker-end="url(#ar)"><animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.2s" repeatCount="indefinite"/></path>')
    s.append(f'<text x="{W/2}" y="244" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="{LAG}">closed loop every 30 to 60 s, replaces reactive HPA</text>')
    s.append(chips(32, 284, ["20 unseen apps, 14 days", "-38.8 kWh vs Cluster Autoscaler at 0% shortfall", "p90 coverage 90.0%"]))
    s.append("</svg>")
    write("aegis.svg", "\n".join(s))

# ---------------------------------------------------------------- NEUROOS
def neuroos():
    W, H = 1000, 404
    s = [card_open(W, H, "NeuroOS-Lite", "Learned preemption and memory partitioning for the OS dispatch path", "simulator results, kernel latency pending")]
    s.append(f'<text x="32" y="118" font-family="{MONO}" font-size="12.5" fill="{MUT}">off-path, local GPU: slow and heavy</text>')
    s.append(node(32, 130, 220, 62, "Policy training", "behavior cloning + PPO", LAG))
    s.append(node(322, 130, 260, 62, "Distill and quantize", "int8, 16 to 8 to 1 MLP", LAG))
    s.append(f'<line x1="252" y1="161" x2="320" y2="161" stroke="{MUT}" stroke-width="1.6" marker-end="url(#ar)"/>')
    s.append(pulse("M252 161 L320 161", 3.2, 0, LAG))
    s.append(f'<line x1="32" y1="226" x2="{W-32}" y2="226" stroke="{AMB}" stroke-opacity=".7" stroke-dasharray="3 7"/>')
    s.append(f'<text x="{W-32}" y="218" text-anchor="end" font-family="{MONO}" font-size="12" fill="{AMB}">kernel boundary</text>')
    s.append(f'<line x1="452" y1="192" x2="452" y2="262" stroke="{LAG}" stroke-width="1.6" stroke-dasharray="5 5" marker-end="url(#ar)"/>')
    s.append(f'<text x="464" y="236" font-family="{MONO}" font-size="12" fill="{LAG}">ship weights</text>')
    s.append(f'<text x="32" y="254" font-family="{MONO}" font-size="12.5" fill="{MUT}">in-kernel fast path: integer math, no GPU, guardrail fallback</text>')
    s.append(node(32, 264, 220, 62, "Run-queue state", "sched_ext, PMU telemetry"))
    s.append(node(322, 264, 260, 62, "Integer policy", "target 45 ns or less"))
    s.append(node(652, 264, 220, 62, "Dispatch", "quantum, preempt, place"))
    for x1, x2 in [(252, 320), (582, 650)]:
        s.append(f'<line x1="{x1}" y1="295" x2="{x2}" y2="295" stroke="{MUT}" stroke-width="1.6" marker-end="url(#ar)"/>')
        for k in range(3):
            s.append(pulse(f"M{x1} 295 L{x2} 295", 0.45, k * 0.15, SIG, 3.5))
    s.append(chips(32, 352, ["30 seeds, simulator", "7-24% lower mean wait than MLFQ (Pareto loads)", ("45 ns: target, not yet measured", LAG)], SIG))
    s.append("</svg>")
    write("neuroos.svg", "\n".join(s))

# ---------------------------------------------------------------- TWIN
def twin():
    W, H = 1000, 366
    s = [card_open(W, H, "Digital Twin Staleness", "What happens to anomaly detection when the twin goes stale", "IEEE TSG manuscript")]
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
    s.append(f'<g><animateTransform attributeName="transform" type="translate" values="12 0;70 0;12 0" dur="8s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".4 0 .6 1;.4 0 .6 1"/><path d="{p}" fill="none" stroke="{LAG}" stroke-width="2.2" stroke-dasharray="6 5"/></g></g>')
    s.append(f'<circle cx="{cx+16}" cy="{cy+18}" r="4" fill="{SIG}"/><text x="{cx+28}" y="{cy+22}" font-family="{MONO}" font-size="12" fill="{MUT}">feeder load, live</text>')
    s.append(f'<circle cx="{cx+170}" cy="{cy+18}" r="4" fill="{LAG}"/><text x="{cx+182}" y="{cy+22}" font-family="{MONO}" font-size="12" fill="{MUT}">twin, staleness as the controlled variable</text>')
    s.append(f'<text x="{cx+cw/2}" y="{cy+ch+22}" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{AMB}">sweep the lag, measure what breaks</text>')
    # mini result chart: residual LSTM-AE F1 vs staleness (read from the repo's fig 03)
    px, py, pw, ph = 690, 128, 270, 124
    s.append(f'<text x="672" y="118" font-family="{MONO}" font-size="12.5" fill="{MUT}">residual LSTM-AE, F1 vs staleness</text>')
    s.append(f'<rect x="{px-14}" y="{py-6}" width="{pw+28}" height="{ph+34}" rx="8" fill="{PANEL}" stroke="{LINE}"/>')
    labels = ["0", "1", "5", "15", "60", "300"]
    vals = [0.978, 0.978, 0.11, 0.095, 0.09, 0.09]
    xsr = [px + i * pw / 5 for i in range(6)]
    ysr = [py + ph - v * ph for v in vals]
    rawy = py + ph - 0.539 * ph
    s.append(f'<line x1="{px}" y1="{rawy:.1f}" x2="{px+pw}" y2="{rawy:.1f}" stroke="{AMB}" stroke-dasharray="5 4"/>')
    s.append(f'<text x="{px+pw}" y="{rawy-5:.1f}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{AMB}">raw baseline 0.539</text>')
    line = "M" + " L".join(f"{x:.0f},{y:.1f}" for x, y in zip(xsr, ysr))
    s.append(f'<path d="{line}" fill="none" stroke="{SIG}" stroke-width="2.4" stroke-dasharray="500" stroke-dashoffset="0"><animate attributeName="stroke-dashoffset" values="500;0;0;500" keyTimes="0;.35;.85;1" dur="7s" repeatCount="indefinite"/></path>')
    for x, y, lb in zip(xsr, ysr, labels):
        s.append(f'<circle cx="{x:.0f}" cy="{y:.1f}" r="3.5" fill="{SIG}"/><text x="{x:.0f}" y="{py+ph+16}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{MUT}">{lb}</text>')
    s.append(f'<text x="{px+pw/2}" y="{py+ph+32}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{MUT}">staleness (s)</text>')
    s.append(chips(32, 312, ["24-condition factorial sweep", "fresh twin: residual F1 0.978 vs raw 0.539", ("hypothesis H3 not supported", AMB)], SIG))
    s.append("</svg>")
    write("twin.svg", "\n".join(s))

if __name__ == "__main__":
    for f in (hero, terminal, ticker, aegis, neuroos, twin, stack, divider):
        f()
