# -*- coding: utf-8 -*-
"""ML techniques.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/167YIiGXqVYVU7b93bfaM5cKqK31q1NB9

# XGBoost
"""

import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load training and testing datasets
train_df = pd.read_excel("/content/train_data.xlsx")
test_df = pd.read_excel("/content/vibraration test data (2).xlsx")
test_df = test_df.head(100)
# Define features and target
features = ['BPFO_Hz', 'BPFI_Hz', 'BSF_Hz', 'FTF_Hz']
target = 'anomaly'

# Encode labels if they're in True/False or string format
label_encoder = LabelEncoder()
train_df[target] = label_encoder.fit_transform(train_df[target])
test_df[target] = label_encoder.transform(test_df[target])

# Separate features and labels
X_train = train_df[features]
y_train = train_df[target]

X_test = test_df[features]
y_test = test_df[target]


# Train XGBoost model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)


# Evaluation
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred, labels=[True, False]))

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=["Normal", "Anomaly"]))

"""# SVM"""

import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Load training and test datasets
train_df = pd.read_excel("/content/train_data.xlsx")
test_df = pd.read_excel("/content/vibraration test data (2).xlsx")
test_df = test_df.head(100)
# Define features and target
features = ['BPFO_Hz', 'BPFI_Hz', 'BSF_Hz', 'FTF_Hz']
target = 'anomaly'

# Encode labels (True/False or strings to 1/0)
label_encoder = LabelEncoder()
train_df[target] = label_encoder.fit_transform(train_df[target])
test_df[target] = label_encoder.transform(test_df[target])

# Extract features and labels
X_train = train_df[features]
y_train = train_df[target]

X_test = test_df[features]
y_test = test_df[target]

# Feature scaling (important for SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the SVM model
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')  # You can tune C and gamma if needed
svm_model.fit(X_train_scaled, y_train)

# Predict on test set
y_pred = svm_model.predict(X_test_scaled)

# Evaluation
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred, labels=[True, False]))

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=["Normal", "Anomaly"]))

"""# ISOLATION FOREST"""

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load datasets
train_df = pd.read_excel("/content/train_data.xlsx")
test_df = pd.read_excel("/content/vibraration test data (2).xlsx")
test_df = test_df.head(100)
# Features used
features = ['BPFO_Hz', 'BPFI_Hz', 'BSF_Hz', 'FTF_Hz']

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(train_df[features])
X_test = scaler.transform(test_df[features])

# Train Isolation Forest
iso_model = IsolationForest(contamination=0.1, random_state=42)
iso_model.fit(X_train)

# Predict: Isolation Forest gives -1 for anomaly, 1 for normal
y_pred_raw = iso_model.predict(X_test)

# Convert to 1 (anomaly), 0 (normal)
y_pred = [1 if p == -1 else 0 for p in y_pred_raw]

# Encode ground truth anomaly labels from test set
label_encoder = LabelEncoder()
y_test = label_encoder.fit_transform(test_df["anomaly"])

# Evaluation
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred, labels=[True, False]))

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=["Normal", "Anomaly"]))

"""# Random Forest"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load training and test datasets
train_df = pd.read_excel("/content/train_data.xlsx")
test_df = pd.read_excel("/content/test_data (2)_with_predictions_with_predictions.xlsx")
test_df = test_df.head(100)

# Define features and target
features = ['BPFO_Hz', 'BPFI_Hz', 'BSF_Hz', 'FTF_Hz']
target = 'anomaly'

# Encode labels (True/False or string → 0/1)
label_encoder = LabelEncoder()
train_df[target] = label_encoder.fit_transform(train_df[target])
test_df[target] = label_encoder.transform(test_df[target])

# Prepare training and testing sets
X_train = train_df[features]
y_train = train_df[target]

X_test = test_df[features]
y_test = test_df[target]

# Train Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict on test set
y_pred = rf_model.predict(X_test)

# Evaluation
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred, labels=[True, False]))

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=["Normal", "Anomaly"]))

