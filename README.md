# Real-Time Credit Card Fraud Detection System using Apache Kafka & Machine Learning

An end-to-end data science and data engineering project that simulates real-time credit card transactions using Apache Kafka, performs fraud detection using an XGBoost machine learning model, and visualizes live insights via a Power BI dashboard.

## 📊 Project Overview

Financial fraud is a critical issue causing billions of dollars in losses annually. This project demonstrates a production-grade pipeline designed to ingest stream data, apply machine learning inference on-the-fly, handle heavy class imbalance, and serve dashboards to risk analysts.

## 🛠️ Tech Stack & Architecture

- **Data Engineering:** Apache Kafka (Zookeeper, Broker)
- **Machine Learning:** Python (Scikit-Learn, XGBoost, SMOTE, Joblib)
- **Business Intelligence:** Power BI Desktop (DAX Measures, Data Modeling)
- **Environment:** Anaconda / JupyterLab / Python 3.11

## 🚀 System Pipeline Workflow

1. **Producer (`producer.py`):** Ingests transaction records from the `creditcard.csv` dataset and streams them dynamically into a Kafka topic named `ml-transactions`.
2. **Consumer & ML Inference (`consumer.py`):** Listens to the live Kafka topic, loads the trained `fraud_model.pkl` classifier, and evaluates each incoming transaction in real-time.
3. **Handling Imbalance:** Applied SMOTE (Synthetic Minority Over-sampling Technique) during training to handle the highly skewed distribution (0.17% fraud vs 99.83% genuine transactions).
4. **BI Dashboard:** Loaded the tracked metrics into Power BI to create executive reports focusing on:
   - **Total Transactions Processed**
   - **Total Fraud Cases & Flagged Amount**
   - **Anomaly Distributions**

## 📂 Project Structure

```text
├── creditcard.csv            # Dataset containing credit card transactions
├── credit_card_model.ipynb   # Jupyter Notebook for EDA, SMOTE, and XGBoost training
├── fraud_model.pkl           # Saved serialized trained XGBoost model
├── producer.py               # Apache Kafka producer stream simulator
├── consumer.py               # Apache Kafka consumer & live ML prediction engine
├── README.md                 # Project documentation
└── Credit_Card_Fraud_Dashboard.pbix # Power BI Dashboard file
```
