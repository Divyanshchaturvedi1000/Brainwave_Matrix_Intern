import streamlit as st
from password_strength import check_password_strength, character_feedback


# Streamlit setup
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔐 Password Strength Checker with Character Comparison")

# Password input
password = st.text_input("Enter your password", type="password")

# Check strength
if password:
    score, suggestions = check_password_strength(password)

    st.markdown(f"### 🔢 Score: `{score}/100`")
    st.markdown(f"### 🧍 Character Match: **{character_feedback(score)}**")

    if suggestions:
        st.markdown("### 🔧 Suggestions to Improve:")
        for tip in suggestions:
            st.markdown(f"- {tip}")
    else:
        st.success("✅ Excellent! Your password is very strong.")
