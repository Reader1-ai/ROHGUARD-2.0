import datetime
import random
import re
import time
from google import genai
import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION & AI INITIALIZATION
# =========================================================
st.set_page_config(
    page_title="ROHGUARD 2.0",
    page_icon="🛡️",
    layout="wide",
)

st.sidebar.markdown("# 🛡️ ROHGUARD 2.0")
st.sidebar.caption("Digital Defense Suite - Tech Fair MVP")

# Initialize Gemini Client if GEMINI_API_KEY is present in Streamlit Secrets
ai_client = None
if "GEMINI_API_KEY" in st.secrets:
    try:
        ai_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        st.sidebar.success("🤖 Gemini AI Engine: ONLINE")
    except Exception as e:
        st.sidebar.warning("⚠️ AI Key Error. Running in Local Engine Mode.")
else:
    st.sidebar.info("💡 Local Engine Mode (Add GEMINI_API_KEY to activate AI)")

# Fallback Rule Lists for Offline / Local Operation
POSITIVE_WORDS = {
    "awesome",
    "amazing",
    "brilliant",
    "brave",
    "caring",
    "creative",
    "friendly",
    "funny",
    "generous",
    "great",
    "helpful",
    "honest",
    "kind",
    "legend",
    "nice",
    "polite",
    "smart",
    "sweet",
    "talented",
    "wonderful",
    "thoughtful",
    "supportive",
    "inspiring",
    "respectful",
    "welcoming",
    "clever",
    "goat",
    "w",
    "slay",
    "valid",
    "wholesome",
}

MODERN_TOXIC_TERMS = {
    "ugly",
    "fat",
    "gross",
    "smelly",
    "weird",
    "skinny",
    "nasty",
    "rude",
    "mean",
    "fake",
    "annoying",
    "obnoxious",
    "lazy",
    "clueless",
    "cringe",
    "lame",
    "boring",
    "loud",
    "bossy",
    "greedy",
    "selfish",
    "horrible",
    "terrible",
    "awful",
    "useless",
    "dumb",
    "stupid",
    "idiot",
    "slow",
    "worst",
    "sucks",
    "fail",
    "loser
