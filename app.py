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

# Initialize ROH Engine (AI Client) if GEMINI_API_KEY is present in Streamlit Secrets
ai_client = None
if "GEMINI_API_KEY" in st.secrets:
    try:
        ai_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        st.sidebar.success("🤖 ROH Engine: ONLINE")
    except Exception as e:
        st.sidebar.warning("⚠️ API Key Error. Running in Local Mode.")
else:
    st.sidebar.info("💡 Local Mode (Add API Key to activate ROH Engine)")

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
    "nobody asked",
    "bro really thought",
    "blud thought",
    "fell off",
    "cry about it",
    "stay mad",
    "copium",
    "seethe",
    "get a life",
    "shut up",
    "you're bad",
    "ur bad",
    "you suck",
    "ur trash",
]

BACKHANDED_PHRASES = [
    "pretty good for",
    "surprised you knew",
    "actually smart",
    "actually nice",
    "finally got it right",
    "at least you tried",
    "good effort though",
    "for a change",
    "no offense but",
    "with all due respect",
    "bless your heart",
    "brave of you to wear",
    "never thought you could",
    "better than expected from you",
    "you look good today for once",
    "you're actually pretty",
    "surprisingly good",
]

COMEBACK_TEMPLATES = [
    (
        "I appreciate the indirect feedback, but I'm keeping things positive"
        " today!"
    ),
    (
        "That sounded like a compliment on the outside, but I'm stepping away"
        " from passive aggression."
    ),
    (
        "Your opinion has been registered and safely redirected to the void."
        " Have a great day!"
    ),
    "I hope your day gets significantly better from here on out! Best wishes.",
    (
        "Thanks for noticing! Focusing on real growth rather than subtle"
        " shade."
    ),
]

# Header Section
st.markdown("## 🛡️ ROHGUARD 2.0 — DIGITAL DEFENSE & SAFETY SUITE")
st.caption(
    "Proactive ROH Engine Risk Mitigation | Real-Time Packet Filter | Decoy"
    " Threat Isolation"
)

# Initialize judge metrics in session state
if "analyzed_count" not in st.session_state:
    st.session_state.analyzed_count = 14
if "threats_blocked" not in st.session_state:
    st.session_state.th
