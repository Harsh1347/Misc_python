from speech import search_word,get_meaning
import tkinter as tk 
import streamlit as st

st.title("word meaning")

if st.button("Say a word"):
    st.text("Listening...")
    word = search_word()
    st.text(f"You said : {word}")
    st.write(get_meaning(word))