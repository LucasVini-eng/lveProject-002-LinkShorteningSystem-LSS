import streamlit as st
import pyshorteners
import validators
import time
from urllib.parse import urlparse

st.set_page_config(
    page_title="Link Shortening System - LSS",
    page_icon="🔗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def load_css(path_css):
    try:
        with open(path_css, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass
load_css("css/style.css")

with st.sidebar:
    st.image(
        "assests/icons/profile.jpeg",
        width=50
    )
    st.subheader("Lucas Vinicius")
    st.subheader("Software & Data Engineer")
    st.divider()
    st.info("💡 This project demonstrates best practices in data validation, link security analysis, and an intuitive user interface.")

st.title("🔗 Link Shortening System (LSS)")
st.write("Enter your long URL below, click “Check,” and securely generate a shortened link.")

long_url = st.text_input("Type or paste the long URL:", placeholder="https://example.com/your-long-url")

if "verified_url" not in st.session_state:
    st.session_state.verified_url = False
if "previous_url" not in st.session_state:
    st.session_state.previous_url = ""

if long_url != st.session_state.previous_url:
    st.session_state.verified_url = False
    st.session_state.previous_url = long_url

def check_safety(url):
    parsed = urlparse(url)
    suspicious_words = ["gratis",
                          "ganhe-dinheiro",
                          "brinde",
                          "desconto",
                          "bet",
                          "urgente",
                          "cadastro",
                          "oferta",
                          ".exe",
                          ".bat"]

    if parsed.scheme != "https":
        return False, "Warning: This URL does not use a secure connection (HTTPS).(u_U)"
    for term in suspicious_words:
        if term in url.lower():
            return False, f"Warning: The URL contains terms frequently associated with threats ('{term}').(u_U)"
    return True, "The URL appears to be safe to shorten.✅"

btn_check = st.button("Check URL")

if btn_check:
    if not long_url:
        st.warning("⚠️ Please, enter a URL before checking.")
    else:
        is_valid = validators.url(long_url)

        if not is_valid:
            st.error("❌ Error: Please enter a valid URL (be sure to include “http://” or “https://”).(u_U)")
            st.session_state.verified_url = False
        else:
            safe, safety_message = check_safety(long_url)

            if safe:
                st.success("✨ URL in a valid format!")
                st.info(f"🛡️ Safety: {safety_message}")
                st.session_state.verified_url = True
            else:
                st.warning(f"⚠️ {safety_message}")
                st.error("The system blocked the shortening for security reasons.")
                st.session_state.verified_url = False

if st.session_state.verified_url:
    st.write("---")
    if st.button("Shorten URL", type="primary"):
        with st.spinner("Generating Your New Shortened URL..."):
            try:
                time.sleep(1.5)
                s = pyshorteners.Shortener()
                url_shorten = s.tinyurl.short(long_url)

                st.success("✅ URL successfully shortened!")
                st.code(url_shorten, language="text")
                st.markdown(f"[Click here to access the shortened link]({url_shorten})")

            except Exception as e:
                st.error(f"Error while trying to shorten the URL: {e}")