import os
import json
import pandas as pd

path = "phonepe_pulse_data/data/aggregated/transaction/country/india/state"
agg_trans = []

for state in os.listdir(path):
    state_path = os.path.join(path, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for file in os.listdir(year_path):
            with open(os.path.join(year_path, file)) as f:
                data = json.load(f)
                for item in data["data"]["transactionData"]:
                    agg_trans.append({
                        "state": state.replace('-', ' ').title(),
                        "year": int(year),
                        "quarter": int(file.strip('.json')),
                        "transaction_type": item["name"],
                        "transaction_count": item["paymentInstruments"][0]["count"],
                        "transaction_amount": item["paymentInstruments"][0]["amount"]
                    })

df_agg_trans = pd.DataFrame(agg_trans)
print(df_agg_trans.head())
print(df_agg_trans.shape)