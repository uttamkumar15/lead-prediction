import joblib
import pandas as pd
model = joblib.load('model.pkl')

df  = 'your dataset'

status = model.predict(df)
print(status)