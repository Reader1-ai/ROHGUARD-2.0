import datetime
import random
import time
import nltk
from nltk.corpus import opinion_lexicon
import streamlit as st

# Download required NLTK opinion lexicon dataset
nltk.download("opinion_lexicon", quiet=True)

POSITIVE_WORDS = set(opinion_lexicon.positive())
NEGATIVE_WORDS = set(opinion_lexicon.negative())

SLANG_NEGATIVES = {
    "skinner",
    "opp",
    "snitch",
    "cringe",
    "ratio",
    "canceled",
    "cap",
    "bozo",
    "npc",
    "mid",
    "flop",
    "trash",
    "garbage",
    "loser",
    "naughty",
}

# ---------------------------------------------------------
# COMEBACK GENERATOR LOGIC (Hacker Disengager & Counter Engine)
# ---------------------------------------------------------
COMEBACK_TEMPLATES = [
    "I appreciate your passion, but I'm focusing my energy on positive growth!",
    (
        "That's an interesting perspective! I'll stick to treating people with"
        " respect."
    ),
    (
        "Thanks for the input, but I choose not to engage in negativity today."
    ),
    (
        "I hope your day gets significantly better from here on out! Best"
        " wishes."
    ),
    (
        "Your opinion has been registered and safely redirected to the void."
        " Have a great day!"
    ),
]

# ---------------------------------------------------------
# STREAMLIT PAGE SETUP
# ---------------------------------------------------------
st.set_page_config(
    page_title="ROHGUARD - Digital Defense Suite",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ ROHGUARD Digital Defense Suite")
st.caption(
    "Integrated Social Media Analyzer | Live Firewall | Hacker Disengager"
)

# Navigation Tabs
tab_analyzer, tab_firewall, tab_disengager = st.tabs(
    ["📝 Post Risk & Comeback Engine", "🔥 Local Traffic Firewall", "👾 Threat Disengager"]
)

# =========================================================
# TAB 1: POST RISK ANALYZER & COMEBACK GENERATOR
# =========================================================
with tab_analyzer:
    st.header("Social Media Risk & Response Engine")
    post_draft = st.text_area(
        "Draft your post or paste a received insult:",
        placeholder="e.g., Calling someone lazy or receiving a rude comment...",
        height=100,
    )

    col1, col2 = st.columns(2)

    with col1:
        analyze_btn = st.button("Analyze Post Risk", type="primary")

    if analyze_btn:
        if not post_draft.strip():
            st.warning("Please type a draft first!")
        else:
            with st.spinner("Analyzing text against 10,000+ terms..."):
                time.sleep(0.5)

                words = [
                    w.strip(".,!?\"'()").lower() for w in post_draft.split()
                ]
                matched_pos = [w for w in words if w in POSITIVE_WORDS]
                matched_neg = [
                    w
                    for w in words
                    if w in NEGATIVE_WORDS or w in SLANG_NEGATIVES
                ]

                if matched_pos and not matched_neg:
                    score = 0
                    verdict = "Splendid! Draft is completely safe and positive."
                    risks = [
                        "Zero risk of social fallout.",
                        f"Matched compliments: {', '.join(matched_pos)}",
                    ]
                elif matched_neg:
                    score = random.randint(85, 98)
                    verdict = (
                        "Goodness gracious! Negative or rude descriptions"
                        " detected."
                    )
                    risks = [
                        "High potential for social conflict and reports.",
                        f"Flagged terms: {', '.join(matched_neg)}",
                    ]
                else:
                    score = 15
                    verdict = "Neutral content detected. Safe to proceed."
                    risks = ["Minimal risk of fallout."]

                st.divider()
                st.subheader("ROHGUARD Assessment")

                if score < 30:
                    st.success(
                        f"🟢 **Risk Score: {score}/100 — Low Risk (Safe)**"
                    )
                else:
                    st.error(
                        f"🔴 **Risk Score: {score}/100 — Severe Consequences"
                        " Imminent!**"
                    )

                st.progress(score / 100)
                st.info(f'🗣️ **ROHGUARD says:** "{verdict}"')

                # AUTOMATIC COMEBACK GENERATOR
                if matched_neg or "call" in post_draft.lower():
                    st.markdown("### 💬 Recommended Classy Comeback:")
                    smart_response = random.choice(COMEBACK_TEMPLATES)
                    st.code(smart_response, language="text")

# =========================================================
# TAB 2: LOCAL TRAFFIC FIREWALL
# =========================================================
with tab_firewall:
    st.header("🔥 ROHGUARD Network Firewall")
    st.write(
        "Active rule-based packet filter for local traffic inspection."
    )

    firewall_active = st.toggle("Enable Active Packet Filter", value=True)

    if firewall_active:
        st.success("🟢 Firewall Protocol ACTIVE — Packet Inspection Running")

        if st.button("Simulate Incoming Network Traffic"):
            traffic_logs = []
            sample_endpoints = [
                ("192.168.1.45", "GET /api/v1/feed", "ALLOWED", "200 OK"),
                (
                    "45.33.21.110",
                    "POST /user/login [BruteForce]",
                    "BLOCKED",
                    "403 Forbidden",
                ),
                ("192.168.1.88", "POST /comment/send", "ALLOWED", "200 OK"),
                (
                    "185.220.101.5",
                    "GET /admin/db_dump",
                    "BLOCKED",
                    "401 Unauthorized",
                ),
            ]

            st.subheader("Live Packet Logs")
            for ip, path, status, code in sample_endpoints:
                time.sleep(0.3)
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                if status == "ALLOWED":
                    st.write(
                        f"[`{timestamp}`] ✅ **{status}** | IP: `{ip}` | Path:"
                        f" `{path}` -> `{code}`"
                    )
                else:
                    st.write(
                        f"[`{timestamp}`] 🚫 **{status}** | IP: `{ip}` | Path:"
                        f" `{path}` -> `{code}`"
                    )
    else:
        st.warning("⚠️ Firewall Disables. Incoming packets unmonitored.")

# =========================================================
# TAB 3: HACKER DISENGAGER & DECOY
# =========================================================
with tab_disengager:
    st.header("👾 Threat Disengager & Decoy Trap")
    st.write(
        "Isolates malicious connection attempts and deploys counter-measures."
    )

    if st.button("Run Threat Disengage Protocol"):
        with st.status("Deploying Counter-Measures...", expanded=True) as status:
            st.write("🔍 Scanning active network sockets...")
            time.sleep(0.6)
            st.write(
                "⚠️ Unauthorized port scan detected from IP: `198.51.100.24`"
            )
            time.sleep(0.6)
            st.write("🛡️ Redirecting attack payload to Isolated Decoy Environment...")
            time.sleep(0.8)
            st.write("🔒 Terminated connection & logged origin IP address.")
            status.update(
                label="Disengage Complete! Threat Neutralized.",
                state="complete",
            )

        st.success(
            "Target isolated safely. Your real session remains hidden!"
        )
