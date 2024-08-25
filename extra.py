# Authenticator imports
import pickle4 as pickle
from pathlib import Path
import streamlit_authenticator as stauth

# -- USER AUTHENTICATION --
names = ["MORE Electric and Power Corporation", "Niel Parcon", "Roel Castro"]
usernames = ["more", "nparcon", "rcastro"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                    "mepc_energy_trading_dashboard", "morepower", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Wrong username/password!")

# Yellow warning box
if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

authenticator.logout("Logout", "main")