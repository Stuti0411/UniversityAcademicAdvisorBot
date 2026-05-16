from sql_agent.sql_agent import ask_sql

while True:
    question = input("Ask Question: ")
    answer = ask_sql(question)
    print("\nAnswer:", answer)
