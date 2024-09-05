import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["MORE Electric and Power Corporation", "Niel Parcon", "Roel Castro"]
usernames = ["more", "nparcon", "rcastro"]
passwords = ["morepower2019", "morepower2019", "morepower2019"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)