import streamlit as st
import requests

TOKEN = "7966824165:AAGE0DKosxtuPCMoLWxcGGTlME74xMnhvwU"
CHAT_ID = "417002195"
BOT_USERNAME = "@Goldtrigger2025_bot"

st.set_page_config(page_title="تست ربات تلگرام", layout="centered")
st.title("🤖 تست اتصال ربات تلگرام")
st.markdown(f"ربات شما: [{BOT_USERNAME}](https://t.me/{BOT_USERNAME[1:]})")

if st.button("📩 ارسال پیام تستی"):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "✅ تست موفق! ربات Goldtrigger2025 فعال و آماده ارسال هشدار است."
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        st.success("پیام با موفقیت ارسال شد ✅")
    else:
        st.error("❌ ارسال پیام با خطا مواجه شد")
