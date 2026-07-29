# 💳 Credit Risk & Loan Default Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Google Colab](https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

# 📌 Project Overview

Credit Risk & Loan Default Prediction is an end-to-end Machine Learning project that predicts whether a borrower is likely to default on a loan based on financial, demographic, and credit history information. The primary objective is to assist financial institutions in making informed lending decisions by identifying high-risk applicants before loan approval.

The project follows the complete Machine Learning lifecycle, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, hyperparameter tuning, and evaluation.

---

# 🎯 Objectives

- Predict loan default risk accurately.
- Build a robust Machine Learning classification model.
- Improve lending decision-making.
- Reduce financial risk by identifying potential defaulters.
- Automate the credit risk assessment process.

---

# 📊 Dataset Information

The dataset contains historical loan application records with demographic, financial, and credit-related attributes.

### Features

| Feature | Description |
|---------|-------------|
| person_age | Age of the applicant |
| person_income | Annual income |
| person_home_ownership | Home ownership status |
| person_emp_length | Employment length (years) |
| loan_intent | Purpose of the loan |
| loan_grade | Credit grade assigned |
| loan_amnt | Loan amount requested |
| loan_int_rate | Loan interest rate |
| loan_percent_income | Loan amount as a percentage of income |
| cb_person_default_on_file | Previous loan default history |
| cb_person_cred_hist_length | Credit history length |
| loan_status | Target Variable (0 = No Default, 1 = Default) |

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Google Colab
- Jupyter Notebook

---

# ⚙️ Machine Learning Workflow

## 1. Data Collection
- Loaded dataset
- Checked dataset dimensions
- Explored data types

## 2. Data Preprocessing
- Missing value handling
- Numerical feature scaling
- Categorical feature encoding
- Pipeline creation
- ColumnTransformer implementation

## 3. Exploratory Data Analysis (EDA)
- Target distribution
- Feature distributions
- Correlation analysis
- Income analysis
- Loan amount analysis
- Interest rate analysis
- Credit history analysis

## 4. Feature Engineering
- One-Hot Encoding
- Standard Scaling
- Data transformation
- Training-ready feature matrix creation

## 5. Model Building
- Random Forest Classifier
- GridSearchCV
- Cross Validation
- Hyperparameter Optimization

## 6. Model Evaluation
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Precision-Recall Curve
- Precision-Recall AUC

---

# 🌲 Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

**Hyperparameter Tuning**

- GridSearchCV
- 5-Fold Cross Validation

**Optimized Parameters**

- n_estimators
- max_depth
- min_samples_split

---

# 📈 Results

The Random Forest Classifier achieved strong predictive performance for identifying loan defaulters.

### Model Highlights

- High classification accuracy
- Strong recall for default prediction
- Reliable precision
- Reduced false negatives
- Robust performance after hyperparameter tuning

---

# 📊 Visualizations Included

- Target Variable Distribution
- Income Distribution
- Loan Amount Distribution
- Interest Rate Distribution
- Correlation Heatmap
- Confusion Matrix
- Precision-Recall Curve

---

# 📂 Project Structure

```
Credit-Risk-Loan-Default-Prediction/
│
├── Credit_Risk_Loan_Default_Pipeline.ipynb
├── credit_risk_dataset.csv
├── README.md
├── requirements.txt
└── images/
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Credit-Risk-Loan-Default-Prediction.git
```

### Move to Project Folder

```bash
cd Credit-Risk-Loan-Default-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

---

# ▶️ How to Run

1. Open the notebook.
2. Run all cells sequentially.
3. Preprocess the dataset.
4. Train the Random Forest model.
5. Evaluate model performance.
6. Predict loan default risk.

---

# 💼 Applications

- Banking
- Loan Approval Systems
- Credit Risk Assessment
- Financial Institutions
- FinTech Companies
- Automated Lending Solutions

---

# 📚 Skills Demonstrated

- Machine Learning
- Classification
- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Pipeline Creation
- Hyperparameter Tuning
- Cross Validation
- Model Evaluation
- Data Visualization
- Credit Risk Analytics

---

# 🔮 Future Improvements

- XGBoost Classifier
- LightGBM
- CatBoost
- SMOTE for Imbalanced Data
- Explainable AI using SHAP
- Streamlit Web Application
- Flask/FastAPI Deployment
- Docker Deployment
- Cloud Deployment

---

# 📌 Key Highlights

- End-to-End Machine Learning Pipeline
- Automated Data Preprocessing
- Hyperparameter Optimization using GridSearchCV
- Random Forest Classification
- Credit Risk Prediction
- Business-Oriented AI Solution
- Real-World Financial Analytics Project

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve this project, feel free to fork the repository, create a new branch, and submit a pull request.

---

# ⭐ Support

If you found this project helpful, please consider giving it a **Star ⭐** on GitHub.

---

## 👩‍💻 Author

**Anuska Biswas**

Machine Learning | Data Science | Artificial Intelligence

---
---

> **Note:** This project was developed for educational purposes to demonstrate an end-to-end Machine Learning workflow for Credit Risk & Loan Default Prediction.
