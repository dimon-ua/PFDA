## Files and Assignments

1. **Projected Birth Rates**
   - File: `assignment01_births.ipynb`
   - Description: Plots the projected birth rates in Ireland based on CSO data.

2. **Northern Bank Holidays**
   - File: `assignment02-bankholidays.py`
   - Description: Prints the dates of bank holidays in Northern Ireland and those unique to the region.

3. **Pie Chart of Email Domains**
   - File: `assignment03-pie.ipynb`
   - Description: Creates a pie chart showing the distribution of email domains from a CSV file containing 1000 users.

4. **Population by Sex and Age**
   - File: `assignment05-population.ipynb`
   - Description:
     - Calculates the weighted mean age for males and females in Ireland.
     - Computes the population difference by sex within a selected age group.
     - Identifies the region with the largest difference between sexes.

5. **Knock Airport Weather**
   - File: `assignment06-weather.ipynb`
   - Description:
     - Plots temperature data (daily and monthly averages).
     - Analyzes wind speed: raw data, rolling 24-hour mean, daily max, and monthly mean of daily max.

## Libraries Used
- pandas
- matplotlib
- seaborn
- requests

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
pip install -U pip
pip install jupyter pandas numpy matplotlib seaborn
```

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
