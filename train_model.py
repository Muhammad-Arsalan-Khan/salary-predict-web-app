"""
Ye script model train karke 'salary_model.pkl' file mein save kar deta hai.
Isay sirf ek dafa chalayein — jab tak data ya features change na karein.
"""

import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Data load karein
data = pd.read_csv('Salary Data.csv')
data = data.dropna()

education_map = {
    "Bachelor's": 1,
    "Master's": 2,
    "PhD": 3
}
data["Education Level"] = data["Education Level"].map(education_map)

X = data[['Years of Experience', 'Education Level']]
y = data['Salary']

model = LinearRegression()
model.fit(X, y)

# Model ko file mein save karein
with open('salary_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model 'salary_model.pkl' mein save ho gaya!")
