import ollama

def analyze_sql_with_ai(query):

    prompt = f"""
You are a senior SQL developer and Data QA engineer.

Analyze the SQL query and return results in the following format:

SQL_ISSUES:
Explain syntax errors or logical problems.

CORRECTED_QUERY:
Provide corrected SQL query if needed.

OPTIMIZATION_SUGGESTIONS:
Suggest improvements for performance.

VALIDATION_QUERIES:
Provide SQL queries for:
- Row count validation
- Duplicate checks
- Null checks

REGRESSION_CHECKS:
Suggest regression test validations.

DATA_MISMATCH_CAUSES:
Explain possible reasons for data mismatch.

TEST_CASES:
Provide testing scenarios for the query.

SQL Query:
{query}
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]