import streamlit as st
import random

st.title("Number Guessing Game")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

guess = st.number_input("Enter number (1-100)", min_value=1, max_value=100)

if st.button("Check"):
    st.session_state.attempts += 1

    if guess > st.session_state.number:
        st.warning(" Too High!")
    elif guess < st.session_state.number:
        st.warning(" Too Low!")
    else:
        st.success(f" Correct! Attempts: {st.session_state.attempts}")

if st.button("Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.info("Game Restarted!")