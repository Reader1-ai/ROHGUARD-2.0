import datetime
import random
import re
import time
from google import genai
import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION & ROH ENGINE INITIALIZATION
# =========================================================
st.set_page_config(
    page_title="ROHGUARD 2.0",
    page_icon="🛡️",
    layout="wide",
)

st.sidebar.markdown("# 🛡️ ROHGUARD 2.0")
st.sidebar.caption("Digital Defense Suite - Tech Fair MVP")

ai_client = None
if "GEMINI_API_KEY" in st.secrets:
    try:
        ai_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        st.sidebar.success("🤖 ROH Engine: ONLINE")
    except Exception:
        st.sidebar.warning("⚠️ API Key Error. Running in Local Mode.")
else:
    st.sidebar.info("💡 Local Mode (Add API Key to activate ROH Engine)")

# =========================================================
# 2. LOCAL HEURISTIC DICTIONARIES & TEMPLATES
# =========================================================
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
    "loser",
    "trash",
    "garbage",
    "cooked",
    "ratio",
    "opp",
    "opps",
    "snitch",
    "canceled",
    "cap",
    "bozo",
    "npc",
    "mid",
    "flop",
    "skibidi",
    "glazing",
    "glaze",
    "unreal",
    "delusional",
    "bum",
    "clown",
    "chopped",
    "karen",
    "simp",
    "bot",
    "washed",
}

MODERN_ROAST_PHRASES = [
    "touch grass",
    "side eye",
    "crash out",
    "rage bait",
    "skill issue",
    "fatherless",
    "zero rizz",
    "no rizz",
    "room temp iq",
    "who asked",
