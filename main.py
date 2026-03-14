from ai_agent import analyze_sql_with_ai

query = input("Enter SQL query: ")

result = analyze_sql_with_ai(query)

print("\nAI Analysis:\n")
print(result)