import pandas as pd
df_ads = pd.read_csv('/content/train_data_ads_test.csv')
df_feeds = pd.read_csv('/content/train_data_feeds_test.csv')
print("The data is loaded...")

import sys
sys.path.insert(0,'/content/Trustworthy-AI-X-GES-Dumb-Peeps/Dataset_Utility')

from Dataset_Utility import utility_functions as uf
uf.calculate_label_rate(df_ads)
uf.calculate_label_rate(df_feeds)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

for col in df_ads.columns:
    if df_ads[col].dtype == 'object':
        le = LabelEncoder()
        df_ads[col] = le.fit_transform(df_ads[col])

for col in df_feeds.columns:
    if df_feeds[col].dtype == 'object':
        le = LabelEncoder()
        df_feeds[col] = le.fit_transform(df_feeds[col])

X_ads = df_ads.drop('label', axis=1)  # 訓練集特徵數據
y_ads = df_ads['label']  # 訓練集目標數據

X_feeds = df_feeds.drop('label', axis=1)  # 驗證集特徵數據
y_feeds = df_feeds['label']  # 驗證集目標數據

for name, model in models.items():
    # 訓練模型
    model.fit(X_ads, y_ads)
    # 在驗證數據集上預測
    feeds_predictions = model.predict(X_feeds)
    # 計算驗證集的準確度
    feeds_accuracy = accuracy_score(y_feeds, feeds_predictions)
    print(f'{name} Validation Accuracy: {feeds_accuracy:.2f}')

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the data
df_ads = pd.read_csv('/content/train_data_ads_test.csv')
df_feeds = pd.read_csv('/content/train_data_feeds_test.csv')

# Check and convert non-numeric data to numeric
for col in df_ads.columns:
    if df_ads[col].dtype == 'object':
        le = LabelEncoder()
        df_ads[col] = le.fit_transform(df_ads[col])

for col in df_feeds.columns:
    if df_feeds[col].dtype == 'object':
        le = LabelEncoder()
        df_feeds[col] = le.fit_transform(df_feeds[col])

# Split the data into features and target
X_ads = df_ads.drop('label', axis=1)
y_ads = df_ads['label']
X_feeds = df_feeds.drop('label', axis=1)
y_feeds = df_feeds['label']

# Align columns
X_feeds = X_feeds.reindex(columns=X_ads.columns, fill_value=0)

# Define models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

# Train and evaluate each model
for name, model in models.items():
    # Train model
    model.fit(X_ads, y_ads)
    # Predict on validation data
    feeds_predictions = model.predict(X_feeds)
    # Calculate accuracy
    feeds_accuracy = accuracy_score(y_feeds, feeds_predictions)
    print(f'{name} Validation Accuracy: {feeds_accuracy:.2f}')

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the data
df_ads = pd.read_csv('/content/train_data_ads_test.csv')
df_feeds = pd.read_csv('/content/train_data_feeds_test.csv')

# Encode non-numeric features consistently
label_encoders = {}
for col in df_ads.columns:
    if df_ads[col].dtype == 'object':
        le = LabelEncoder()
        df_ads[col] = le.fit_transform(df_ads[col])
        label_encoders[col] = le

for col in df_feeds.columns:
    if df_feeds[col].dtype == 'object':
        if col in label_encoders:
            le = label_encoders[col]
            df_feeds[col] = le.transform(df_feeds[col])
        else:
            le = LabelEncoder()
            df_feeds[col] = le.fit_transform(df_feeds[col])
            label_encoders[col] = le

# Align columns
common_columns = list(set(df_ads.columns).intersection(set(df_feeds.columns)))
df_ads = df_ads[common_columns]
df_feeds = df_feeds[common_columns]

# Ensure no missing values
df_ads.fillna(0, inplace=True)
df_feeds.fillna(0, inplace=True)

# Split the data into features and target
X_ads = df_ads.drop('label', axis=1)
y_ads = df_ads['label']
X_feeds = df_feeds.drop('label', axis=1)
y_feeds = df_feeds['label']

# Consistent label encoding for target variable
label_encoder_y = LabelEncoder()
y_ads = label_encoder_y.fit_transform(y_ads)
y_feeds = label_encoder_y.transform(y_feeds)

# Define models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

# Train and evaluate each model
for name, model in models.items():
    # Train model
    model.fit(X_ads, y_ads)
    # Predict on validation data
    feeds_predictions = model.predict(X_feeds)
    # Calculate accuracy
    feeds_accuracy = accuracy_score(y_feeds, feeds_predictions)
    print(f'{name} Validation Accuracy: {feeds_accuracy:.2f}')