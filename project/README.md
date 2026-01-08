# Wind Energy Analysis Project

This repository contains a data analysis project focused on historical wind speed data from Met Éireann, the Irish National Meteorological Service.  
The aim of the project is to explore wind speed patterns and assess their potential relevance for wind energy generation in Ireland.

## Project Overview
The project demonstrates the key stages of a data analytics workflow:
- Acquiring data from an external source
- Cleaning and preparing the data
- Analysing wind speed patterns and trends
- Presenting findings using visualisations

## Repository Structure
- `wind_analysis.ipynb` — main Jupyter Notebook containing the analysis, code, and visualisations  
- `data/` — directory used to store the dataset(s) used in the project  

## Requirements
The project uses Python and the following main libraries:
- pandas
- numpy
# Wind Energy Analysis Project

This folder contains the wind-speed analysis for a small exploratory project.
The primary artefact is the `wind_analysis.ipynb` notebook which reads the
hourly wind-speed dataset, performs cleaning and exploratory analysis, and
produces visualisations useful for assessing wind energy potential.

## Project Overview

- Acquire, clean and inspect hourly wind-speed measurements
- Compute summary statistics and diurnal/seasonal patterns
- Visualise time series, distributions and aggregated summaries

## Repository Structure

- `wind_analysis.ipynb` — main Jupyter Notebook with analysis and plots
- `data/MeanWindSpeed_hourly.csv` — primary dataset used by the notebook
- `README.md` — this file

## Data

The project uses the CSV file at `data/MeanWindSpeed_hourly.csv`. Place any
additional datasets in the `data/` directory. If you refresh or replace the
data, re-run the notebook cells from the top to ensure derived columns are
recomputed.

## Requirements

This project uses standard Python data-science packages. From the repository
root you can create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r ../requirements.txt
```

`requirements.txt` in the repository root lists commonly used packages for the
notebooks (pandas, numpy, matplotlib, seaborn, etc.). Pin versions there if
you need exact reproducibility.

## How to Run

1. From the `project/` directory, start Jupyter Lab or Notebook and open
	 `wind_analysis.ipynb`:

```bash
jupyter lab
```

2. Select the appropriate Python kernel (the virtualenv created above) and
	 run the notebook cells top-to-bottom.

Optional: if you prefer, convert the notebook to a script or run individual
cells in VS Code's notebook editor.

## Reproducibility & Notes

- Ensure the active kernel matches the virtual environment with installed
	dependencies.
- If you plan to distribute results, pin package versions in
	`requirements.txt` or produce an environment export.

## Contact

Repository owner: dimon-ua
