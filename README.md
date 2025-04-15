# 📊 data-quant-python-go

A personal learning repository combining concepts and hands-on projects in:

- 🧠 Quantitative Development
- ⚙️ Data Engineering
- 🐍 Python, Go, and SQL stack
- 💹 Financial programming and data analysis

This repo documents my journey towards becoming a **Quant Developer** or **Data Engineer** with a strong foundation in algorithms, data pipelines, and financial systems.

---

## 🗺️ Learning Roadmap

### 📅 Week 1 – Core Foundations: NumPy, pandas, Finance Programming
- [x] Day 1: NumPy fundamentals (`notebooks/numpy_basics.ipynb`)
- [ ] Day 2: pandas & time series exploration (`notebooks/pandas_intro.ipynb`)
- [ ] Day 3: Portfolio analysis (risk, return, volatility)
- [ ] Day 4: Intro to SQL & databases
- [ ] Day 5: Basic ETL using pandas + SQL
- [ ] Days 6–7: Weekly project – mini backtester or data dashboard

### 🔁 Upcoming Topics
- Python for Finance, statsmodels, backtesting
- Intermediate SQL + Airflow pipelines
- PySpark & Kafka streaming
- Go: concurrency, performance, system design
- Data APIs + dashboards in React
- Monitoring, testing, cloud (AWS/GCP)

---

## 📁 Folder Structure

data-quant-python-go/
├── notebooks/
├── src/
│   ├── data_engineering/
│   ├── quant/
│   └── go_integration/
├── logs/
├── requirements.txt
├── README.md
└── .gitignore


data-quant-python-go/
│
├── notebooks/               # 📓 Jupyter Notebooks – concepts & exercises
│   ├── numpy_basics.ipynb
│   ├── pandas_intro.ipynb
│   ├── ...
│   ├── ...
│   └── ...
│
├── projects/                # 🚧 Larger mini-projects & experiments
│   ├── .../
│   ├── .../
│   ├── .../
│   └── ...
│
├── resources/               # 🗂️ Datasets, CSV files, charts
│   ├── ...
│   ├── ...
│   └── ...
│
├── scripts/                 # 🐍 Modules and scripts
│   ├── ..
│   ├── ...
│   └── ...
│
├── go_src/                  # 🦫 Golang code
│   ├── ...
│   ├── ...
│   └── ...
│
├── react_dashboard/         # 🌐 (optional) dashboard build in React
│   ├── src/
│   ├── public/
│   └── ...
│
├── README.md
├── .gitignore
└── requirements.txt         # 📦 Dependencies

---

## 🚀 How to Run the Notebooks

```Bash
# 1. Clone the repository
git clone https://github.com/your-username/data-quant-python-go.git
cd data-quant-python-go

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
# Or manually:
pip install numpy pandas matplotlib jupyter

# 4. Launch Jupyter Notebook
jupyter notebook
```
Then open the notebooks/ folder in your browser and start exploring!

To run example scripts or pipelines that use the logger:

```Bash
# From the root directory of the repository
PYTHONPATH=. python src/data_engineering/example_pipeline.py

# This ensures that the src/ directory is included in your Python module path, allowing correct imports like:
from src.logger import get_logger

# You can also make sure src/ and src/data_engineering/ contain __init__.py files (even empty) to treat them as Python packages.
```

## 📚 References & Inspiration
Python for Data Analysis – Wes McKinney
Python for Finance – Yves Hilpisch
Go in Action, Mastering Go
QuantInsti Blog
Kaggle Learn

## 👨‍💻 Author
This is a work-in-progress educational repo built by a self-taught developer with a passion for data, programming, and financial systems. Every commit is a step toward becoming a professional Quant Developer or Data Engineer.