import streamlit as st

# Page setup
st.set_page_config(page_title="Smart Code Reviewer", page_icon="💻")

# Title
st.title("💻 Smart Code Reviewer")
st.write("Analyze your code for time complexity and performance issues.")

# File upload
uploaded_file = st.file_uploader("📂 Upload your code file", type=["txt", "py", "cpp", "java"])

# OR manual input
code = st.text_area("📌 Or paste your code here:", height=200)

# If file uploaded → override code
if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")

# Button
if st.button("🚀 Analyze Code"):

    if code.strip() == "":
        st.warning("⚠ Please provide code (upload or paste).")
    else:
        # Count loops
        loops = code.lower().count("for") + code.lower().count("while")

        # Complexity logic
        if loops == 0:
            complexity = "O(1)"
        elif loops == 1:
            complexity = "O(n)"
        elif loops == 2:
            complexity = "O(n^2)"
        else:
            complexity = f"O(n^{loops})"

        # Show results
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
            st.info("Your code is efficient. Good job!")

        # Extra checks
        if "def" in code:
            st.warning("⚠ Recursion detected — check stack usage")

        if code.count("\n") > 20:
            st.warning("⚠ Code is too long — consider breaking into functions")
