import re 
import streamlit as st

#page layout
st.set_page_config(page_title = "Password Checker", page_icon = "🔐", layout = "centered") 

# Custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !importent; margin: auto;}
    .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px; }
    .stButton button:hover {background-color:red ; color: white;}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your Password below to check security level. 🔍") 

# Function to check password Strength
def check_password_strength(password):
    score = 0
    feedback = []
     
    # Length Check
    if len(password) >=8:
        score += 1  # Icreasde sxore by one
    else:
        feedback.append("❌ Password should be **at least 8 character long**. ")

    # Upper & Lower case Check
    if re.search(r"[A-z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both upper (A-Z) and lower (a-z) laters.**")

    # Digit Chek
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one numbers (0-9)**")

    #Special character
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special  character (!@#$%^&*)**" )

    # Strength rating
    if score == 4:
        st.success("✅ ** Strong Password** Your password is secure")
    elif score == 3:
        st.info("⚠️ ** Moderate Password** Consider improving security by adding more feature")
    else:
        st.error("❌ **Weak Password** Follow the suggested below to strength it")

    # Feedback
    if feedback:
        with st.expander("🔍 **Improve your Password** "):
            for item in feedback:
                st.write(item)

# Get userr input
password = st.text_input("Enter your Password: ", type = "password", help = "Ensure your password is strong 🔐")

# Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password) 
    else:
        st.warning("⚠️ Please enter a password first!") # show warning if password empty




