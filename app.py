import datetime
import random
import re
import time
import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="ROHGUARD 2.0",
    page_icon="🛡️",
    layout="wide",
)

st.sidebar.markdown("# 🛡️ ROHGUARD 2.0")
st.sidebar.caption("Digital Defense Suite - Tech Fair MVP")

# Modern Positives & Compliments
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

# Modern Slang, Insults & Toxic Words
MODERN_TOXIC_TERMS = {
    # Classic insults
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
    # Modern online roasts & slang
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
    "bUM",
    "clown",
    "chopped",
    " Karen",
    "simp",
    "bot",
    "washed",
}

# Multi-Word Modern
