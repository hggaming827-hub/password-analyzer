import re
import streamlit as st  # Web interface banane ke liye module

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8: score += 1
    else: feedback.append("❌ Password ki length kam se kam 8 characters honi chahiye.")

    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("❌ Password mein kam se kam ek Uppercase letter (A-Z) hona chahiye.")

    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("❌ Password mein kam se kam ek Lowercase letter (a-z) hona chahiye.")

    if re.search(r"\d", password): score += 1
    else: feedback.append("❌ Password mein kam se kam ek Number (0-9) hona chahiye.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>_+-]", password): score += 1
    else: feedback.append("❌ Password mein kam se kam ek Special Character (!@#$) hona chahiye.")

    if score <= 2: return "WEAK (Bohot Kamzoor) 🔴", feedback, "red"
    elif score <= 4: return "MEDIUM (Theek-Thaak) 🟡", feedback, "orange"
    else: return "STRONG (Mazboot) 🟢", feedback, "green"

# --- WEB PAGE DESIGN ---
st.set_page_config(page_title="Password Analyzer", page_icon="🔒", layout="centered")

st.title("🔒 Cyber Security: Password Analyzer")
st.write("Apna password check karne ke liye neeche enter karein:")

# Web Input Box (Password characters ko chhupane ke liye type="password" lagaya hai)
user_password = st.text_input("Enter Password Here", type="password")

if user_password:
    # Function ko call kiya aur result liya
    strength, feedback_list, color = analyze_password(user_password)
    
    st.subheader("Result:")
    # Alag-alag color box mein strength dikhane ke liye
    if color == "red": 
        st.error(f"Password Strength: {strength}")
    elif color == "orange": 
        st.warning(f"Password Strength: {strength}")
    else: 
        st.success(f"Password Strength: {strength}")

    # Suggestions dikhane ke liye
    if feedback_list:
        st.write("### 💡 Password ko strong banane ke liye sujhaav:")
        for tip in feedback_list:
            st.write(tip)
    else:
        st.balloons() # Ek mazaadar digital balloon animation screen par aayega 🎉
        st.write("🎉 Badhai ho! Aapka password cyber attacks se surakshit hai.")