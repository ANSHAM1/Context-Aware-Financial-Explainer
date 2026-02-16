def generate_explanation(query: str, context: dict) -> dict:
    explanation = f"""
This is an educational explanation about: {query}

Based on your provided financial context:
Income: {context.get("income")}
Savings: {context.get("savings")}
Loans: {context.get("loans")}
Goals: {context.get("goals")}

This explanation is for educational purposes only.
"""

    return {
        "explanation": explanation.strip(),
        "assumptions": [
            "User-provided financial data is accurate.",
            "No additional liabilities were provided."
        ],
        "risks": [
            "Financial concepts may vary based on regulation changes.",
            "Individual circumstances may alter applicability."
        ],
        "sources": [
            "RBI Financial Literacy Portal",
            "SEBI Education Booklet"
        ]
    }