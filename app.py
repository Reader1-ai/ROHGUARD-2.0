# -----------------------------------------------------
            # PATH A: GEMINI AI ANALYSIS (WITH STABLE FALLBACKS)
            # -----------------------------------------------------
            if ai_client:
                with st.spinner("🤖 Consulting Gemini AI Engine..."):
                    prompt = f"""
                    You are ROHGUARD 2.0, an advanced cyberbullying, roast, and digital safety AI.
                    Analyze the following input: "{post_draft}"
                    
                    Respond in EXACTLY this format (no extra text):
                    SCORE: [Number from 0 to 100 where 0 is safe/positive and 100 is toxic/severe roast/passive-aggressive]
                    VERDICT: [One short sentence summarizing the safety tone, hidden shade, or risk]
                    FLAGGED: [Comma separated list of toxic words, roasts, or hidden shade phrases, or 'None']
                    COMEBACK: [A witty, polite, non-escalating comeback the user can copy and paste]
                    """

                    response = None
                    active_model_used = None
                    # Stable active production models in the Google GenAI SDK
                    candidate_models = [
                        "gemini-2.5-flash",
                        "gemini-2.0-flash",
                        "gemini-1.5-flash",
                    ]

                    for model_name in candidate_models:
                        try:
                            response = ai_client.models.generate_content(
                                model=model_name,
                                contents=prompt,
                            )
                            if response and response.text:
                                active_model_used = model_name
                                break  # Successfully got response!
                        except Exception:
                            continue  # Try next available model in candidate list

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
