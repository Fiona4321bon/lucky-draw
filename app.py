import streamlit as st
import random
import time

st.set_page_config(page_title="班級抽獎系統", page_icon="🎁", layout="centered")

# 獎項與圖片連結、機率
prizes = [
    {"name": "🧃 鋁箔包飲料一包", "weight": 20, "image": "https://i.imgur.com/JvS6PXL.png"},
    {"name": "🥤 小汽水一罐", "weight": 16, "image": "https://i.imgur.com/h0VZyCe.png"},
    {"name": "✨ 文具小福袋", "weight": 13, "image": "https://i.imgur.com/jPgJ7Cr.png"},
    {"name": "✏️ 可愛擦擦樂", "weight": 12, "image": "https://i.imgur.com/qn06D0d.png"},
    {"name": "💌 老師手寫加油卡", "weight": 10, "image": "https://i.imgur.com/sQxgFc1.png"},
    {"name": "➕ 集點再加1點卡", "weight": 9, "image": "https://i.imgur.com/bZIDyEq.png"},
    {"name": "👯 幸運雙人抽獎卡", "weight": 7, "image": "https://i.imgur.com/jKwQZvk.png"},
    {"name": "📝 明日作業加分券", "weight": 6, "image": "https://i.imgur.com/DKPyiPa.png"},
    {"name": "🚪 下課優先出門卡", "weight": 6, "image": "https://i.imgur.com/Mn37D0r.png"},
    {"name": "❌ 免寫訂正卷卡", "weight": 1, "image": "https://i.imgur.com/SXJ99Ab.png"}
]

st.title("🎁 詠芳老師的幸運轉盤抽獎系統")
st.markdown("每累積 10 點就能抽一次，快來看看你的幸運吧！")

# 播放音效
def play_sound():
    st.audio("https://www.soundjay.com/button/beep-07.wav", autoplay=True)

if st.button("🎉 開始抽獎！"):
    with st.spinner("抽獎中，轉盤轉轉轉..."):
        time.sleep(2)
    weighted_list = []
    for prize in prizes:
        weighted_list.extend([prize] * prize["weight"])
    result = random.choice(weighted_list)
    st.success(f"🎊 恭喜你抽中：{result['name']}")
    st.image(result["image"], caption=result["name"], use_column_width=True)
    play_sound()

with st.expander("📋 查看所有獎項與中獎機率"):
    for p in prizes:
        st.markdown(f"**{p['name']}** – 機率：{p['weight']}%")
        st.image(p["image"], width=100)
