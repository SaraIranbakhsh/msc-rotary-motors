# MSc research code: coupled rotary molecular motors (Fo–F1)

This repository contains the simulation and analysis code used in my M.Sc. research on **coupled rotary molecular motors** (ATP synthase Fo–F1), focusing on symmetry mismatch and intermediate coupling regimes.

## Repository layout

- `Cluster_code_source/`
  - `main_model{1..4}.py` — entry points for running simulations (calls the corresponding FPE solvers)
  - `fpe_model{1..4}.pyx` — Cython implementations of the Fokker–Planck / inertial Langevin solver kernels
  - `setup_model{1..4}.py` — build scripts to compile the Cython modules
  - `utilities.pyx` — shared Cython utilities
  - `production_slurm.sh`, `parallel_submit_slurm.sh`, `parallelize.sh` — SLURM helpers for cluster runs
- `Analyze/`
  - Jupyter notebooks for post-processing and figure generation:
    - `File_processing.ipynb`
    - `Paper_plots.ipynb`
    - `Thesis_plots.ipynb`
    - `mu_vs_Ec.ipynb`

## Quick start (local)

### 1) Create an environment

With **conda**:
```bash
conda create -n msc-motors python=3.11 -y
conda activate msc-motors
pip install -U pip
pip install numpy scipy pandas matplotlib cython jupyter imageio kneed qrcode
```

Or with **pip** in a venv:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install numpy scipy pandas matplotlib cython jupyter imageio kneed qrcode
```

### 2) Compile the Cython modules (recommended)

From the repo root:
```bash
cd Cluster_code_source
python setup_model1.py build_ext --inplace
python setup_model2.py build_ext --inplace
python setup_model3.py build_ext --inplace
python setup_model4.py build_ext --inplace
```

Notes:
- The `main_model*.py` scripts also use `pyximport`, which can compile on first import, but explicit compilation is usually faster and more reproducible.
- You may need a C compiler (Xcode Command Line Tools on macOS, or `build-essential` on Linux).

### 3) Run a simulation

Example:
```bash
python Cluster_code_source/main_model1.py
```

Parameters are currently set inside each `main_model*.py` script (e.g., `Ecouple`, `dt`, `N`, `gamma0`, `gamma1`, etc.). Edit those values for your runs.

## Running on a SLURM cluster (e.g., Cedar)

The SLURM scripts in `Cluster_code_source/` are templates. Typical workflow:

1. Copy the repo to the cluster.
2. Load a Python module / activate an environment with `cython`, `numpy`, etc.
3. Submit a job script, e.g.:
```bash
sbatch Cluster_code_source/production_slurm.sh
```

If you parallelize sweeps, use `parallel_submit_slurm.sh` and `parallelize.sh` as starting points.

## Reproducibility

- Notebooks in `Analyze/` assume outputs produced by the cluster scripts and may need path edits.
- Consider pinning exact package versions (e.g., via `pip freeze > requirements.txt`) once you finalize figures.

## Citation

If you use this code, please cite the associated thesis/paper:
- *Add your thesis/paper citation here.*

## License

Choose a license before publishing (MIT/BSD-3-Clause are common for academic code).
