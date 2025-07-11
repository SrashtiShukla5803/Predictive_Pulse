#import necessary libraries
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns

# Load(Reading) dataset
df = pd.read_csv("dataset/patient_data.csv")

# Fixing inconsistencies
df['TakeMedication'] = df['TakeMedication'].replace({'Yes ': 'Yes'})
df['NoseBleeding'] = df['NoseBleeding'].replace({'No ': 'No'})
df['Systolic'] = df['Systolic'].replace({'121- 130': '121 - 130'})
df['Stages'] = df['Stages'].replace({
    'HYPERTENSIVE CRISI': 'HYPERTENSIVE CRISIS',
    'HYPERTENSION (Stage-2).': 'HYPERTENSION (Stage-2)'
})

# Label encoding to convert categorical columns to numerical
label_encoders = {}
target_encoder = LabelEncoder()

for col in df.columns:
    if col == 'Stages':
        df[col] = target_encoder.fit_transform(df[col])
    elif df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

# Saving encoders
with open('encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)

with open('stage_encoder.pkl', 'wb') as f:
    pickle.dump(target_encoder, f)

# Split features/target
X = df.drop('Stages', axis=1)
y = df['Stages']

# Visualizing class distribution before balancing
decoded_y = target_encoder.inverse_transform(y)
plt.figure(figsize=(10, 4))
sns.countplot(x=decoded_y, order=target_encoder.classes_)
plt.title("Before Balancing")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SMOTE balancing(Handling Imbalanced Data)
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Visualizing class distribution after balancing
decoded_y_res = target_encoder.inverse_transform(y_train_res)
plt.figure(figsize=(10, 4))
sns.countplot(x=decoded_y_res, order=target_encoder.classes_)
plt.title("After SMOTE Balancing")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Training RandomForest
clf = RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42)
clf.fit(X_train_res, y_train_res)

# Evaluating the model
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=target_encoder.classes_))

# Saving the model 
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)
