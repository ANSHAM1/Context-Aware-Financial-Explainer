import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-flash-latest")

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

    if not query.strip():
        st.warning("Please enter a question.")
        st.stop()

    prompt = f"""
    You are an educational financial explainer.
    Do NOT provide financial advice.
    Only provide conceptual explanation.

    User Context:
    - Monthly Income: {income}
    - Savings: {savings}
    - Loans: {loans}
    - Goals: {goals}

    User Question:
    {query}

    Output strictly in this format:

    Explanation:
    <detailed explanation>

    Assumptions:
    - assumption 1
    - assumption 2

    Risks:
    - risk 1
    - risk 2

    Sources:
    - general financial knowledge
    """

    with st.spinner("Generating explanation..."):
        response = model.generate_content(prompt)
        output = response.text

    # Simple structured parsing
    sections = output.split("Assumptions:")
    
    explanation_part = sections[0].replace("Explanation:", "").strip()

    assumptions = []
    risks = []
    sources = []

    if len(sections) > 1:
        rest = sections[1]
        parts = rest.split("Risks:")
        assumptions_text = parts[0]

        assumptions = [
            line.strip("- ").strip()
            for line in assumptions_text.split("\n")
            if line.strip().startswith("-")
        ]

        if len(parts) > 1:
            risks_split = parts[1].split("Sources:")
            risks_text = risks_split[0]

            risks = [
                line.strip("- ").strip()
                for line in risks_text.split("\n")
                if line.strip().startswith("-")
            ]

            if len(risks_split) > 1:
                sources = [
                    line.strip("- ").strip()
                    for line in risks_split[1].split("\n")
                    if line.strip().startswith("-")
                ]

    st.markdown("### Explanation")
    st.write(explanation_part)

    if assumptions:
        st.markdown("### Assumptions")
        for item in assumptions:
            st.write(f"- {item}")

    if risks:
        st.markdown("### Risks")
        for item in risks:
            st.write(f"- {item}")

    if sources:
        st.markdown("### Sources")
        for item in sources:
            st.write(f"- {item}")