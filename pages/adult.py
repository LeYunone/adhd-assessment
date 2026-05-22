import streamlit as st

st.title("👨‍💼 成人 ADHD 评估")
questions = [
    "很难长时间专注于一项任务？",
    "经常丢三落四？",
    "容易分心？",
    "做事拖延、难以开始？",
    "经常打断别人说话？"
]

score = 0
for i, q in enumerate(questions):
    ans = st.radio(f"{i+1}. {q}", ["从不", "偶尔", "经常", "总是"], horizontal=True)
    score += [0,1,2,3][["从不", "偶尔", "经常", "总是"].index(ans)]

if st.button("查看结果"):
    if score >= 14:
        st.error("⚠️ 高度提示 ADHD 倾向，建议就医评估")
    elif score >= 8:
        st.warning("⚠️ 中度倾向，可进一步观察")
    else:
        st.success("✅ 暂无明显 ADHD 倾向")