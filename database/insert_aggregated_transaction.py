import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import mysql.connector
from data_transformation.transform_data import df_agg_trans

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sailee@999",
    database="phonepe_pulse"
)

cursor = conn.cursor()

insert_query = """
INSERT INTO aggregated_transaction
(state, year, quarter, transaction_type, transaction_count, transaction_amount)
VALUES (%s, %s, %s, %s, %s, %s)
"""

data = [
    (
        row["state"],
        int(row["year"]),
        int(row["quarter"]),
        row["transaction_type"],
        int(row["transaction_count"]),
        float(row["transaction_amount"])
    )
    for _, row in df_agg_trans.iterrows()
]

cursor.executemany(insert_query, data)
conn.commit()

print(f"{cursor.rowcount} rows inserted successfully.")

cursor.close()
conn.close()

