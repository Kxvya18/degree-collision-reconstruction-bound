# Degree-Collision Reconstruction Bound for Preferential-Attachment Networks

A research-oriented Python project for studying how much hidden growth history can be recovered from a final preferential-attachment network snapshot. The project focuses on degree collisions: situations where multiple nodes have identical or nearly identical degree information, making their arrival order difficult or impossible to reconstruct reliably.

The repository includes simulation code, reconstruction experiments, validation workflows, finite-size checks, condensed-regime analysis, and saved result artifacts. It is designed as a reproducible scientific-computing project for network science, graph-based learning, and mathematical modeling.

## Project Overview

Preferential-attachment models are commonly used to describe growing networks where high-degree nodes are more likely to attract new connections. In many practical settings, however, the full growth process is not observed. Only the final graph is available.

This project asks a reconstruction question:

> Given only the final network, how accurately can the historical node arrival order be inferred?

The central idea is that degree collisions create a fundamental ambiguity. If several nodes have the same or similar degree signatures, a reconstruction method may not be able to distinguish their relative arrival order from the final snapshot alone. The code explores this limitation through simulations, reconstruction pipelines, collision probability measurements, and validation plots.

## What This Project Demonstrates

- Preferential-attachment network simulation
- Historical reconstruction from static graph snapshots
- Degree-collision probability analysis
- Recoverability-bound validation
- Attachment-exponent beta experiments
- Collision trends across tau-style reconstruction diagnostics
- Finite-size scaling studies
- Condensed-regime behavior in preferential-attachment networks
- Reproducible scientific Python workflows
- Figure and table generation for network-science experiments

## Repository Structure

```text
.
├── ba_inference.py
├── run_reconstruction_paper_figures.py
├── requirements.txt
├── src/
│   ├── ba_inference.py
│   ├── condensed_regime_analysis.py
│   └── condensed_regime_analysis_fast.py
├── shared/
│   └── ba_experiments_full.py
├── validation/
│   ├── recoverability_validation.py
│   ├── figure1_bound_validation.py
│   ├── figure2_collision_beta.py
│   ├── figure3_collision_tau.py
│   ├── figure4_heatmap.py
│   ├── statistics.py
│   ├── utils.py
│   └── plot_style.py
└── outputs/
    ├── main/
    ├── validation_figures/
    ├── condensed_regime_analysis/
    ├── condensed_regime_analysis_fast/
    └── extended/
```

## Main Components

| Component | Purpose |
|---|---|
| `ba_inference.py` | Core preferential-attachment inference and reconstruction utilities |
| `src/ba_inference.py` | Source-organized version of the main inference code |
| `run_reconstruction_paper_figures.py` | Main reconstruction and figure-generation pipeline |
| `shared/ba_experiments_full.py` | Extended experiment utilities used by the reconstruction workflow |
| `validation/recoverability_validation.py` | Validation workflow for reconstruction bounds and collision trends |
| `validation/figure*.py` | Scripts for generating individual validation figures |
| `validation/statistics.py` | Statistical summaries used in validation analysis |
| `validation/utils.py` | Shared validation helpers |
| `outputs/` | Saved figures, tables, and result artifacts |

## Setup

Create and activate a virtual environment if preferred:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

The project uses standard scientific Python packages for numerical computation, graph simulation, plotting, and tabular result handling.

## Reproducing Main Results

Run the main reconstruction pipeline:

```bash
python run_reconstruction_paper_figures.py
```

Run the validation workflow:

```bash
python validation/recoverability_validation.py
```

Run individual validation figures when needed:

```bash
python validation/figure1_bound_validation.py
python validation/figure2_collision_beta.py
python validation/figure3_collision_tau.py
python validation/figure4_heatmap.py
```

Generated files are written under `outputs/` or the corresponding validation output directory.

## Important Output Files

| File or Folder | Description |
|---|---|
| `outputs/main/fig3_reconstruction.png` | Reconstruction behavior and accuracy trends |
| `outputs/main/fig5_unified.png` | Unified reconstruction and collision summary |
| `outputs/main/table_finite_size_scaling.csv` | Finite-size scaling results |
| `outputs/main/step5_unified_v12.csv` | Unified grid of reconstruction and collision measurements |
| `outputs/validation_figures/Figure1_BoundValidation.png` | Recoverability-bound validation figure |
| `outputs/validation_figures/Figure2_CollisionVsBeta.png` | Collision probability versus attachment exponent beta |
| `outputs/validation_figures/Figure3_CollisionVsTau.png` | Collision probability versus recoverability/tau diagnostics |
| `outputs/validation_figures/Figure4_Heatmap.png` | Collision and recoverability heatmap |
| `outputs/condensed_regime_analysis/` | Condensed-regime analysis figures |
| `outputs/condensed_regime_analysis_fast/` | Fast condensed-regime analysis artifacts |
| `outputs/extended/` | Extended reconstruction outputs for multiple attachment settings |

## Method Summary

The workflow follows four main stages:

1. Simulate preferential-attachment networks across selected parameters.
2. Measure degree-collision structure and related reconstruction ambiguity.
3. Apply reconstruction diagnostics to estimate how much arrival-order information is recoverable.
4. Generate plots and tables that summarize reconstruction accuracy, collision probability, finite-size behavior, and condensed-regime trends.

The project separates main experiment code, validation code, and output artifacts so that results can be inspected without rerunning every experiment.

## Notes on Code Organization

`ba_inference.py` is kept at the repository root for compatibility with the original experiment scripts. The same core utilities are also available under `src/` for clearer source organization.

`shared/ba_experiments_full.py` contains reusable experiment functions from the broader preferential-attachment workflow. It is included so the repository can run independently without relying on another local project folder.

## Skills and Concepts

This project combines ideas from:

- network science
- graph theory
- preferential-attachment models
- inverse problems on graphs
- statistical simulation
- reconstruction diagnostics
- finite-size scaling
- scientific Python programming
- reproducible research workflows

## Status

Research project code and generated experiment artifacts.
