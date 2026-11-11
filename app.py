# -----------------------------------------------------
            # PATH A: GEMINI AI ANALYSIS (WITH CANDIDATE RETRIES)
            # -----------------------------------------------------
            if ai_client:
                with st.spinner("🤖 Consulting Gemini AI Engine..."):
                    prompt = f"""
                    You are ROHGUARD 2.0, an advanced cyberbullying, roast, and digital safety AI.
                    Analyze the following input: "{post_draft}"
                    
                    Respond in EXACTLY this format (no extra markdown outside this structure):
                    SCORE: [Number from 0 to 100 where 0 is safe/positive and 100 is toxic/severe roast/passive-aggressive]
                    VERDICT: [One short sentence summarizing the safety tone, hidden shade, or risk]
                    FLAGGED: [Comma separated list of toxic words, roasts, or hidden shade phrases, or 'None']
                    COMEBACK: [A witty, polite, non-escalating comeback the user can copy and paste]
                    """

                    response = None
                    candidate_models = [
                        "gemini-3.8-flash",
                        "gemini-2.5-flash",
                        "gemini-1.5-flash",
                    ]

                    for model_name in candidate_models:
                        try:
                            res = ai_client.models.generate_content(
                                model=model_name,
                                contents=prompt,
                            )
                            if res and res.text:
                                response = res
                                active_model_used = model_name  # Save active model name!
                                break
                        except Exception:
                            continue

                    if response and response.text:
                        raw_text = response.text

                        score_match = re.search(r"SCORE:\s*(\d+)", raw_text)
                        verdict_match = re.search(r"VERDICT:\s*(.*)", raw_text)
                        flagged_match = re.search(r"FLAGGED:\s*(.*)", raw_text)
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
                            else "Keep it positive!"
                        )

                        latency = round((time.time() - start_time) * 1000, 2)
                        ai_used = True
                    else:
                        ai_used = False

            # -----------------------------------------------------
            # PATH B: LOCAL RULE ENGINE (FALLBACK)
            # -----------------------------------------------------
            if not ai_used:
                with st.spinner("Scanning via Local Rules Engine..."):
                    time.sleep(0.05)
                    text_lower = post_draft.lower()
                    words = re.findall(r"\b\w+\b", text_lower)

                    matched_pos = [w for w in words if w in POSITIVE_WORDS]
                    matched_neg = [w for w in words if w in MODERN_TOXIC_TERMS]
                    matched_phrases = [
                        p for p in MODERN_ROAST_PHRASES if p in text_lower
                    ]
                    matched_back = [
                        p for p in BACKHANDED_PHRASES if p in text_lower
                    ]

                    all_flagged = list(
                        set(matched_neg + matched_phrases + matched_back)
                    )
                    flagged_str = (
                        ", ".join(all_flagged) if all_flagged else "None"
                    )

                    base_score = 0
                    if matched_back:
                        base_score += len(matched_back) * 40
                    if matched_phrases:
                        base_score += len(matched_phrases) * 35
                    if matched_neg:
                        base_score += len(matched_neg) * 30
                    if matched_pos and not matched_back:
                        base_score -= len(matched_pos) * 15

                    score = max(0, min(99, base_score))

                    # Force minimum warning score if toxic words or roasts are flagged
                    if all_flagged and score < 50:
                        score = 75

                    if matched_back:
                        verdict = (
                            "🎭 Backhanded Compliment Detected! Passive-aggressive"
                            " shade identified."
                        )
                    elif score >= 50:
                        verdict = (
                            "Warning! Toxic terms or roasts detected in draft."
                        )
                    elif matched_pos and score < 30:
                        verdict = "Splendid! Safe and positive message."
                    else:
                        verdict = "Neutral content detected."

                    comeback = random.choice(COMEBACK_TEMPLATES)
                    latency = round((time.time() - start_time) * 1000, 2)
