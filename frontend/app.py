import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/v1/explain"

st.set_page_config(page_title="Financial Explainer", layout="wide")

st.title("Context-Aware Financial Concept Explanation System")
st.subheader("Educational & Non-Advisory")

with st.sidebar:
    st.header("Financial Context")

    income = st.number_input("Monthly Income", min_value=0.0)
    savings = st.number_input("Total Savings", min_value=0.0)
    loans = st.number_input("Total Loans", min_value=0.0)
    goals = st.text_input("Financial Goals")

query = st.text_area("Ask a financial question:")

if st.button("Explain"):

    payload = {
        "user_id": "user_1",
        "query": query,
        "context": {
            "income": income,
            "savings": savings,
            "loans": loans,
            "goals": goals
        }
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        data = response.json()

        if data["advisory_blocked"]:
            st.error("Advisory request detected. Educational explanation only.")

        st.markdown("### Explanation")
        st.write(data["explanation"])

        if data["assumptions"]:
            st.markdown("### Assumptions")
            for item in data["assumptions"]:
                st.write(f"- {item}")

        if data["risks"]:
            st.markdown("### Risks")
            for item in data["risks"]:
                st.write(f"- {item}")

        if data["sources"]:
            st.markdown("### Sources")
            for item in data["sources"]:
                st.write(f"- {item}")
    else:
        st.error("Backend error.")