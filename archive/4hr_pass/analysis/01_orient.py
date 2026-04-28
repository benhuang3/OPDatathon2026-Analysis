"""Phase 1 — Orient.

Loads both parquet files, verifies shapes against the data dictionary, computes
baseline distributions and a missingness table, and writes the results into
`analysis/00_orientation.md`.

Usage:
    python -m analysis.01_orient
"""

from __future__ import annotations

from analysis.lib import load_normalized, load_raw


def main() -> None:
    raw = load_raw()
    norm = load_normalized()

    assert len(raw) == 930, f"expected 930 raw rows, got {len(raw)}"
    print(f"raw:        {raw.shape}")
    print(f"normalized: {norm.shape}")

    # TODO: marginal frequencies for every categorical column
    # TODO: mean / median / IQR for every numeric column
    # TODO: missingness rate per column, sorted descending
    # TODO: verify cluster3 / cluster2 distributions match the dictionary
    # TODO: write results into analysis/00_orientation.md


if __name__ == "__main__":
    main()
