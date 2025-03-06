# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")

# genai.configure(api_key=API_KEY)

# model = genai.GenerativeModel("models/gemini-1.5-flash")

# response = model.generate_content("what is the capital of belgium?")

# st.write(response.text.strip())




import re
import streamlit as st
import random
import string

def generate_strong_password(length=12):
    """Generate a strong password with a mix of characters."""
    if length < 8:
        st.warning("Password length should be at least 8 characters.")
        return None
    
    # Ensure the password contains at least one of each required character type
    password = [
        random.choice(string.ascii_uppercase),  # At least one uppercase
        random.choice(string.ascii_lowercase),  # At least one lowercase
        random.choice(string.digits),           # At least one digit
        random.choice("!@#$%^&*")                # At least one special character
    ]
    
    # Fill the rest of the password length with random choices
    password += random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=length-4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")
        for suggestion in feedback:
            st.write(suggestion)

# Streamlit user interface
st.title("Password Strength Meter")
user_password = st.text_input("Enter your password:", type="password")
if st.button("Check Password Strength"):
    check_password_strength(user_password)

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    if strong_password:
        st.write(f"Suggested Strong Password: **{strong_password}**")



