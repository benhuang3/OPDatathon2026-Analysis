"""Smoke tests for analysis/methods.py — small synthetic examples confirming
that each helper returns the right shape on data we can reason about.
Run with: `python -m pytest analysis/tests/test_methods.py -q` or
`python analysis/tests/test_methods.py`.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import methods  # noqa: E402


def synthetic_lca_data(seed: int = 0, n: int = 600) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    items = [f"item_{i}" for i in range(8)]
    classes = rng.choice([0, 1, 2], size=n, p=[0.4, 0.4, 0.2])
    probs = np.array([
        [0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2],   # class 0: low
        [0.7, 0.7, 0.7, 0.7, 0.3, 0.3, 0.3, 0.3],   # class 1: split
        [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],   # class 2: all-yes
    ])
    rows = []
    for c in classes:
        rows.append((rng.random(len(items)) < probs[c]).astype(int))
    df = pd.DataFrame(rows, columns=items)
    return df


def test_lca():
    df = synthetic_lca_data()
    res = methods.latent_class_model(df, df.columns.tolist(), k_range=(2, 3, 4), n_init=2)
    assert res.best_k in (2, 3, 4)
    assert res.posteriors.shape[0] == len(df)
    assert res.fit_table.loc[res.best_k, "bic"] == res.fit_table["bic"].min()
    print(f"  LCA: best_k={res.best_k}, BIC={res.fit_table['bic'].min():.1f}, classes={dict(res.fit_table.loc[res.best_k, 'n_per_class'])}")


def test_irt_2pl():
    df = synthetic_lca_data()
    res = methods.irt_score(df, df.columns.tolist(), model="2pl")
    assert len(res.discrimination) == len(df.columns)
    assert len(res.person_scores) == len(df)
    print(f"  IRT 2PL: alpha range=[{res.discrimination.min():.2f}, {res.discrimination.max():.2f}], theta range=[{res.person_scores.min():.2f}, {res.person_scores.max():.2f}]")


def test_oaxaca():
    rng = np.random.default_rng(1)
    n = 500
    g = rng.choice([0, 1], size=n)
    x1 = rng.normal(loc=g * 0.5, size=n)  # endowment differs
    x2 = rng.normal(size=n)
    y = 1.0 * x1 + 0.5 * x2 + 0.3 * g + rng.normal(scale=0.5, size=n)
    df = pd.DataFrame({"y": y, "g": g, "x1": x1, "x2": x2})
    res = methods.oaxaca_decompose(df, "y", "g", ["x1", "x2"])
    assert abs(res.endowments + res.coefficients + res.interaction - res.raw_gap) < 1e-6
    print(f"  Oaxaca: gap={res.raw_gap:.3f}; E={res.endowments:.3f}, C={res.coefficients:.3f}, I={res.interaction:.3f}")


def test_sem():
    rng = np.random.default_rng(2)
    n = 400
    x = rng.normal(size=n)
    m = 0.6 * x + rng.normal(scale=0.5, size=n)
    y = 0.4 * x + 0.5 * m + rng.normal(scale=0.5, size=n)
    df = pd.DataFrame({"x": x, "m": m, "y": y})
    res = methods.sem_fit(df, "y ~ x + m\nm ~ x")
    assert res.coefficients is not None
    print(f"  SEM: n_paths={len(res.coefficients)}, fit_keys={list(res.fit_indices)[:5]}")


def test_ipw():
    df = pd.DataFrame({"ref": ["a"] * 600 + ["b"] * 200 + ["c"] * 100})
    bench = {"a": 0.5, "b": 0.3, "c": 0.2}
    res = methods.ipw_reweight(df, bench, "ref")
    assert abs(res.weights.sum() - len(df)) < 1e-3
    print(f"  IPW: effective_n={res.effective_n:.1f}, weight range=[{res.weights.min():.3f}, {res.weights.max():.3f}]")


def test_multilevel():
    rng = np.random.default_rng(3)
    n = 800
    grp = rng.choice(["A", "B", "C", "D"], size=n)
    grp_intercept = {"A": 0.0, "B": 0.5, "C": -0.3, "D": 0.2}
    x = rng.normal(size=n)
    y = np.array([grp_intercept[g] for g in grp]) + 0.5 * x + rng.normal(scale=0.3, size=n)
    df = pd.DataFrame({"y": y, "x": x, "grp": grp})
    res = methods.multilevel_model(df, "y ~ x", group_col="grp")
    assert res.icc > 0
    print(f"  Multilevel: ICC={res.icc:.3f}, fixed effects={list(res.fixed_effects.index)}")


def test_mediation():
    rng = np.random.default_rng(4)
    n = 500
    x = rng.normal(size=n)
    m = 0.6 * x + rng.normal(scale=0.5, size=n)
    y = 0.3 * x + 0.5 * m + rng.normal(scale=0.5, size=n)
    df = pd.DataFrame({"x": x, "m": m, "y": y})
    res = methods.mediation_full(df, "x", "m", "y", n_boot=300)
    assert res.indirect > 0
    print(f"  Mediation: indirect={res.indirect:.3f} CI [{res.indirect_ci[0]:.3f}, {res.indirect_ci[1]:.3f}], pm={res.proportion_mediated:.3f}")


def test_mca_louvain():
    rng = np.random.default_rng(5)
    n = 300
    # two clusters of items
    block1 = (rng.random((n, 4)) < 0.5).astype(int)
    block2 = (rng.random((n, 4)) < 0.5).astype(int)
    # make blocks correlated within
    corr_factor = (rng.random(n) < 0.6).astype(int).reshape(-1, 1)
    block1 = ((block1 + corr_factor * 0.5) > 0.5).astype(int)
    df = pd.DataFrame(np.hstack([block1, block2]),
                      columns=[f"a{i}" for i in range(4)] + [f"b{i}" for i in range(4)])
    res = methods.mca_louvain(df, df.columns.tolist())
    assert len(res.item_communities) == 8
    print(f"  MCA + Louvain: {res.item_communities.value_counts().to_dict()}")


def main():
    print("Running smoke tests for methods.py")
    print("-" * 60)
    test_lca()
    test_irt_2pl()
    test_oaxaca()
    test_sem()
    test_ipw()
    test_multilevel()
    test_mediation()
    test_mca_louvain()
    print("-" * 60)
    print("All smoke tests passed.")


if __name__ == "__main__":
    main()
