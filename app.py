import streamlit as st

# Page config
st.set_page_config(page_title="Smart Code Reviewer", page_icon="💻", layout="centered")

# Title
st.title("💻 Smart Code Reviewer")
st.markdown("Analyze your code for **time complexity**, issues, and improvements.")

# Input box
code = st.text_area("📌 Paste your code below:", height=200)

# Button
if st.button("🚀 Analyze Code"):

    if code.strip() == "":
        st.warning("⚠ Please paste some code first.")
    else:
        loops = code.lower().count("for") + code.lower().count("while")

        # Complexity logic
        if loops == 0:
            complexity = "O(1)"
        elif loops == 1:
            complexity = "O(n)"
        elif loops == 2:
            complexity = "O(n²)"
        else:
            complexity = f"O(n^{loops})"

        # Results section
        st.markdown("---")
        st.subheader("📊 Analysis Result")

        col1, col2 = st.columns(2)
        col1.metric("Loops Found", loops)
        col2.metric("Time Complexity", complexity)

        # Issues
        st.markdown("### ⚠ Issues")
        if loops >= 2:
            st.error("Nested loops detected (high complexity)")
        else:
            st.success("No major performance issues")

        # Suggestions
        st.markdown("### 💡 Suggestions")
        if loops >= 2:
            st.info("Try optimizing using better data structures (e.g., HashMap, Sets)")
        else:
            st.info("Code is efficient. Keep it up!")

        # Extra checks
        if "def" in code:
            st.warning("⚠ Recursion detected — check stack usage")

        if code.count("\n") > 20:
            st.warning("⚠ Code is too long — consider breaking into functions")