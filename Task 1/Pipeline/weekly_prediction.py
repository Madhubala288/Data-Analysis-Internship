import pandas as pd
import pickle
import os
from datetime import datetime
MODEL_PATH = "../Notebook/models/logistic_model.pkl"
SCALER_PATH = "../Notebook/models/scaler.pkl"
INPUT_PATH = "input/new_customer_data.csv"
OUTPUT_DIR = "output"
print(" Automated Weekly Pipeline Started...")
if not os.path.exists(INPUT_PATH):
    print(f" Error: No new data found at {INPUT_PATH}. Please drop the weekly file there.")
else:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)
    data = pd.read_csv(INPUT_PATH)
    features = data[['tenure', 'MonthlyCharges']] 
    scaled_features = scaler.transform(features)
    probability = model.predict_proba(scaled_features)[:, 1]
    data["Churn_Probability"] = probability
    data["Risk"] = pd.cut(probability, bins=[0, 0.3, 0.7, 1], labels=["Low", "Medium", "High"])
    current_date = datetime.now().date()
    output_file = os.path.join(OUTPUT_DIR, f"weekly_churn_report_{current_date}.csv")
    data.to_csv(output_file, index=False)
    print(f"✅ Success! Weekly report saved at: {output_file}")