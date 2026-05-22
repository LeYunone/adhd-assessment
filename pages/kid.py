import streamlit as st

st.title("👶 儿童 ADHD 评估")
questions = [
    "坐不住，小动作多？",
    "容易冲动、打断别人？",
    "注意力不集中？",
    "粗心大意？",
    "难以遵守规则？"
]

score = 0
for i, q in enumerate(questions):
    ans = st.radio(f"{i+1}. {q}", ["没有", "偶尔", "经常"], horizontal=True)
    score += [0,1,2][["没有", "偶尔", "经常"].index(ans)]

if st.button("查看结果"):
    if score >= 8:
        st.error("⚠️ 高度提示 ADHD 倾向，建议就医评估")
    elif score >= 4:
        st.warning("⚠️ 需关注，建议观察")
    else:
        st.success("✅ 暂无明显 ADHD 倾向")