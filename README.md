
# Instacart Market Basket Analysis

## 📄 Project Overview
This project analyzes Instacart transactional data to derive actionable insights for:
1. **Optimizing product recommendations** through Market Basket Analysis.
2. **Segmenting customers** based on shopping patterns.
3. **Predicting customer churn** to improve retention strategies.

---

## 📊 Key Insights
### 1. Market Basket Analysis
- **Objective:** Identify frequently bought product combinations.
- **Findings:** 
  - Bag of Organic Bananas -> Organic Hass Avocado (Lift: 1.81, Confidence: 0.29)
  - Organic Hass Avocado -> Bag of Organic Bananas (Lift: 1.81, Confidence: 0.16)
  - Banana -> Organic Avocado (Lift: 1.50, Confidence: 0.11)
- **Actionable Insight:** Cross-promote frequently paired items to increase basket value.

### 2. Customer Segmentation
- **Objective:** Group customers based on purchasing patterns.
- **Findings:** 
  - **High-frequency shoppers:** Order every 7 days, avg. basket size of 15 items.
  - **Occasional shoppers:** Order every 30 days, avg. basket size of 5 items.
  - **Seasonal bulk buyers:** Order every 90 days, avg. basket size of 30 items.
- **Actionable Insight:** Offer loyalty programs to frequent shoppers and discounts to occasional shoppers.

### 3. Churn Prediction
- **Objective:** Identify customers likely to churn and improve retention strategies.
- **Findings:** 
  - Model Accuracy: 1.00
  - Key drivers of churn: Long gaps between orders and small basket sizes.
- **Actionable Insight:** Send re-engagement emails or personalized discounts to customers predicted to churn.

---

## 🛠️ Project Structure
```
Instacart_Analysis/
│
├── data/                              # Raw and processed data
├── notebooks/                         # Jupyter notebooks for analysis
│   ├── 1_data_loading_and_preprocessing.ipynb
│   ├── 2_question1_product_recommendations.ipynb
│   ├── 3_question2_customer_segmentation.ipynb
│   ├── 4_question3_customer_churn.ipynb
│
├── scripts/                           # Python scripts for reusable code
│   ├── data_cleaning.py
│   ├── market_basket.py
│   ├── customer_segmentation.py
│   ├── churn_analysis.py
│
├── reports/                           # Final reports and visualizations
│   ├── Instacart_Insights_Report.pdf  # Summary of findings
│
└── README.md                          # Project overview and instructions
```

---

## 🚀 How to Run the Project
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/instacart-analysis.git
cd instacart-analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Scripts
- **Data Cleaning:** `python scripts/data_cleaning.py`
- **Market Basket Analysis:** `python scripts/market_basket.py`
- **Customer Segmentation:** `python scripts/customer_segmentation.py`
- **Churn Prediction:** `python scripts/churn_analysis.py`

---

## 📦 Dependencies
- `pandas`
- `numpy`
- `scikit-learn`
- `mlxtend`
- `matplotlib`

---

## 📋 License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🤝 Acknowledgements
Thanks to [Kaggle](https://www.kaggle.com/c/instacart-market-basket-analysis) for providing the dataset.
