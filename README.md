# 📊 Customer Churn Prevention System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Google Colab](https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

Predict customer churn using Machine Learning and uncover the key business factors driving customer attrition. This project leverages **Decision Tree** and **Random Forest** classifiers to identify customers at risk of leaving, helping businesses take proactive retention measures through data-driven insights.

---

## 🎯 Project Objectives

* Build a Machine Learning model to predict customer churn.
* Compare the performance of Decision Tree and Random Forest classifiers.
* Evaluate model performance using industry-standard classification metrics.
* Identify the most influential features contributing to churn.
* Translate model findings into actionable business strategies for customer retention.

---

## 📂 Dataset

* **Source:** Kaggle
* **Dataset Type:** Customer Churn Dataset
* **Target Variable:** `Churn` (Yes/No)

The dataset contains customer demographics, account information, subscription details, service usage, and billing history used to predict whether a customer is likely to churn.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Jupyter Notebook

---

## 🤖 Machine Learning Algorithms

* Decision Tree Classifier
* Random Forest Classifier

---

## ⚙️ Project Workflow

1. Import required libraries.
2. Load and inspect the dataset.
3. Perform data cleaning and preprocessing.
4. Encode categorical variables.
5. Split the dataset into training and testing sets.
6. Train Decision Tree and Random Forest models.
7. Evaluate model performance.
8. Analyze feature importance.
9. Generate business recommendations based on model insights.

---

## 📊 Exploratory Data Analysis (EDA)

The dataset was explored to understand:

* Customer demographics
* Churn distribution
* Contract types
* Monthly and total charges
* Service subscription patterns
* Relationships between customer attributes and churn

Visualizations created using **Matplotlib** helped identify important trends and patterns in customer behavior.

---

# 📈 Model Performance

| Metric            |      Score |
| ----------------- | ---------: |
| **Accuracy**      | **79.49%** |
| **Precision**     | **64.71%** |
| **Recall**        | **50.00%** |
| **F1-Score**      | **56.41%** |
| **ROC-AUC Score** | **83.85%** |

### Performance Summary

* **Accuracy:** Correctly classified nearly **8 out of 10** customers.
* **Precision:** Approximately **65%** of predicted churn customers actually churned.
* **Recall:** Successfully identified **50%** of actual churn cases.
* **F1-Score:** Balanced precision and recall for reliable classification performance.
* **ROC-AUC:** Achieved **83.85%**, indicating strong ability to distinguish between churn and non-churn customers.

---

## 🔍 Feature Importance

Feature Importance analysis was performed using the **Random Forest Classifier** to determine which customer attributes contribute most to churn prediction.

This helps businesses understand the primary reasons customers leave and supports strategic decision-making for customer retention.

---

## 💼 Business Impact

The developed model enables organizations to:

* Predict customers at high risk of churning.
* Launch targeted retention campaigns.
* Improve customer engagement strategies.
* Reduce customer acquisition costs.
* Increase customer lifetime value (CLV).
* Make informed business decisions using data-driven insights.

---

## 📌 Key Features

* ✅ End-to-end Customer Churn Prediction pipeline
* ✅ Data preprocessing and feature engineering
* ✅ Decision Tree and Random Forest implementation
* ✅ Feature Importance analysis
* ✅ Customer churn classification
* ✅ Performance evaluation using multiple metrics
* ✅ Business-oriented insights and recommendations

---

## 📁 Repository Structure

```text
Customer_Churn_Prevention/
│
├── Customer_Churn_Prevention.ipynb
├── customer_churn_model.pkl
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

```bash
git clone https://github.com/your-username/Customer_Churn_Prevention.git

cd Customer_Churn_Prevention

pip install -r requirements.txt
```

---

## ▶️ Usage

1. Open the Jupyter Notebook.
2. Run all notebook cells sequentially.
3. Train the Machine Learning models.
4. Evaluate model performance.
5. Interpret feature importance.
6. Predict customer churn for new customer records.

---

## 📊 Expected Output

* Customer Churn Prediction Model
* Decision Tree & Random Forest Comparison
* Confusion Matrix
* ROC Curve
* Feature Importance Visualization
* Business Report with Customer Retention Strategies

---

## 📚 Skills Demonstrated

* Machine Learning Classification
* Data Cleaning & Preprocessing
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Decision Trees
* Random Forest
* Model Evaluation
* Feature Importance Analysis
* Business Analytics
* Data Visualization

---

## 🔮 Future Improvements

* Hyperparameter tuning using GridSearchCV
* Cross-validation for improved model robustness
* Address class imbalance using SMOTE
* Deploy the model with Streamlit or Flask
* Real-time customer churn prediction dashboard

---

## 👩‍💻 Author

**Anuska Biswas**

If you found this project useful, consider giving it a ⭐ on GitHub!

