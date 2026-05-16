import pandas as pd 
import sqlite3

df = pd.read_excel("data/uab_records.xlsx")
conn = sqlite3.connect("students.db")
df.to_sql("uab_records", conn, if_exists="replace", index=False)
print("Database created successfully.")
