"""Phase 5 — produce all final figures into ../figures/ as PNG + SVG."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analysis import lib

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"
FIG_DIR.mkdir(exist_ok=True)

INK = "#1a1a1a"
MUTED = "#6b7280"
GRID = "#e5e7eb"
USE = "#9aa3b0"
WANT = "#1f6feb"
GAP = "#f97316"
CONSUMER = "#1f6feb"
LATE = "#f59e0b"
SKEPTIC = "#9333ea"
GN = "#0f766e"
GS = "#dc2626"

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "axes.axisbelow": True,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.frameon": False,
    "legend.fontsize": 9,
})


def save(fig, name: str) -> None:
    for ext in ("png", "svg"):
        fig.savefig(FIG_DIR / f"{name}.{ext}", dpi=200)
    plt.close(fig)
    print(f"  wrote figures/{name}.{{png,svg}}")


def add_title(fig, title, subtitle=None, x=0.04, y_title=0.94, y_sub=0.895):
    fig.text(x, y_title, title, fontsize=14, fontweight="bold", color=INK, ha="left", va="bottom")
    if subtitle:
        fig.text(x, y_sub, subtitle, fontsize=10, color=MUTED, ha="left", va="top")


def add_footer(fig, text, x=0.04, y=0.04):
    fig.text(x, y, text, fontsize=8.5, color=MUTED, ha="left", va="bottom")


TASK_LABELS = {
    "Organi": "Organize information",
    "Predict": "Predict outcomes",
    "Assist": "Assist / automate",
    "Interpret": "Interpret data",
    "Translat": "Translate / transcribe",
    "Ask": "Ask a chatbot",
    "Generat": "Generate content",
}


# === 01 — Aspiration gap ======================================================

def fig_aspiration_gap(j: pd.DataFrame) -> None:
    tasks = ["Organi", "Predict", "Assist", "Interpret", "Translat", "Ask", "Generat"]
    rows = []
    for t in tasks:
        u = j[f"[U] {t}"].mean() * 100
        w = j[f"[W] {t}"].mean() * 100
        rows.append((TASK_LABELS[t], u, w, w - u))
    df = pd.DataFrame(rows, columns=["task", "use", "want", "gap"])

    fig = plt.figure(figsize=(11, 6.6))
    fig.subplots_adjust(left=0.18, right=0.96, top=0.78, bottom=0.13)
    ax = fig.add_subplot(111)
    y = np.arange(len(df))
    h = 0.34

    ax.barh(y - h / 2, df["use"], h, color=USE, label="Doing today", zorder=2)
    ax.barh(y + h / 2, df["want"], h, color=WANT, label="Want to do", zorder=2)

    for i, row in df.iterrows():
        ax.text(row["use"] + 1, i - h / 2, f"{row['use']:.0f}%", va="center", fontsize=9, color=INK)
        ax.text(row["want"] + 1, i + h / 2, f"{row['want']:.0f}%", va="center", fontsize=9, color=INK, fontweight="bold")
        if abs(row["gap"]) >= 30:
            ax.text(row["want"] + 9, i + h / 2, f"+{row['gap']:.0f} pp",
                    fontsize=10.5, color=GAP, fontweight="bold", va="center")

    ax.set_yticks(y, df["task"], fontsize=10)
    ax.invert_yaxis()
    ax.set_xlim(0, 88)
    ax.set_xlabel("Share of nonprofits (%)")
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.0))

    add_title(fig,
              "Nonprofits use AI to write. They want it to think.",
              "Today's AI use is dominated by content generation. The next wave nonprofits aspire to —\n"
              "predicting, organizing, interpreting their own data — is barely off the ground.")
    add_footer(fig, "Source: GivingTuesday 2024 AI Readiness Survey (n=930). All four large gaps are paired-McNemar p < 1×10⁻⁵⁸.")
    save(fig, "01_aspiration_gap")


# === 02 — Generate sign-flip ==================================================

def fig_generate_signflip(j: pd.DataFrame) -> None:
    clusters = [(-1, "AI Skeptics", 142), (0, "Late Adopters", 265), (1, "Heavy Users", 523)]
    use_vals, want_vals = [], []
    for cl, _, _ in clusters:
        sub = j[j["cluster3"] == cl]
        use_vals.append(sub["[U] Generat"].mean() * 100)
        want_vals.append(sub["[W] Generat"].mean() * 100)

    fig = plt.figure(figsize=(10, 6.4))
    fig.subplots_adjust(left=0.10, right=0.96, top=0.78, bottom=0.18)
    ax = fig.add_subplot(111)
    x = np.arange(len(clusters))
    w = 0.36

    ax.bar(x - w / 2, use_vals, w, color=USE, label="Use 'Generate content' today", zorder=2)
    ax.bar(x + w / 2, want_vals, w, color=WANT, label="Want 'Generate content'", zorder=2)

    for i, (cl, name, n) in enumerate(clusters):
        u, wv = use_vals[i], want_vals[i]
        ax.text(i - w / 2, u + 1.5, f"{u:.0f}%", ha="center", fontsize=10)
        ax.text(i + w / 2, wv + 1.5, f"{wv:.0f}%", ha="center", fontsize=10, fontweight="bold")
        gap = wv - u
        gap_color = GAP if gap > 0 else "#16a34a"
        ax.text(i, max(u, wv) + 9, f"{gap:+.0f} pp",
                fontsize=12, fontweight="bold", color=gap_color, ha="center")

    ax.set_xticks(x, [f"{name}\n(n = {n})" for _, name, n in clusters], fontsize=10)
    ax.set_ylim(0, 110)
    ax.set_ylabel("Share of cluster (%)")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 1.0))

    add_title(fig,
              "Heavy users have moved past generative AI. Late Adopters are still chasing it.",
              "Generative-content tools are the only AI task where the heaviest users have flipped the gap negative —\n"
              "84% use it but just 69% still want it. Late Adopters, by contrast, want it ten times more than they use it.")
    add_footer(fig, "Of the 265 “Late Adopters,” only 3% use a generative tool today, while 40% want to.")
    save(fig, "02_generate_signflip")


# === 03 — Comfort × infrastructure 2×2 ========================================

def fig_comfort_infra_2x2(j: pd.DataFrame) -> None:
    sub = j.dropna(subset=["readiness", "person_ai_comfort", "use_count"]).copy()
    med_r = sub["readiness"].median()
    med_c = sub["person_ai_comfort"].median()
    sub["hi_infra"] = (sub["readiness"] > med_r).astype(int)
    sub["hi_comfort"] = (sub["person_ai_comfort"] > med_c).astype(int)
    grid = sub.groupby(["hi_infra", "hi_comfort"]).agg(n=("use_count", "size"), use=("use_count", "mean")).reset_index()

    mat = np.zeros((2, 2))
    nmat = np.zeros((2, 2), dtype=int)
    for _, r in grid.iterrows():
        mat[int(r["hi_infra"]), int(r["hi_comfort"])] = r["use"]
        nmat[int(r["hi_infra"]), int(r["hi_comfort"])] = int(r["n"])

    fig = plt.figure(figsize=(13, 7.4))
    fig.subplots_adjust(left=0.30, right=0.70, top=0.80, bottom=0.13)
    ax = fig.add_subplot(111)

    ax.imshow(mat, cmap="Blues", vmin=0, vmax=mat.max() * 1.05, aspect="auto", extent=[-0.5, 1.5, 1.5, -0.5])
    for i in range(2):
        for j_ in range(2):
            color = "white" if mat[i, j_] > mat.max() * 0.55 else INK
            ax.text(j_, i - 0.05, f"{mat[i, j_]:.2f}", ha="center", va="center",
                    fontsize=28, fontweight="bold", color=color)
            ax.text(j_, i + 0.20, "AI tasks used", ha="center", va="center", fontsize=8.5, color=color)
            ax.text(j_, i + 0.30, f"n = {nmat[i, j_]}", ha="center", va="center", fontsize=9, color=color)

    ax.set_xticks([0, 1], ["Low comfort\n(score ≤ 0.70)", "High comfort\n(score > 0.70)"], fontsize=10)
    ax.set_yticks([0, 1], ["Low infrastructure\n(readiness ≤ 0.40)", "High infrastructure\n(readiness > 0.40)"], fontsize=10)
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(1.5, -0.5)
    ax.set_xlabel("Personal AI comfort", fontsize=11, fontweight="bold")
    ax.set_ylabel("Organizational data readiness", fontsize=11, fontweight="bold")
    ax.grid(False)

    # Side annotations in the wide right margin
    fig.text(0.71, 0.65,
             "Stranded infrastructure",
             fontsize=11, color="#dc2626", ha="left", va="top", fontweight="bold")
    fig.text(0.71, 0.62,
             "216 orgs have the data plumbing\n"
             "but low-comfort people — and use\n"
             "just 1.65 AI tasks on average.",
             fontsize=9.5, color=INK, ha="left", va="top")
    fig.text(0.71, 0.42,
             "Riding consumer LLMs",
             fontsize=11, color="#0f766e", ha="left", va="top", fontweight="bold")
    fig.text(0.71, 0.39,
             "170 orgs have no infrastructure but\n"
             "high comfort gets them to 2.05 —\n"
             "more than the 216 low-comfort,\n"
             "high-infrastructure peers below.",
             fontsize=9.5, color=INK, ha="left", va="top")

    add_title(fig,
              "Both keys matter — but comfort is the more powerful one.",
              "Mean number of AI tasks used (out of 7), split by median data readiness × median personal AI comfort.")
    add_footer(fig, "n=908 (excluding rows missing comfort or readiness inputs). Going from low- to high-comfort roughly doubles use within each infrastructure tier.")
    save(fig, "03_comfort_infra_2x2")


# === 04 — Late Adopter Paradox ================================================

def fig_late_adopter_paradox(j: pd.DataFrame) -> None:
    clusters = [(-1, "AI Skeptics", SKEPTIC, 142),
                (0, "Late Adopters", LATE, 265),
                (1, "Heavy Users", CONSUMER, 523)]
    metrics = [
        ("cloud_storage", "Cloud storage"),
        ("data_use_policy", "Data-use policy"),
        ("tech_person", "Tech specialist"),
        ("person_ai_comfort", "AI comfort"),
        ("dont_understand", "“Don't understand AI”"),
        ("zero_use", "Use zero AI tasks"),
    ]
    j = j.copy()
    j["dont_understand"] = (j["ai_risk_reward"] == -1).astype(int)
    j["zero_use"] = (j["use_count"] == 0).astype(int)

    fig = plt.figure(figsize=(13, 7.6))
    fig.subplots_adjust(left=0.07, right=0.97, top=0.74, bottom=0.18)
    ax = fig.add_subplot(111)
    x = np.arange(len(metrics))
    w = 0.26

    for i, (cl, name, color, n) in enumerate(clusters):
        sub = j[j["cluster3"] == cl]
        vals = [sub[m].mean() for m, _ in metrics]
        bars = ax.bar(x + (i - 1) * w, vals, w, color=color, label=f"{name} (n = {n})", zorder=2)
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.012, f"{v*100:.0f}%",
                    ha="center", fontsize=8.5, color=INK)

    ax.set_xticks(x, [lbl for _, lbl in metrics], fontsize=10)
    ax.set_ylim(0, 1.20)
    ax.yaxis.set_major_formatter(mpl.ticker.PercentFormatter(1.0))
    ax.set_ylabel("Share of cluster")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.06), ncol=3)

    # Section banding via text labels above legend
    ax.axvspan(-0.5, 2.5, alpha=0.04, color=INK, zorder=0)
    ax.axvspan(2.5, 5.5, alpha=0.06, color=GAP, zorder=0)
    ax.text(1.0, 1.16, "Have the infrastructure", ha="center", fontsize=10, color=MUTED, style="italic")
    ax.text(4.0, 1.16, "Lack the comprehension and confidence", ha="center", fontsize=10, color=GAP, style="italic", fontweight="bold")

    add_title(fig,
              "Late Adopters have the plumbing. They don't have the people-side readiness.",
              "Six measures across the three clusters. Late Adopters match Heavy Users on cloud and policy —\n"
              "and look nothing like them on comfort and comprehension.")
    add_footer(fig, "Of 265 Late Adopters, 90% use zero AI tasks today and 53% answer “I don't understand AI enough to have a clear view.”\n"
                    "In a logistic regression of cluster membership, comfort and comprehension are the only significant predictors — infrastructure variables are not.")
    save(fig, "04_late_adopter_paradox")


# === 05 — Divide reversal =====================================================

def fig_divide_reversal(j: pd.DataFrame) -> None:
    sub = j.dropna(subset=["use_count", "global_north_south", "org_size_int", "tech_person"]).copy()
    sub["small"] = (sub["org_size_int"] <= 1).astype(int)
    cells = []
    for s in [0, 1]:
        for sm in [0, 1]:
            for t in [0, 1]:
                cell = sub[(sub["global_north_south"].eq("S").astype(int) == s) & (sub["small"] == sm) & (sub["tech_person"] == t)]
                cells.append({
                    "is_S": s, "small": sm, "has_tech": int(t), "n": len(cell),
                    "mean_use": cell["use_count"].mean() if len(cell) else np.nan,
                })
    df = pd.DataFrame(cells)

    fig = plt.figure(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.80, bottom=0.20, wspace=0.18)
    axes = [fig.add_subplot(1, 2, i) for i in (1, 2)]
    titles = ["Small organizations (≤ 15 staff)", "Larger organizations (> 15 staff)"]

    for ax, sm, title in zip(axes, [1, 0], titles):
        gn = df[(df["is_S"] == 0) & (df["small"] == sm)].sort_values("has_tech")
        gs = df[(df["is_S"] == 1) & (df["small"] == sm)].sort_values("has_tech")
        x = np.arange(2)
        w = 0.36
        ax.bar(x - w/2, gn["mean_use"], w, color=GN, label="Global North", zorder=2)
        ax.bar(x + w/2, gs["mean_use"], w, color=GS, label="Global South", zorder=2)
        for xi, (g, gv) in enumerate(zip(gn["mean_use"], gs["mean_use"])):
            ax.text(xi - w/2, g + 0.07, f"{g:.2f}", ha="center", fontsize=9.5, color=INK)
            ax.text(xi + w/2, gv + 0.07, f"{gv:.2f}", ha="center", fontsize=9.5, color=INK)
        ns_gn = gn["n"].tolist(); ns_gs = gs["n"].tolist()
        for xi, (a, b) in enumerate(zip(ns_gn, ns_gs)):
            ax.text(xi - w/2, -0.30, f"n={a}", ha="center", fontsize=8, color=MUTED)
            ax.text(xi + w/2, -0.30, f"n={b}", ha="center", fontsize=8, color=MUTED)
        ax.set_xticks(x, ["No tech specialist", "Has tech specialist"], fontsize=10)
        ax.set_title(title, fontsize=11, fontweight="bold", loc="left", color=INK, pad=8)
        ax.set_ylim(-0.05, 3.4)

    axes[0].set_ylabel("Mean number of AI tasks used")
    axes[0].legend(loc="upper left")
    axes[0].annotate(
        "Reversal: Global South\nuses more AI than Global\nNorth among small orgs\nwithout a tech specialist.",
        xy=(0 + 0.18, 1.59), xytext=(-0.4, 2.6),
        fontsize=9.5, color=GS, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=GS, lw=1.4),
    )

    add_title(fig,
              "The digital divide reverses where AI matters most: small, under-resourced organizations.",
              "Mean AI tasks used today, by region × organization size × whether the org has a tech specialist.")
    add_footer(fig,
               "Among small Global South orgs without a tech specialist, mean AI use (1.59) actually exceeds the comparable Global North group (1.15);\n"
               "the is_S × small interaction is significant in a Poisson model (p = 0.024). Likely mechanism: consumer LLMs require no organizational\n"
               "infrastructure, so the resource gap that historically widened with each tech wave does not bind on this one.")
    save(fig, "05_divide_reversal")


# === 06 — Re-derived 3-tier typology ==========================================

def fig_typology_redrawn(j: pd.DataFrame) -> None:
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    feat_cols = [c for c in j.columns if c.startswith("[U] ") or c.startswith("[W] ")]
    feat_cols += ["readiness", "person_ai_comfort"]
    X = j[feat_cols].fillna(0).values
    Xs = StandardScaler().fit_transform(X)
    km = KMeans(n_clusters=3, random_state=0, n_init=10).fit(Xs)
    j = j.copy()
    j["my_cluster"] = km.labels_

    profile = j.groupby("my_cluster")[["use_count", "want_count"]].mean()
    pu = profile["use_count"].idxmax()
    ds = profile["want_count"].idxmin()
    asp = [c for c in profile.index if c not in (pu, ds)][0]
    cluster_meta = {pu: "Power Users", asp: "Aspirationals", ds: "Disengaged"}
    counts = j["my_cluster"].value_counts().to_dict()

    fig = plt.figure(figsize=(13, 6.8))
    fig.subplots_adjust(left=0.06, right=0.96, top=0.78, bottom=0.18, wspace=0.30)
    ax_l = fig.add_subplot(1, 2, 1)
    ax_r = fig.add_subplot(1, 2, 2)

    order = [pu, asp, ds]
    use_vals = [j.loc[j.my_cluster == c, "use_count"].mean() for c in order]
    want_vals = [j.loc[j.my_cluster == c, "want_count"].mean() for c in order]
    x = np.arange(3)
    w = 0.36
    ax_l.bar(x - w/2, use_vals, w, color=USE, label="AI tasks used today")
    ax_l.bar(x + w/2, want_vals, w, color=WANT, label="AI tasks wanted")
    for i, c in enumerate(order):
        ax_l.text(i - w/2, use_vals[i] + 0.15, f"{use_vals[i]:.1f}", ha="center", fontsize=10)
        ax_l.text(i + w/2, want_vals[i] + 0.15, f"{want_vals[i]:.1f}", ha="center", fontsize=10, fontweight="bold")
    ax_l.set_xticks(x, [f"{cluster_meta[c]}\n(n = {counts[c]}, {counts[c]/930*100:.0f}%)" for c in order], fontsize=10)
    ax_l.set_ylim(0, 7.5)
    ax_l.set_ylabel("Mean count of AI tasks (max 7)")
    ax_l.set_title("Three tiers of nonprofit AI engagement", fontsize=11, fontweight="bold", loc="left", pad=8)
    ax_l.legend(loc="upper right")

    ct = pd.crosstab(j["my_cluster"], j["cluster3"])
    ct = ct.reindex(order)
    ct.columns = ["Skeptics (-1)", "Late Adopters (0)", "Consumers (+1)"]
    ct.index = [cluster_meta[c] for c in order]
    ax_r.imshow(ct.values, cmap="Blues", aspect="auto")
    for i in range(ct.shape[0]):
        for k in range(ct.shape[1]):
            v = ct.values[i, k]
            color = "white" if v > ct.values.max() * 0.55 else INK
            ax_r.text(k, i, str(v), ha="center", va="center", fontsize=12, fontweight="bold", color=color)
    ax_r.set_xticks(range(ct.shape[1]), ct.columns, fontsize=9.5)
    ax_r.set_yticks(range(ct.shape[0]), ct.index, fontsize=10)
    ax_r.set_xlabel("Official cluster3 label")
    ax_r.set_title("Where each tier hides in the published clusters", fontsize=11, fontweight="bold", loc="left", pad=8)
    ax_r.grid(False)

    add_title(fig,
              "The actionable middle: a 444-org Aspirationals tier the official labels miss.",
              "Re-clustering on AI use, want, comfort, and readiness yields three crisp tiers — and reveals a giant\n"
              "Aspirationals group that the published labels split between “Late Adopters” and “Consumers.”")
    add_footer(fig,
               "Aspirationals already use ~1.8 AI tasks and want ~5.0 — they are this dataset's clearest target for capacity-building.\n"
               "Method: K-means (k=3) on the 16 [U]/[W] one-hots plus standardized comfort and readiness; ARI vs cluster3 = 0.17.")
    save(fig, "06_typology_redrawn")


def main() -> None:
    j = lib.load_joined()
    j["use_count"] = lib.ai_use_count(j)
    j["want_count"] = lib.ai_want_count(j)
    j["readiness"] = lib.data_readiness_score(j)

    print(f"Writing figures to {FIG_DIR}")
    fig_aspiration_gap(j)
    fig_generate_signflip(j)
    fig_comfort_infra_2x2(j)
    fig_late_adopter_paradox(j)
    fig_divide_reversal(j)
    fig_typology_redrawn(j)
    print("Done.")


if __name__ == "__main__":
    main()
