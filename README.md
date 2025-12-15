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

## Notes & suggested improvements

- Fix the `assignment02-bankholdiays.py` filename typo to `assignment02-bankholidays.py` for consistency.
- Add a top-level `requirements.txt` (or `environment.yml`) to pin package versions so others reproduce results.
- If assignments depend on external data files, add a short `DATA.md` or a `data/` folder and reference it here with instructions where to put downloaded files.
- Add a short “Objective” and “Expected output” section to each notebook so reviewers know what to check.
- Consider converting simple `.py` scripts to notebooks (or vice versa) for consistent delivery.

## Contribution & grading checklist (for maintainers / students)

- [ ] Ensure each assignment includes a short description/objective at the top.
- [ ] Confirm all data required by the notebooks is committed or linked with download instructions.
- [ ] Ensure notebooks run from top to bottom without errors in a clean environment.
- [ ] Add tests or a small validation script (optional) to verify outputs for grading.

## Next steps I can take for you

- Open each file and generate a concise summary of what it does (I can extract titles, cell outputs, and code highlights).
- Create or update this `assignments/README.md` in the repository.
- Add `requirements.txt` with detected packages and versions.
- Rename the typo file and update references.

Tell me which of the next steps you'd like me to do (summarize files, commit the README, add requirements, rename file, etc.), and I will proceed.