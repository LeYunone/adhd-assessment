import streamlit as st

# 页面配置
st.set_page_config(
    page_title="ADHD 评估工具",
    page_icon="🧠",
    layout="wide"
)

# 标题
st.title("🧠 ADHD 注意力缺陷多动障碍 评估工具")
st.markdown("---")

# 分栏
col1, col2 = st.columns(2)

with col1:
    st.subheader("👨‍💼 成人 ADHD 评估 (ASRS v1.1)")
    st.info("世界卫生组织 WHO 官方标准量表")
    if st.button("开始成人评估", type="primary", use_container_width=True):
        st.switch_page("pages/adult.py")

with col2:
    st.subheader("👶 儿童 ADHD 评估 (SNAP-IV)")
    st.info("DSM-5 标准儿童多动/注意力筛查量表")
    if st.button("开始儿童评估", type="primary", use_container_width=True):
        st.switch_page("pages/kid.py")

# 说明
st.markdown("---")
st.markdown("""
### 📌 重要说明
- 本工具仅用于**初步筛查**，不能替代专业诊断
- 若结果异常，请前往医院精神科/心理科就诊
- 所有题目和评分标准均来自公开医学指南
""")
