import sqlite3
from utils.llm import get_llm_response

conn = sqlite3.connect("students.db")

def ask_sql(question):
    # Get table schema
    cursor = conn.execute("PRAGMA table_info(uab_records)")
    columns = cursor.fetchall()
    schema_info = "\n".join([f"- \"{col[1]}\": {col[2]}" for col in columns])

    print("Available columns:", [col[1] for col in columns])  # Debug print

    prompt = f"""Table: uab_records
Columns:
{schema_info}

Convert this question into SQL query. Use the EXACT column names from the schema above, including double quotes if they contain spaces or special characters.
If a column name contains a space or symbol, wrap it in double quotes exactly as shown.
Do not assume or invent column names - only use those listed.

If the question refers to marks, score, points, or result, use the column "Marks (/100)".
If the question refers to attendance, use the column "Attendance (%)".
If the question asks for an average by department, use AVG("Marks (/100)") and GROUP BY Department.
If the question asks for the highest average marks by department, use ORDER BY AVG("Marks (/100)") DESC LIMIT 1.

Question: {question}
Return ONLY SQL query
"""
    sql_query = get_llm_response(prompt)
    sql_query = sql_query.replace("```sql","").replace("```","").strip()
    print("Generated SQL Query:", sql_query)
    cursor = conn.execute(sql_query)
    result= cursor.fetchall()
    return result