---
title: Customer Churn Dashboard
emoji: 📊
colorFrom: blue
colorTo: green
sdk: streamlit
app_file: app.py
path_in_repo: Task 1
pinned: false
---
# Customer Behavior Analytics & Churn Prediction Dashboard

## Project Overview

This project develops an end-to-end **Customer Behavior Analytics and Churn Prediction System** that analyzes customer behavior, identifies churn patterns, predicts churn probability, and generates actionable business insights.

The system combines:

- Data Analysis
- Feature Engineering
- Customer Segmentation
- Machine Learning Models
- Explainable AI (SHAP)
- Interactive Streamlit Dashboard
- Automated Weekly Prediction Pipeline
- Email Report Generation


---

# Business Problem

Customer churn directly impacts business revenue. Companies need a system that can identify customers who are likely to leave and understand the reasons behind churn.

This project helps businesses to:

- Analyze customer behavior patterns
- Identify high-risk customers
- Predict churn probability
- Segment customers based on value
- Take preventive retention actions


---

# Dataset

Dataset Used:

**Telco Customer Churn Dataset**

The dataset contains customer information:

- Demographics
- Services usage
- Contract details
- Payment methods
- Monthly charges
- Total charges
- Churn status


### Main Features

| Feature | Description |
|---|---|
| CustomerID | Unique customer identifier |
| Gender | Customer gender |
| SeniorCitizen | Senior citizen indicator |
| Partner | Partner information |
| Dependents | Dependents information |
| Tenure | Customer relationship duration |
| InternetService | Internet service type |
| Contract | Contract type |
| PaymentMethod | Payment method |
| MonthlyCharges | Monthly billing amount |
| TotalCharges | Total amount paid |
| Churn | Customer churn status |


---

# Project Workflow

```
Customer Data
      |
      ↓
Data Cleaning
      |
      ↓
Exploratory Data Analysis
      |
      ↓
Feature Engineering
      |
      ↓
Customer Segmentation
      |
      ↓
Machine Learning Models
      |
      ↓
Churn Prediction
      |
      ↓
SHAP Explainability
      |
      ↓
Streamlit Dashboard
      |
      ↓
Automated Reports
      |
      ↓
Email Notification
```


---

# Features Implemented

## 1. Data Analysis

Performed:

- Dataset loading
- Data exploration
- Missing value handling
- Duplicate removal
- Outlier detection
- Summary statistics


---

## 2. Feature Engineering

Created behavioral features:

### Tenure Group

Customer classification:

- New Customer
- Medium Customer
- Loyal Customer


### Service Usage Score

Calculated service usage based on:

- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming Services


### Spending Features

Created:

- Average Monthly Spending
- Customer Value Score


### Risk Features

Created:

- Contract Risk
- Payment Risk


---

# 3. Data Visualization

Implemented visual analysis:

- Churn distribution
- Revenue trends
- Customer segmentation charts
- Correlation heatmap
- Contract-wise churn analysis
- Payment method comparison
- Internet service comparison


---

# 4. Customer Segmentation

Customers are divided into:

## High Value Customers

Based on:

- High spending
- Long tenure
- More services


## Medium Value Customers

Customers with average behavior.


## Low Value Customers

Based on:

- Low spending
- Short tenure
- Limited services


---

# 5. Machine Learning Models

Two models were trained:


## Logistic Regression

Baseline classification model.


## Random Forest Classifier

Main predictive model used for churn prediction.


---

# Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score


---

# 6. Churn Prediction System

The system predicts:

## Churn Probability

Example:

```
Churn Probability: 82%
```


## Risk Category

| Probability | Risk Level |
|---|---|
| 0-30% | Low Risk |
| 30-70% | Medium Risk |
| 70-100% | High Risk |


---

# 7. SHAP Explainability

SHAP is used to explain model predictions.

It identifies:

- Important churn factors
- Features increasing churn probability
- Features reducing churn probability


Example churn factors:

- Month-to-month contract
- High monthly charges
- Low tenure
- Lack of support services


---

# 8. Streamlit Dashboard

Interactive dashboard includes:

## Overview

- Total customers
- Churn rate
- Revenue impact


## Analytics

- Customer behavior analysis
- Churn visualization


## Customer Segmentation

- High Value
- Medium Value
- Low Value


## Prediction System

Provides:

- Churn probability
- Risk category


---

# 9. Automated Weekly Prediction Pipeline

The pipeline automatically:

- Loads new customer data
- Applies preprocessing
- Generates churn predictions
- Assigns risk categories
- Creates weekly reports


Workflow:

```
New Data
   |
   ↓
ML Model
   |
   ↓
Churn Probability
   |
   ↓
Risk Classification
   |
   ↓
Weekly Report
```


---

# 10. Email Report Generation

The system automatically sends weekly churn reports through email.

Reports include:

- High-risk customers
- Churn probabilities
- Risk categories
- Business summary


---

# Technologies Used

## Programming

- Python


## Data Analysis

- Pandas
- NumPy


## Visualization

- Matplotlib
- Seaborn


## Machine Learning

- Scikit-learn


## Explainable AI

- SHAP


## Dashboard

- Streamlit


## Automation

- Python Automation
- Email Automation


---

# Project Structure

```
Customer_Churn_Analytics/

│
├── Dataset/
│   └── customer_churn.csv
│
├── Notebook/
│   └── Customer_Churn_Analytics.ipynb
│
├── Models/
│   └── churn_model.pkl
│
├── Dashboard/
│   └── app.py
│
├── Pipeline/
│   └── weekly_prediction.py
│
├── Reports/
│   ├── Business_Insights_Report.md
│   └── Model_Report.md
│
├── requirements.txt
│
└── README.md
```


---

# Installation

Clone repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```


---

# Run Streamlit Dashboard

```bash
streamlit run Dashboard/app.py
```


---

# Run Weekly Prediction Pipeline

```bash
python Pipeline/weekly_prediction.py
```


---

# Business Impact

This system helps businesses to:

- Reduce customer churn
- Identify high-risk customers early
- Improve retention strategies
- Understand customer behavior
- Protect revenue


---

# Future Improvements

- Real-time churn monitoring
- Cloud deployment
- Automated model retraining
- Customer retention recommendation system
- Advanced deep learning models


---

# Author

MadhuBala