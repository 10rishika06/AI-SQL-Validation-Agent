import streamlit as st
from ai_agent import analyze_sql_with_ai

st.set_page_config(
    page_title="AI SQL Validation Agent",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("AI SQL Agent")
st.sidebar.write("This tool analyzes SQL queries and generates validation checks, optimizations, and test cases.")

st.sidebar.markdown("### Example Queries")

example_queries = [
    "SELECT * FROM orders",
    "SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id",
    "SELECT o.order_id, c.customer_name FROM orders o JOIN customers c ON o.customer_id = c.customer_id",
    "SELECT name age FROM employees",
    "SELECT email FROM users"
]

for q in example_queries:
    st.sidebar.code(q, language="sql")

st.sidebar.markdown("---")
st.sidebar.write("Tip: Try queries with errors to see AI corrections.")

# Main Title
st.title("🤖 AI SQL Validation Agent")
st.write("Analyze SQL queries and automatically generate validation checks, optimizations, and test cases.")

# Query Input
query = st.text_area(
    "Enter SQL Query",
    height=120,
    placeholder="Example: SELECT * FROM orders"
)

# Query history
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Analyze Query"):

    if query.strip() == "":
        st.warning("Please enter an SQL query.")

    else:

        with st.spinner("Analyzing SQL query..."):

            result = analyze_sql_with_ai(query)

        st.session_state.history.append(query)

        st.success("Analysis Complete")

        sections = {
            "SQL_ISSUES": "⚠ SQL Issues",
            "CORRECTED_QUERY": "✅ Corrected SQL Query",
            "OPTIMIZATION_SUGGESTIONS": "🚀 Optimization Suggestions",
            "VALIDATION_QUERIES": "🔍 Data Validation Queries",
            "REGRESSION_CHECKS": "🔁 Regression Testing Checks",
            "DATA_MISMATCH_CAUSES": "📊 Possible Data Mismatch Causes",
            "TEST_CASES": "🧪 Suggested Test Cases"
        }

        for key, title in sections.items():

            if key in result:
                content = result.split(key + ":")[1]

                for other_key in sections.keys():
                    if other_key != key and other_key + ":" in content:
                        content = content.split(other_key + ":")[0]

                with st.expander(title):
                    if "QUERY" in key or "VALIDATION" in key:
                        st.code(content.strip(), language="sql")
                    else:
                        st.write(content.strip())

# Query History
if st.session_state.history:
    st.markdown("### Query History")
    for h in reversed(st.session_state.history[-5:]):
        st.code(h, language="sql")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit + Ollama (phi3) | AI SQL Validation Agent")