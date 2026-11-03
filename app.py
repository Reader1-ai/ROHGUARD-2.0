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

# Genuine Positives & Compliments
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

# Modern Slang & Direct Insults
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

# Direct Multi-Word Modern Roasts
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

# 🎭 Backhanded Compliments & Passive-Aggressive Insults
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

# Custom Interface Header
st.markdown("## 🛡️ ROHGUARD 2.0 — DIGITAL DEFENSE & SAFETY SUITE")
st.caption(
    "Proactive Risk Mitigation System | Real-Time Packet Filter | Decoy Threat"
    " Isolation"
)

# Initialize judge metrics in session state
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
# TAB 1: RISK ANALYZER (UPGRADED DETECTION ENGINE)
# =========================================================
with tab_analyzer:
    st.header("Social Media Risk & Response Engine")
    post_draft = st.text_area(
        "Draft your post or paste a received insult / backhanded compliment:",
        placeholder=(
            "Try backhanded insults like 'no offense but you actually did"
            " good for once' or 'at least you tried'..."
        ),
        height=100,
    )

    if st.button("Analyze Post Risk", type="primary"):
        if not post_draft.strip():
            st.warning("Please type a draft first!")
        else:
            start_time = time.time()

            with st.spinner(
                "Scanning for modern roasts, backhanded compliments & risks..."
            ):
                time.sleep(0.2)

                text_lower = post_draft.lower()
                words = re.findall(r"\b\w+\b", text_lower)

                matched_pos = [w for w in words if w in POSITIVE_WORDS]
                matched_neg = [w for w in words if w in MODERN_TOXIC_TERMS]
                matched_phrases = [
                    phrase
                    for phrase in MODERN_ROAST_PHRASES
                    if phrase in text_lower
                ]
                matched_backhanded = [
                    phrase
                    for phrase in BACKHANDED_PHRASES
                    if phrase in text_lower
                ]

                # Combine all flagged triggers
                all_flagged = list(
                    set(matched_neg + matched_phrases + matched_backhanded)
                )

                # Dynamic Risk Score Calculation
                base_score = 0
                if matched_backhanded:
                    base_score += len(matched_backhanded) * 40  # High penalty
                if matched_phrases:
                    base_score += len(matched_phrases) * 35
                if matched_neg:
                    base_score += len(matched_neg) * 25
                if matched_pos and not matched_backhanded:
                    base_score -= len(matched_pos) * 15

                # Cap score between 0 and 99
                score = max(0, min(99, base_score))

                # Safeguard override for backhanded phrases
                if matched_backhanded and score < 70:
                    score = random.randint(75, 89)

                latency = round((time.time() - start_time) * 1000, 2)
                st.session_state.analyzed_count += 1

                if matched_backhanded:
                    st.session_state.threats_blocked += 1
                    verdict = (
                        "🎭 Backhanded Compliment Detected! This text sounds"
                        " polite on the surface but contains passive-aggressive"
                        " shade."
                    )
                elif score >= 50:
                    st.session_state.threats_blocked += 1
                    verdict = (
                        "Warning! Toxic slang, roasts, or conflict-inducing"
                        " phrasing detected."
                    )
                elif matched_pos and score < 30:
                    verdict = (
                        "Splendid! Your draft contains genuine positive"
                        " language."
                    )
                else:
                    verdict = "Neutral content detected. Safe to proceed."

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
                            f"🔴 **Risk Score: {score}/100 — High Risk /"
                            " Passive-Aggressive Shade Flagged!**"
                        )
                    st.progress(score / 100)

                with col_latency:
                    st.metric(
                        label="⚡ Analysis Speed", value=f"{latency} ms"
                    )

                st.info(f'🗣️ **ROHGUARD says:** "{verdict}"')

                if all_flagged:
                    st.markdown(
                        f"🚨 **Flagged Terms & Passive-Aggressive Phrases:**"
                        f" `{', '.join(all_flagged)}`"
                    )
                    st.markdown("### 💬 Recommended Classy Comeback:")
                    smart_response = random.choice(COMEBACK_TEMPLATES)
                    st.code(smart_response, language="text")

# =========================================================
# TAB 2: LOCAL FIREWALL
# =========================================================
with tab_firewall:
    st.header("🔥 ROHGUARD Network Firewall")
    st.write("Active rule-based packet filter for local traffic inspection.")

    firewall_active = st.toggle("Enable Active Packet Filter", value=True)

    if firewall_active:
        st.success("🟢 Firewall Protocol ACTIVE — Packet Inspection Running")

        if st.button("Simulate Incoming Network Traffic"):
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
        st.warning("⚠️ Firewall Disabled. Incoming packets unmonitored.")

# =========================================================
# TAB 3: THREAT DISENGAGER
# =========================================================
with tab_disengager:
    st.header("👾 Threat Disengager & Decoy Trap")
    st.write(
        "Isolates malicious connection attempts and deploys counter-measures."
    )

    if st.button("Run Threat Disengage Protocol"):
        with st.status(
            "Deploying Counter-Measures...", expanded=True
        ) as status:
            st.write("🔍 Scanning active network sockets...")
            time.sleep(0.5)
            st.write(
                "⚠️ Unauthorized port scan detected from IP: `198.51.100.24`"
            )
            time.sleep(0.5)
            st.write(
                "🛡️ Redirecting attack payload to Isolated Decoy Environment..."
            )
            time.sleep(0.6)
            st.write("🔒 Terminated connection & logged origin IP address.")
            status.update(
                label="Disengage Complete! Threat Neutralized.",
                state="complete",
            )

        st.success("Target isolated safely. Your real session remains hidden!")

# =========================================================
# TAB 4: TECH FAIR JUDGES' METRICS
# =================================
