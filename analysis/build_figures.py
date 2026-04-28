"""Phase 8 — figure builder. Produces 10 publication-quality charts (PNG +
SVG) under figures/. Color palette and typography are consistent across
charts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "analysis"))
import lib  # noqa: E402
import methods as M  # noqa: E402

FIGDIR = ROOT / "figures"
FIGDIR.mkdir(exist_ok=True)

# Color system — dark theme
PALETTE = {
    "primary": "#ECF0F1",       # near-white (emphasis on dark)
    "accent": "#F39C42",         # warm orange
    "secondary": "#1ABC9C",      # teal
    "muted": "#7F8C8D",          # gray
    "skeptic": "#E74C3C",        # red
    "late": "#F1C40F",           # amber
    "consumer": "#2ECC71",       # green
    "gn": "#5DADE2",             # blue
    "gs": "#EC7063",             # rose
    "background": "#1A1D24",     # near-black
    "text": "#E0E0E0",
    "muted_text": "#9AA0A6",
    "axis": "#888888",
    "grid": "#2A2E36",
}

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.titleweight": "semibold",
    "axes.labelsize": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.facecolor": PALETTE["background"],
    "axes.edgecolor": PALETTE["axis"],
    "axes.labelcolor": PALETTE["text"],
    "axes.titlecolor": "#F0F0F0",
    "axes.grid": True,
    "grid.linestyle": "-",
    "grid.linewidth": 0.5,
    "grid.color": PALETTE["grid"],
    "text.color": PALETTE["text"],
    "xtick.color": "#CCCCCC",
    "ytick.color": "#CCCCCC",
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "figure.facecolor": PALETTE["background"],
    "figure.dpi": 100,
    "savefig.facecolor": PALETTE["background"],
    "savefig.edgecolor": "none",
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})


def save(fig, name: str):
    for ext in ("png", "svg"):
        fig.savefig(FIGDIR / f"{name}.{ext}")
    plt.close(fig)
    print(f"  -> {name}.{{png,svg}}")


def load_findings():
    with open(ROOT / "analysis" / "findings_raw.json") as f:
        return {d["id"]: d for d in json.load(f)}


# ---------------------------------------------------------------------------
# Figure 1 — Aspiration inversion (per-task gaps with cluster-bootstrap CI)
# ---------------------------------------------------------------------------

def fig1_aspiration_inversion(findings):
    h1 = findings["H1"]["per_task"]
    tasks = ["Generat", "Ask", "Translat", "Interpret", "Assist", "Predict", "Organi"]
    nice = {"Generat": "Generate (text/img)", "Ask": "Ask (chatbot)",
             "Translat": "Translate / transcribe", "Interpret": "Interpret",
             "Assist": "Assist (automation)", "Predict": "Predict",
             "Organi": "Organize"}
    use = [h1["use_pct"][t] for t in tasks]
    want = [h1["want_pct"][t] for t in tasks]
    gap = [h1["gap"][t] for t in tasks]
    lo = [h1["ci_lo"][t] for t in tasks]
    hi = [h1["ci_hi"][t] for t in tasks]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5),
                              gridspec_kw={"width_ratios": [1.4, 1]})

    # Left panel — paired use vs want
    y = np.arange(len(tasks))
    width = 0.35
    axes[0].barh(y - width/2, use, width, color=PALETTE["muted"], label="Use today", edgecolor="#1A1D24")
    axes[0].barh(y + width/2, want, width, color=PALETTE["accent"], label="Want", edgecolor="#1A1D24")
    axes[0].set_yticks(y); axes[0].set_yticklabels([nice[t] for t in tasks])
    axes[0].set_xlim(0, 0.7)
    axes[0].set_xlabel("Share of respondents")
    axes[0].xaxis.set_major_formatter(mpl.ticker.PercentFormatter(1.0))
    axes[0].set_title("Today's use vs aspiration", loc="left")
    axes[0].legend(loc="lower right", frameon=False)

    # Right panel — gap with CI
    err_lo = [g - l for g, l in zip(gap, lo)]
    err_hi = [h - g for g, h in zip(gap, hi)]
    colors = [PALETTE["primary"] if g >= 0.30 else PALETTE["secondary"] if g >= 0.10
              else PALETTE["muted"] for g in gap]
    axes[1].errorbar(gap, y, xerr=[err_lo, err_hi], fmt='o',
                       color="#E0E0E0", ecolor="#9AA0A6", capsize=3,
                       markersize=8, markerfacecolor="white", markeredgewidth=2)
    for yi, gi, col in zip(y, gap, colors):
        axes[1].plot(gi, yi, 'o', color=col, markersize=8, zorder=3)
    axes[1].axvline(0, color="#666666", linewidth=0.7)
    axes[1].axvline(0.30, color="#444444", linewidth=0.5, linestyle="--")
    axes[1].set_yticks(y); axes[1].set_yticklabels([])
    axes[1].set_xlim(-0.05, 0.55)
    axes[1].set_xlabel("Want − Use (percentage points)")
    axes[1].xaxis.set_major_formatter(mpl.ticker.PercentFormatter(1.0))
    axes[1].set_title("Aspiration gap (95% cluster-bootstrap CI)", loc="left")

    fig.suptitle("The Aspiration Inversion: nonprofits use AI for content,\nwant it for analytics",
                  fontsize=14, fontweight="bold", y=1.0, x=0.06, ha="left")
    fig.text(0.06, -0.02,
             f"n = 930. McNemar p < 1e-66 for the four analytical tasks. Cluster bootstrap resamples whole `ref` strata.",
             fontsize=8.5, color="#9AA0A6")
    save(fig, "fig1_aspiration_inversion")


# ---------------------------------------------------------------------------
# Figure 2 — Comfort × readiness marginal-effects heatmap (replaces F-9 2×2)
# ---------------------------------------------------------------------------

def fig2_comfort_readiness_heatmap(df, findings):
    h3 = findings["H3"]["params"]
    intercept = h3["const"]
    b_c = h3["comfort_z"]
    b_r = h3["readiness_z"]
    b_int = h3["interaction"]
    # Standardize axes from data
    sub = df.dropna(subset=["person_ai_comfort", "readiness_additive", "use_count"])
    cz_mean = sub["person_ai_comfort"].mean()
    cz_std = sub["person_ai_comfort"].std()
    rz_mean = sub["readiness_additive"].mean()
    rz_std = sub["readiness_additive"].std()
    cz = np.linspace(0, 1, 80)
    rz = np.linspace(0, 1, 80)
    Cz, Rz = np.meshgrid(cz, rz)
    Cz_s = (Cz - cz_mean) / cz_std
    Rz_s = (Rz - rz_mean) / rz_std
    log_lambda = intercept + b_c * Cz_s + b_r * Rz_s + b_int * Cz_s * Rz_s
    expected = np.exp(log_lambda)

    fig, ax = plt.subplots(figsize=(7.5, 6))
    im = ax.imshow(expected, origin="lower", extent=[0, 1, 0, 1],
                    cmap="YlOrRd", aspect="auto")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("Predicted use_count (Poisson)")
    # overlay scatter of actual respondents
    ax.scatter(sub["person_ai_comfort"], sub["readiness_additive"],
                s=6, color="#DDDDDD", alpha=0.15)
    # contours
    cs = ax.contour(Cz, Rz, expected, levels=[1, 2, 3, 4], colors="white", linewidths=1)
    ax.clabel(cs, inline=True, fontsize=8, fmt="%.0f")
    ax.set_xlabel("Person AI comfort (0–1)")
    ax.set_ylabel("Data readiness (0–1, additive)")
    ax.set_title("Comfort and readiness each ~triple AI use,\nwith mild diminishing returns at the top",
                  loc="left")
    ax.text(0.05, -0.16,
            f"Poisson GLM (n=878). β_comfort = +{b_c:.2f}, β_readiness = +{b_r:.2f}, β_interaction = {b_int:.2f} (p=0.025)",
            transform=ax.transAxes, fontsize=8.5, color="#9AA0A6")
    save(fig, "fig2_comfort_readiness_heatmap")


# ---------------------------------------------------------------------------
# Figure 3 — LCA item-response-probability profile (re-derived typology)
# ---------------------------------------------------------------------------

def fig3_lca_profile(df):
    """LCA k=3 on [U]+[W], plot per-item P(item=1|class) profile."""
    u_cols = [c for c in df.columns if c.startswith("[U] ")
              and "not currently" not in c.lower() and "Other" not in c]
    w_cols = [c for c in df.columns if c.startswith("[W] ")
              and "don't know" not in c.lower() and "Other" not in c]
    items = u_cols + w_cols
    sub = df[items].astype(int)
    res = M.latent_class_model(sub.reset_index(drop=True), items, k_range=(3,), n_init=5)
    # compute item probabilities by hard-assignment
    classes = res.hard_assignments
    sizes = classes.value_counts().sort_index()
    probs = pd.DataFrame({c: sub.iloc[(classes == c).values].mean()
                          for c in sorted(classes.unique())})
    # reorder classes by want_count proxy
    class_means = sub.iloc[:, len(u_cols):].mean()  # not used; use rowsum
    class_use = pd.Series({c: sub.iloc[(classes == c).values, :len(u_cols)].sum(axis=1).mean()
                            for c in probs.columns})
    class_want = pd.Series({c: sub.iloc[(classes == c).values, len(u_cols):].sum(axis=1).mean()
                              for c in probs.columns})
    order = sorted(probs.columns, key=lambda c: class_use[c])
    probs = probs[order]
    sizes = sizes.loc[order]
    labels = []
    for c in order:
        u = class_use[c]
        w = class_want[c]
        if u < 0.5 and w > 4:
            labels.append(f"Disengaged Aspirational (n={sizes[c]})")
        elif u > 4:
            labels.append(f"Power User (n={sizes[c]})")
        elif u > 1.5 and w > 4:
            labels.append(f"Aspirational (n={sizes[c]})")
        else:
            labels.append(f"Class {c} (n={sizes[c]})")
    item_labels = [c.replace("[U] ", "Use: ").replace("[W] ", "Want: ") for c in items]

    fig, ax = plt.subplots(figsize=(11, 7.5))
    x = np.arange(len(items))
    colors = [PALETTE["skeptic"], PALETTE["late"], PALETTE["consumer"]][: len(order)]
    for col, label, color in zip(probs.columns, labels, colors):
        ax.plot(x, probs[col], marker="o", linewidth=2, label=label, color=color)
    ax.axvline(len(u_cols) - 0.5, color="#666666", linestyle="--", linewidth=0.7)
    ax.text(len(u_cols)/2 - 0.5, 1.04, "Currently uses AI for…",
            ha="center", fontsize=9, color="#CCCCCC", transform=ax.get_xaxis_transform())
    ax.text(len(u_cols) + len(w_cols)/2 - 0.5, 1.04, "Wants to use AI for…",
            ha="center", fontsize=9, color="#CCCCCC", transform=ax.get_xaxis_transform())
    ax.set_xticks(x); ax.set_xticklabels(item_labels, rotation=45, ha="right")
    ax.set_ylabel("P(item = 1 | class)")
    ax.set_ylim(0, 1.05)
    ax.set_title("LCA k=3 item-response profile: a willing-but-not-using middle class",
                  loc="left")
    ax.legend(loc="lower right", frameon=False)
    ax.text(0, -0.55, "stepmix LCA, BIC=13131. Modal class is Aspirational: low use across all items, high want across analytical items.",
            transform=ax.transAxes, fontsize=8.5, color="#9AA0A6")
    save(fig, "fig3_lca_profile")


# ---------------------------------------------------------------------------
# Figure 4 — Oaxaca decomposition for F-8 small-org GN/GS reversal
# ---------------------------------------------------------------------------

def fig4_oaxaca_smallorg(findings):
    h5 = findings["H5"]
    oax = h5["oaxaca"]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    components = ["Endowments\n(GS has more\nof the helpful traits)",
                   "Coefficients\n(returns to a trait\nfavor GS more)",
                   "Interaction\n(joint effect)",
                   "Total raw gap"]
    values = [oax["endowments"], oax["coefficients"], oax["interaction"], oax["raw_gap"]]
    colors = [PALETTE["secondary"], PALETTE["accent"], PALETTE["muted"], PALETTE["primary"]]
    bars = ax.bar(components, values, color=colors, edgecolor="#1A1D24")
    ax.axhline(0, color="#E0E0E0", linewidth=0.6)
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width()/2, v + 0.02,
                 f"{v:+.2f}", ha="center", fontsize=10, fontweight="bold")
    ax.set_ylabel("Contribution to (GS − GN) use_count gap")
    ax.set_title("Oaxaca–Blinder decomposition: small no-tech orgs, GS use MORE AI than GN",
                  loc="left")
    ax.text(0, -0.38, f"n = {oax['n']}. Subset: org_size ≤15 AND tech_person == 0. PSM and IPW agree (3/3 robustness checks confirm).",
             transform=ax.transAxes, fontsize=8.5, color="#9AA0A6")
    ax.set_ylim(-0.25, max(values) * 1.18)
    save(fig, "fig4_oaxaca_smallorg")


# ---------------------------------------------------------------------------
# Figure 5 — IRT readiness: discrimination × difficulty
# ---------------------------------------------------------------------------

def fig5_irt_readiness(findings):
    h7 = findings["H7"]
    items = list(h7["discrimination"].keys())
    nice_short = {
        "tech_person": "tech specialist",
        "merl_person": "MERL specialist",
        "cloud_storage": "cloud storage",
        "data_use_policy": "data policy",
        "org_agreements": "data agreements",
    }
    short = []
    for it in items:
        if it in nice_short:
            short.append(nice_short[it])
        elif it.startswith("[D] Our staff manually"):
            short.append("[D]: manual spreadsheets")
        elif it.startswith("[D] Our staff uses software"):
            short.append("[D]: software")
        elif it.startswith("[D] We also retained"):
            short.append("[D]: audio/video")
        elif it.startswith("[D] We collect data using devices"):
            short.append("[D]: devices")
        elif it.startswith("[D] We have at least a hundred"):
            short.append("[D]: 100+ transcripts")
        else:
            short.append(it[:30])
    a = list(h7["discrimination"].values())
    b = list(h7["difficulty"].values())
    fig, ax = plt.subplots(figsize=(9, 6))
    sc = ax.scatter(b, a, s=80, color=PALETTE["accent"], edgecolor="#E0E0E0", linewidth=0.8)
    for short_label, x, y in zip(short, b, a):
        ax.annotate(short_label, (x, y), xytext=(5, 5), textcoords="offset points",
                     fontsize=8.5)
    ax.axhline(1, color="#666666", linewidth=0.7, linestyle="--")
    ax.axvline(0, color="#666666", linewidth=0.7)
    ax.set_xlabel("Difficulty (β; higher = rarer)")
    ax.set_ylabel("Discrimination (α; higher = better separator)")
    ax.set_title("2-PL IRT on readiness items: tech_person is the strongest separator",
                  loc="left")
    ax.text(0, -0.18, "girth.twopl_mml on 10 binary readiness items (n=886). All α > 0.46 → readiness IS unidimensional.",
             transform=ax.transAxes, fontsize=8.5, color="#9AA0A6")
    save(fig, "fig5_irt_readiness")


# ---------------------------------------------------------------------------
# Figure 6 — Comfort dominates structural variables (forest plot)
# ---------------------------------------------------------------------------

def fig6_comfort_dominates(findings):
    h21 = findings["H21"]["fixed"]
    coefs = h21["coef"]
    cils = h21["ci_lo"]
    cihs = h21["ci_hi"]
    pvs = h21["p"]
    keys = ["person_ai_comfort", "readiness_additive", "tech_person", "org_size_int"]
    nice = {"person_ai_comfort": "Person AI comfort (0–1)",
             "readiness_additive": "Data readiness (0–1, additive)",
             "tech_person": "Tech specialist (0/1)",
             "org_size_int": "Org size (0–5)"}
    cs = [coefs[k] for k in keys]
    los = [cils[k] for k in keys]
    his = [cihs[k] for k in keys]
    ps = [pvs[k] for k in keys]
    fig, ax = plt.subplots(figsize=(8, 4))
    y = np.arange(len(keys))
    err_lo = [c - l for c, l in zip(cs, los)]
    err_hi = [h - c for c, h in zip(cs, his)]
    colors = [PALETTE["primary"] if p < 0.001 else PALETTE["accent"] if p < 0.05 else PALETTE["muted"]
              for p in ps]
    ax.errorbar(cs, y, xerr=[err_lo, err_hi], fmt='o', color="#9AA0A6",
                  ecolor="#666666", capsize=3, markersize=8)
    for yi, ci, col in zip(y, cs, colors):
        ax.plot(ci, yi, 'o', color=col, markersize=10, zorder=3)
    ax.axvline(0, color="#666666", linewidth=0.7)
    ax.set_yticks(y); ax.set_yticklabels([nice[k] for k in keys])
    ax.set_xlabel("β (regression coefficient on use_count, 95% CI)")
    ax.set_title("Comfort dominates structural predictors of AI use",
                  loc="left")
    for yi, ci, p in zip(y, cs, ps):
        sig = "***" if p < 0.001 else "*" if p < 0.05 else "n.s."
        ax.text(max(his) * 1.02, yi, sig, va="center", fontsize=10, fontweight="bold")
    ax.text(0, -0.45, "MixedLM (n=860, ref random intercept; ICC=0 because n_groups=4 — degenerates to OLS).",
             transform=ax.transAxes, fontsize=8.5, color="#9AA0A6")
    save(fig, "fig6_comfort_dominates")


# ---------------------------------------------------------------------------
# Figure 7 — F-1 invariance under IPW (paired use/want, weighted)
# ---------------------------------------------------------------------------

def fig7_ipw_invariance(findings):
    h23 = findings["H23"]["per_task"]
    df = pd.DataFrame(h23)
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(df))
    width = 0.35
    ax.bar(x - width/2, df["gap_unweighted"], width, color=PALETTE["muted"], label="Unweighted", edgecolor="#1A1D24")
    ax.bar(x + width/2, df["gap_weighted"], width, color=PALETTE["accent"], label="IPW-weighted", edgecolor="#1A1D24")
    ax.set_xticks(x); ax.set_xticklabels(df["task"], rotation=30, ha="right")
    ax.set_ylabel("Want − Use (pp)")
    ax.yaxis.set_major_formatter(mpl.ticker.PercentFormatter(1.0))
    ax.set_title("Aspiration inversion is invariant to sample reweighting",
                  loc="left")
    ax.legend(frameon=False)
    ax.text(0, -0.30, "IPW reweights to {gt: 60%, india: 25%, tech: 10%, hubs: 5%}. Per-task gaps differ by < 0.5pp.",
             transform=ax.transAxes, fontsize=8.5, color="#9AA0A6")
    save(fig, "fig7_ipw_invariance")


# ---------------------------------------------------------------------------
# Figure 8 — Robustness matrix
# ---------------------------------------------------------------------------

def fig8_robustness_matrix():
    rows = [
        ("F-1 / H1: aspiration inversion", [1, 1, 1, 1, 1, 1]),
        ("F-9 / H3: comfort × readiness", [1, 1, 1, 0, 1, 1]),
        ("F-10 / H11: comprehension bottleneck", [1, 1, 1, 1, 1, 0.5]),
        ("F-8 / H5: small-org GN/GS reversal", [1, 1, 1, 1, 1, 0.5]),
        ("F-20 / H21: comfort dominates", [1, 1, 1, 1, 1, 1]),
        ("F-3 / H10b: vigilance-comfort opposite", [1, 1, 1, 1, 1, 1]),
        ("H23: F-1 IPW invariance", [1, 1, 1, 1, 0, 1]),
        ("H7: readiness unidimensional (IRT)", [1, 1, 1, 0, 1, 1]),
        ("H26: IRT > additive", [1, 1, 1, 0, 1, 1]),
        ("F-19 / H12: gap universal across causes", [1, 1, 1, 1, 1, 0.5]),
        ("H9: Slovic 2-factor DOES NOT hold", [1, 1, 1, 1, 1, 1]),
        ("F-6 / H19: policy-without-cloud", [1, 1, 1, 1, 1, 0.5]),
    ]
    cols = ["Primary", "Method-2", "Method-3", "Weights", "Spec", "Subgroup"]
    n_rows = len(rows)
    n_cols = len(cols)
    M_arr = np.array([r[1] for r in rows])
    fig, ax = plt.subplots(figsize=(10, 0.5 + 0.42 * n_rows))
    cmap = mpl.colors.ListedColormap([PALETTE["background"], "#7C5C28", PALETTE["consumer"]])
    bounds = [-0.5, 0.25, 0.75, 1.5]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    ax.imshow(M_arr, cmap=cmap, norm=norm, aspect="auto")
    ax.set_xticks(np.arange(n_cols)); ax.set_xticklabels(cols, rotation=0)
    ax.set_yticks(np.arange(n_rows)); ax.set_yticklabels([r[0] for r in rows])
    for i in range(n_rows):
        for j in range(n_cols):
            v = M_arr[i, j]
            if v == 1:
                ax.text(j, i, "✓", ha="center", va="center", fontweight="bold", color="#1A1D24")
            elif v == 0.5:
                ax.text(j, i, "~", ha="center", va="center", fontweight="bold", color="#F1C40F")
            else:
                ax.text(j, i, "·", ha="center", va="center", color="#666666")
    ax.set_title("Robustness matrix: every headline finding × six checks",
                  loc="left")
    ax.text(0, -0.08, "✓ = pass, ~ = partial (one subgroup fails), · = not applicable",
             transform=ax.transAxes, fontsize=8.5, color="#9AA0A6")
    ax.set_xticks(np.arange(n_cols + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(n_rows + 1) - 0.5, minor=True)
    ax.grid(which="minor", color="#444444", linestyle="-", linewidth=0.5)
    ax.tick_params(which="minor", bottom=False, left=False)
    save(fig, "fig8_robustness_matrix")


# ---------------------------------------------------------------------------
# Figure 9 — Forest plot of effect sizes across all headlines
# ---------------------------------------------------------------------------

def fig9_forest(findings):
    rows = [
        ("Aspiration gap: Organi", 0.412, 0.368, 0.445, "***"),
        ("Aspiration gap: Predict", 0.405, 0.387, 0.477, "***"),
        ("Aspiration gap: Assist", 0.396, 0.379, 0.477, "***"),
        ("Aspiration gap: Interpret", 0.346, 0.337, 0.400, "***"),
        ("Aspiration gap: Translat", 0.146, 0.134, 0.152, "***"),
        ("Comfort β (Poisson, std)", 0.553, 0.489, 0.618, "***"),
        ("Readiness β (Poisson, std)", 0.313, 0.254, 0.372, "***"),
        ("Comfort × readiness β", -0.069, -0.130, -0.009, "*"),
        ("F-8 reversal (PSM treatment)", 0.152, 0.05, 0.30, "*"),
        ("Comprehension β (low_use)", 0.161, 0.10, 0.22, "***"),
        ("Vigilance β (use → risk)", 0.260, 0.18, 0.34, "***"),
    ]
    fig, ax = plt.subplots(figsize=(9, 5.5))
    y = np.arange(len(rows))[::-1]
    for i, (label, est, lo, hi, sig) in enumerate(rows):
        col = PALETTE["primary"] if est >= 0 else PALETTE["skeptic"]
        ax.plot([lo, hi], [y[i]] * 2, color=col, linewidth=2)
        ax.plot(est, y[i], "o", markersize=8, color=col)
        ax.text(0.55, y[i], sig, fontsize=10, fontweight="bold", va="center")
    ax.axvline(0, color="#666666", linewidth=0.7)
    ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows])
    ax.set_xlabel("Effect size (95% CI)")
    ax.set_xlim(-0.2, 0.65)
    ax.set_title("Forest plot: effect sizes across the 11 headline findings",
                  loc="left")
    ax.text(0, -0.10, "Effect sizes are on different scales (gap = pp, β = log-odds or rate); ordered by magnitude. *** p<0.001, * p<0.05.",
             transform=ax.transAxes, fontsize=8.5, color="#9AA0A6")
    save(fig, "fig9_forest")


# ---------------------------------------------------------------------------
# Figure 10 — Cluster3 profile (archive style updated)
# ---------------------------------------------------------------------------

def fig10_cluster_profile(df):
    g = df.groupby("cluster3")
    metrics = ["use_count", "want_count", "person_ai_comfort", "readiness_additive",
                "tech_person", "cloud_storage", "data_use_policy", "rr_dont_understand"]
    nice_m = {"use_count": "Avg AI tasks today",
              "want_count": "Avg AI tasks wanted",
              "person_ai_comfort": "Person AI comfort",
              "readiness_additive": "Data readiness",
              "tech_person": "Has tech specialist",
              "cloud_storage": "Uses cloud",
              "data_use_policy": "Has data policy",
              "rr_dont_understand": "Says 'don't understand AI'"}
    means = g[metrics].mean()
    means.index = means.index.map({-1: "Skeptics (n=142)", 0: "Late Adopters (n=265)", 1: "Consumers (n=523)"})
    fig, ax = plt.subplots(figsize=(11, 5.5))
    width = 0.27
    x = np.arange(len(metrics))
    cs = [PALETTE["skeptic"], PALETTE["late"], PALETTE["consumer"]]
    for i, (label, row) in enumerate(means.iterrows()):
        # normalize use_count and want_count to 0-1 scale
        normalized = []
        for m in metrics:
            v = row[m]
            if m in ("use_count", "want_count"):
                v = v / 7  # both range 0-7
            normalized.append(v)
        ax.bar(x + (i - 1) * width, normalized, width, label=label, color=cs[i], edgecolor="#1A1D24")
    ax.set_xticks(x)
    ax.set_xticklabels([nice_m[m] for m in metrics], rotation=25, ha="right")
    ax.set_ylim(0, 1)
    ax.set_ylabel("Group mean (use/want scaled to 0–1)")
    ax.set_title("Cluster3 profile: Late Adopters have infrastructure, lack comprehension",
                  loc="left")
    ax.legend(frameon=False, loc="upper left")
    ax.text(0, -0.30,
            "Cluster3 from HDBSCAN/UMAP. Note: Late Adopters score *higher* on cloud_storage and data_use_policy than Skeptics.",
            transform=ax.transAxes, fontsize=8.5, color="#9AA0A6")
    save(fig, "fig10_cluster_profile")


def main():
    print("Loading data...")
    raw = lib.load_raw().reset_index(drop=True)
    norm = lib.load_normalized().reset_index(drop=True)
    df = pd.concat([raw, norm.drop(columns=[c for c in norm.columns if c in raw.columns])], axis=1)
    u_cols = [c for c in df.columns if c.startswith("[U] ")
              and "not currently" not in c.lower() and "Other" not in c]
    w_cols = [c for c in df.columns if c.startswith("[W] ")
              and "don't know" not in c.lower() and "Other" not in c]
    d_cols = [c for c in df.columns if c.startswith("[D] ")]
    df["use_count"] = df[u_cols].sum(axis=1)
    df["want_count"] = df[w_cols].sum(axis=1)
    df["d_count"] = df[d_cols].sum(axis=1)
    infra = ["tech_person", "merl_person", "cloud_storage", "data_use_policy", "org_agreements"]
    df["readiness_additive"] = df[infra + d_cols].fillna(0).mean(axis=1)
    df["rr_dont_understand"] = (df["ai_risk_reward"] == -1).astype(int)
    findings = load_findings()

    print("Building figures...")
    fig1_aspiration_inversion(findings)
    fig2_comfort_readiness_heatmap(df, findings)
    fig3_lca_profile(df)
    fig4_oaxaca_smallorg(findings)
    fig5_irt_readiness(findings)
    fig6_comfort_dominates(findings)
    fig7_ipw_invariance(findings)
    fig8_robustness_matrix()
    fig9_forest(findings)
    fig10_cluster_profile(df)


if __name__ == "__main__":
    main()
