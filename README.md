# 📊 data-quant-python-go

A personal learning repository combining concepts and hands-on projects in:

- ⚙️ Data Engineering
- 🐍 Python, and SQL

This repo documents my journey towards becoming a **Data Engineer**.

---

## 🗺️ Learning Roadmap

### 📅 Stage 1 – Core Foundations: NumPy, SQL, ETL/ELT
- [x] NumPy fundamentals (`notebooks/numpy_basics.ipynb`)
- [x] pandas fundamentals (`notebooks/pandas_basic.ipynb`)
- [ ] Intro to SQL & databases
- [x] Basic ETL using pandas + SQL
- [ ] Mini project – mini backtester or data dashboard

### 🔁 Upcoming Topics
- Python for statsmodels and backtesting
- Intermediate SQL + Airflow pipelines
- PySpark & Kafka streaming
- Monitoring, testing, cloud (AWS)

---

## 📁 Folder Structure
```
data-quant-python-go/    
│    
├── notebooks/                    # 📓 Jupyter Notebooks – concepts & exercises      
│    ├── numpy_basic.ipynb    
│    └── pandas_basic.ipynb
│  
├── logs/    
│    └── pipeline.log    
│  
├── projects/                     # 🚧 Larger mini-projects & experiments        
│  
├── src/  
│    ├── __init__.py               
│    ├── logger.py                  
│    └── data_engineering/    
│         ├── __init__.py   
│         ├── simple_etl_pipeline.py       
│         └── example_pipeline.py      
│    
├── resources/                    # 🗂️ Datasets, CSV files, charts      
│    ├── input    
│    │    └── sales.csv    
│    └── output      
│         └── low_revenue.csv    
│    
├── tests/    
│    ├── __init__.py      
│    └── test_simple_etl.py    
│    
├── README.md                     
└── requirements.txt              # 📦 Dependencies      
```
---

## 🔧 Instalations

1. Sklonuj repozytorium:    
   
```bash
git clone https://github.com/SerumYouNeed/data-quant-python-go.git
cd data-quant-python-go
```

2. Utwórz i aktywuj środowisko wirtualne:  
   
```bash
python -m venv venv
source venv/bin/activate  # Unix/Linux
# or
venv\Scripts\activate  # Windows
```

3. Zainstaluj zależności:  
   
```bash
pip install -r requirements.txt
```

## 🚀 How to run a pipeline

```bash
python src/data_engineering/simple_etl_pipeline.py
```


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

## ✅ Testing

To run tests:
```bash
pytest tests/
```

## 📚 References & Inspiration
Python for Data Analysis – Wes McKinney    
Python for Finance – Yves Hilpisch    
Kaggle Learn  

## 👨‍💻 Author
This is a work-in-progress educational repo built by a self-taught developer with a passion for data and programming. Every commit is a step toward becoming a professional Data Engineer.