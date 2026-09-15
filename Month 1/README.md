# 📊 Project FORESIGHT: Demand & Inventory Intelligence
### **Zidio Development — Month 1 Internship Project**
#### **Team #8**

---

## 🚀 Executive Overview
**Project FORESIGHT** is an end-to-end data engineering, machine learning, and business intelligence pipeline designed to solve supply chain inefficiencies. The system ingests raw relational inventory data, performs exploratory data analysis to uncover hidden sales trends, trains a predictive machine learning model for demand forecasting, and evaluates real-time stock health to prevent costly stockouts.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python (3.10+)
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **Data Visualization:** Seaborn, Matplotlib
* **Web Application Framework:** Streamlit
* **Version Control:** Git, GitHub Desktop, VS Code

---

## ⚙️ How to Run Locally
If you want to run this application or test the pipeline on your local machine, follow these steps:

## Clone the repository:

Bash
git clone [https://github.com/787870/Zidio-Development.git](https://github.com/787870/Zidio-Development.git)
Navigate to the project folder & install dependencies:

Bash
cd "Zidio Development/Month 1/src"
pip install -r requirements.txt
Launch the Streamlit Dashboard:

Bash
cd ../app
streamlit run dashboard.py
Developed with dedication by Team #8 for Zidio Development.

---

## 📂 Repository Structure
```text
Month 1/
│
├── app/
│   └── dashboard.py          # Interactive Streamlit Executive Dashboard
├── data/
│   ├── calendar.csv          # Date dimensions and temporal attributes
│   ├── inventory_snapshots.csv # Historical stock levels and reorder points
│   ├── sales_daily.csv       # Daily transactional sales records
│   └── sku_master.csv        # Product catalog and cost/margin metrics
├── notebooks/
│   └── 01_data_ingestion_and_eda.ipynb # EDA, Feature Engineering & ML Training Notebook
└── src/
    └── requirements.txt      # Project dependencies and libraries

git clone [https://github.com/787870/Zidio-Development.git](https://github.com/787870/Zidio-Development.git)
