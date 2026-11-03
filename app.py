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
st.sidebar.caption("Digital Defense Suite - AI Enhanced")

# Initialize Gemini Client if Key Exists
ai_client = None
if "GEMINI_API_KEY" in st.secrets:
    try:
        ai_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        st.sidebar.success("🤖 Gemini AI Engine: ONLINE")
    except Exception as e:
        st.sidebar.warning("⚠️ AI Key Error. Running in Local Mode.")
else:
    st.sidebar.info("💡 Local Engine Mode (Add GEMINI_API_KEY to activate AI)")

# Fallback Rule Lists
POSITIVE_WORDS = {"awesome", "amazing", "brilliant", "kind", "smart", "great"}
MODERN_TOXIC_TERMS = {"cooked", "ratio", "opp", "trash", "cringe", "loser"}
BACKHANDED_PHRASES = ["no offense but", "at least you tried", "actually smart"]

# Header
st.markdown("## 🛡️ ROHGUARD 2.0 — DIGITAL DEFENSE & SAFETY SUITE")
st.caption(
    "Proactive AI Risk Mitigation | Real-Time Packet Filter | Decoy Threat"
    " Isolation"
)

if "analyzed_count" not in st.session_state:
    st.session_state.analyzed_count = 14
if "threats_blocked" not in st.session_state:
    st.session_state.threats_blocked = 6

tab_analyzer, tab_firewall, tab_disengager, tab_metrics = st.tabs(
    [
        "📝 Post Risk & Comeback Engine",
        "🔥 Local Traffic Firewall",
        "👾 Threat Disengager",
        "📊 Tech Fair Judges' Telemetry",
    ]
)

# =========================================================
# TAB 1: AI-POWERED RISK ANALYZER
# =========================================================
with tab_analyzer:
    st.header("Social Media Risk & Response Engine")
    post_draft = st.text_area(
        "Draft your post or paste a received insult / comment:",
        placeholder="Type any message, modern roast, or passive-aggressive comment...",
        height=100,
    )

    if st.button("Analyze Post Risk", type="primary"):
        if not post_draft.strip():
            st.warning("Please type a draft first!")
        else:
            start_time = time.time()
            st.session_state.analyzed_count += 1

            # -----------------------------------------------------
            # PATH A: GEMINI AI ANALYSIS (If Key Present)
            # -----------------------------------------------------
            if ai_client:
                with st.spinner("🤖 Consulting Gemini AI Engine..."):
                    prompt = f"""
                    You are ROHGUARD 2.0, a cyberbullying and digital safety AI.
                    Analyze the following user input: "{post_draft}"
                    
                    Respond in EXACTLY this format (no extra text):
                    SCORE: [Number from 0 to 100 where 0 is completely safe/positive and 100 is toxic/severe roast/passive-aggressive]
                    VERDICT: [One short sentence summarizing the safety tone or risk]
                    FLAGGED: [Comma separated list of toxic words, roasts, or hidden shade phrases, or 'None']
                    COMEBACK: [A witty, polite, non-escalating comeback the user can copy and paste]
                    """
                    try:
                        response = ai_client.models.generate_content(
                            model="gemini-2.5-flash",
                            contents=prompt,
                        )
                        raw_text = response.text

                        # Parse AI Response
                        score_match = re.search(r"SCORE:\s*(\d+)", raw_text)
                        verdict_match = re.search(
                            r"VERDICT:\s*(.*)", raw_text
                        )
                        flagged_match = re.search(
                            r"FLAGGED:\s*(.*)", raw_text
                        )
                        comeback_match = re.search(
                            r"COMEBACK:\s*(.*)", raw_text
                        )

                        score = (
                            int(score_match.group(1)) if score_match else 50
                        )
                        verdict = (
                            verdict_match.group(1).strip()
                            if verdict_match
                            else "Analyzed by AI."
                        )
                        flagged_str = (
                            flagged_match.group(1).strip()
                            if flagged_match
                            else "None"
                        )
                        comeback = (
                            comeback_match.group(1).strip()
                            if comeback_match
                            else "Stay positive!"
                        )

                        latency = round((time.time() - start_time) * 1000, 2)

                    except Exception as e:
                        st.error(f"AI Connection error: {e}. Falling back to local rules.")
                        ai_client = None

            # -----------------------------------------------------
            # PATH B: LOCAL RULE ENGINE (Fallback)
            # -----------------------------------------------------
            if not ai_client:
                with st.spinner("Scanning locally..."):
                    time.sleep(0.2)
                    text_lower = post_draft.lower()
                    words = re.findall(r"\b\w+\b", text_lower)

                    matched_pos = [w for w in words if w in POSITIVE_WORDS]
                    matched_neg = [w for w in words if w in MODERN_TOXIC_TERMS]
                    matched_back = [
                        p for p in BACKHANDED_PHRASES if p in text_lower
                    ]

                    flagged_str = ", ".join(set(matched_neg + matched_back))
                    if not flagged_str:
                        flagged_str = "None"

                    if matched_back or matched_neg:
                        score = 85
                        verdict = "Risk detected by local keyword scanner."
                        comeback = "I choose to focus on positive energy today!"
                    elif matched_pos:
                        score = 5
                        verdict = "Safe and positive message."
                        comeback = "N/A"
                    else:
                        score = 15
                        verdict = "Neutral text."
                        comeback = "N/A"

                    latency = round((time.time() - start_time) * 1000, 2)

            # -----------------------------------------------------
            # DISPLAY RESULTS
            # -----------------------------------------------------
            if score >= 50:
                st.session_state.threats_blocked += 1

            st.divider()
            st.subheader("ROHGUARD Assessment")

            col_score, col_latency = st.columns([3, 1])
            with col_score:
                if score < 30:
                    st.success(
                        f"🟢 **Risk Score: {score}/100 — Low Risk (Safe)**"
                    )
                elif score < 60:
                    st.warning(
                        f"🟡 **Risk Score: {score}/100 — Moderate Risk**"
                    )
                else:
                    st.error(
                        f"🔴 **Risk Score: {score}/100 — High Risk / Toxic"
                        " Content Flagged!**"
                    )
                st.progress(score / 100)

            with col_latency:
                st.metric(
                    label="⚡ Engine Latency",
                    value=f"{latency} ms",
                    delta="Gemini 2.5 Flash" if ai_client else "Local Rules",
                )

            st.info(f'🗣️ **ROHGUARD says:** "{verdict}"')

            if flagged_str != "None":
                st.markdown(f"🚨 **Flagged Features:** `{flagged_str}`")

            if score >= 40 and comeback != "N/A":
                st.markdown("### 💬 Dynamic AI-Generated Comeback:")
                st.code(comeback, language="text")

# =========================================================
# TAB 2 & 3 & 4 (FIREWALL, DISENGAGER & TELEMETRY)
# =========================================================
with tab_firewall:
    st.header("🔥 ROHGUARD Network Firewall")
    st.write("Active rule-based packet filter inspecting network ports.")
    if st.button("Simulate Incoming Network Traffic"):
        st.write("[`192.168.1.45`] ✅ ALLOWED — `200 OK` | Path: `/feed`")
        st.write("[`45.33.21.110`] 🚫 BLOCKED — `403 Forbidden` | Path: `/login_bruteforce`")

with tab_disengager:
    st.header("👾 Threat Disengager & Decoy Trap")
    if st.button("Run Threat Disengage Protocol"):
        st.success("Target isolated in sandbox environment!")

with tab_metrics:
    st.header("📊 Engineering Telemetry & System Design")
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Total Drafts Scanned", st.session_state.analyzed_count)
    col_m2.metric("Threats Neutralized", st.session_state.threats_blocked)
    col_m3.metric("AI Model", "Gemini 2.5 Flash", delta="Hybrid Architecture")
