import streamlit as st

# 設定網頁標題與圖示
st.set_page_config(page_title="阿瓦隆遊戲助手", page_icon="⚔️", layout="centered")

st.title("🛡️ 阿瓦隆 Avalon 遊戲助手")
st.markdown("---")

# --- Feature 1: 遊戲玩法總覽圖 ---
st.header("1. 遊戲規則總覽")
try:
    st.image("Avalon_infographic_R3.png", caption="阿瓦隆基本規則說明圖")
except:
    st.error("❌ 找不到圖片檔 'Avalon_infographic_R3.png'，請確認檔案在資料夾中。")

st.markdown("---")

# --- Feature 2: 遊戲人數與配置 ---
st.header("2. 角色配置與詳細能力")

# 下拉式選單
player_count = st.selectbox(
    "請選擇遊戲人數：",
    options=[5, 6, 7, 8, 9, 10],
    index=0
)

# 角色配置資料
role_config = {
    5: "梅林、派西維爾、忠臣、莫甘娜、刺客",
    6: "梅林、派西維爾、忠臣x2、莫甘娜、刺客",
    7: "梅林、派西維爾、忠臣x2、莫甘娜、刺客、奧伯倫",
    8: "梅林、派西維爾、忠臣x3、莫甘娜、刺客、爪牙",
    9: "梅林、派西維爾、忠臣x4、莫甘娜、刺客、莫德雷德",
    10: "梅林、派西維爾、忠臣x4、莫甘娜、刺客、奧伯倫、莫德雷德"
}

# 顯示配置框
st.subheader(f"👥 {player_count} 人局角色分配")
st.info(f"**配置清單：**\n{role_config[player_count]}")

# 角色能力說明 (可折疊)
with st.expander("🔍 查看角色能力詳細說明"):
    st.markdown("""
    ### 😇 正義方角色
    * **梅林**：知道壞人是誰，但必須隱藏身份，否則會被刺殺。
    * **派西維爾**：知道梅林和莫甘娜是誰，但不知道誰是誰。
    * **亞瑟的忠臣**：沒有特殊能力，憑邏輯找出隊友。

    ### 😈 邪惡方角色
    * **莫甘娜**：以梅林的形象出現，用來混淆派西維爾。
    * **刺客**：邪惡方最後的反擊機會，若成功指認梅林則邪惡方獲勝。
    * **莫德雷德**：大魔王，不會被梅林知道身份。
    * **奧伯倫**：不知道其他壞人是誰，也不會被其他壞人知道。
    * **邪惡爪牙**：普通的邪惡方成員。
    """)

st.markdown("---")

# --- Feature 3: 語音主持人 ---
st.header("3. 語音主持人")

# MP3 檔案對應
audio_files = {
    5: "Avalon_5_6_Final.mp3",
    6: "Avalon_5_6_Final.mp3",
    7: "Avalon_7_Final.mp3",
    8: "Avalon_8_9_Final.mp3",
    9: "Avalon_8_9_Final.mp3",
    10: "Avalon_10_Final.mp3"
}

st.warning("🔔 所有玩家都確認自己身份後，主持人就可以開始了！")

# 播放按鈕邏輯
if st.button(f"▶️ 播放 {player_count} 人局語音"):
    audio_path = audio_files[player_count]
    try:
        with open(audio_path, 'rb') as f:
            audio_bytes = f.read()
            st.audio(audio_bytes, format='audio/mp3')
            st.success(f"正在播放：{audio_path}")
    except FileNotFoundError:
        st.error(f"❌ 找不到語音檔：{audio_path}，請檢查檔案名稱。")

st.markdown("---")
# --- 修改後的註腳 ---
st.caption("🎙️ 主持人語音由業餘主持人慧蘭真人演繹，並非AI生成。祝你遊戲愉快~~")