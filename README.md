# Assignments

This folder contains the course/homework assignments for the PFDA repository. Each file is an assignment that demonstrates basic data loading, analysis and plotting with Python / Jupyter.

## Contents

- `assignment01-plot.ipynb` — Introductory plotting examples (matplotlib / seaborn).
- `assignment02-bankholdiays.py` — Script working with bank holidays data (note: filename contains a typo `bankholdiays` → consider renaming to `assignment02-bankholidays.py`).
- `assignment03-pie.ipynb` — Example creating pie charts / categorical distribution visualizations.
- `assignment05-population.ipynb` — Population data exploration and visualizations.
- `assignment_6_Weather.ipynb` — Weather dataset analysis (time series / plots).

> If any file names or descriptions above are inaccurate, I can open each file and extract a short summary to replace these placeholders.

## Prerequisites

- Python 3.8+ (or compatible)
- JupyterLab / Jupyter Notebook
- Typical Python packages used in these notebooks:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - jupyter

You can create a virtual environment and install packages with:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
pip install -U pip
pip install jupyter pandas numpy matplotlib seaborn
```

If you want, I can add a `requirements.txt` with exact versions.

## How to run

- Notebooks (.ipynb): open with JupyterLab or Jupyter Notebook
  ```bash
  jupyter lab
  # or
  jupyter notebook
  ```
  then open the `.ipynb` files from the browser UI and run the cells.

- Python script(s): run directly
  ```bash
  python assignment02-bankholdiays.py
  ```

