# PFDA

A small collection of data analysis assignments, notebooks, and helper
scripts used for learning and experiments with Python data tools.

## Repository Overview

- **assignments/** — Course assignments and notebooks (weather, plotting, etc.).
- **my-work/** — Personal experiments and utility scripts (e.g. `read_data.py`, `print_json_console.py`).
- **project/** — Project work and analyses (includes `wind_analysis.ipynb` and project data).

## Notable files

- `project/data/MeanWindSpeed_hourly.csv` — Wind-speed dataset used in the project notebooks.
- `my-work/data.csv` — Small data sample used by notebooks in `my-work`.
- `log-file/access.log.txt` — Example log file for log-parsing exercises.

## Getting Started

1. (Optional) Create and activate a virtual environment:

	python -m venv .venv
	source .venv/bin/activate

2. Install commonly used packages (adjust as needed):

	pip install pandas numpy matplotlib jupyter

3. Open the notebooks with VS Code or Jupyter:

	jupyter lab

Or open `/workspaces/PFDA/project/wind_analysis.ipynb` in VS Code's notebook editor.

## Running scripts

- Example: run a small utility

  python my-work/read_data.py

Adjust the command to your active Python interpreter/virtual environment.

## Contributing

Feel free to open issues, add notebooks, or submit improvements. Keep code and
notebooks focused and include a short description of changes.

## Contact

Repository owner: dimon-ua

## Requirements

Install the project's Python dependencies (recommended in a virtualenv):

```
pip install -r requirements.txt
```

The included `requirements.txt` contains commonly used data-analysis packages for the notebooks.

## Examples

- Start Jupyter Lab and open notebooks:

```
jupyter lab
```

- Run a small utility script from the repository root:

```
python my-work/read_data.py
```

## Notes

- Pin versions in `requirements.txt` if you need reproducible environments.


