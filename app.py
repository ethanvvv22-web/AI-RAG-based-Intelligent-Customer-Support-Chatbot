import time

import streamlit as st
from agent.react_agent import ReactAgent
st.set_page_config(page_title="AI Customer Service", layout="centered")
st.markdown("""
<style>

/* 页面背景 */
.stApp {
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
}

/* 标题 */
h1 {
    text-align: center;
    font-weight: 700;
}

/* 聊天气泡 */
.stChatMessage {
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

/* 用户消息 */
[data-testid="stChatMessage"]:has(div[data-testid="stMarkdownContainer"]:has(p)) {
}

/* 用户 vs AI（颜色区分） */
[data-testid="stChatMessage"][aria-label="user"] {
    background: #4CAF50;
    color: white;
}

[data-testid="stChatMessage"][aria-label="assistant"] {
    background: #f1f5f9;
    color: black;
}

/* 输入框 */
textarea {
    border-radius: 20px !important;
}

</style>
""", unsafe_allow_html=True)
# 标题
st.markdown("## 🤖 AI Customer Service")
st.caption("Ask anything, I will help you 🚀")
st.divider()

if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()

if "message" not in st.session_state:
    st.session_state["message"] = []

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 用户输入提示词
prompt = st.chat_input()

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    response_messages = []
    with st.spinner("Agent is thinking..."):
        res_stream = st.session_state["agent"].execute_stream(prompt)

        def capture(generator, cache_list):

            for chunk in generator:
                cache_list.append(chunk)

                # for char in chunk:
                #     time.sleep(0.0001)
                #     yield char
                yield chunk

        # st.chat_message("assistant").write_stream(capture(res_stream, response_messages))
        # st.session_state["message"].append({"role": "assistant", "content": response_messages[-1]})
        # st.rerun()
        st.chat_message("assistant").write_stream(capture(res_stream, response_messages))

        st.session_state["message"].append({
            "role": "assistant",
            "content": "".join(response_messages)
        })