import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score

print("Loading dataset...")

df = pd.read_csv('creditcard.csv')

# Split features and target
X = df.drop(columns=['Class'])
y = df['Class']

print("Splitting data into train and test sets...")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("Applying SMOTE to balance the dataset...")

smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

print("Training XGBoost Classifier...")

model = XGBClassifier(n_estimators=100, random_state=42)
model.fit(X_train_res, y_train_res)

# Evaluate model
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

print("Saving trained model to pickle file...")

with open('fraud_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Success: 'fraud_model.pkl' created and saved successfully!")