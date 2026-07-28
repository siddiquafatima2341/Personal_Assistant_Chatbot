import json
import streamlit as st

# --- Load knowledge base ---
with open("responses.json", "r") as f:
    RESPONSES = json.load(f)


def get_response(user_input: str) -> str:
    text = user_input.lower().strip()
    if text in RESPONSES:
        return RESPONSES[text]
    for key in RESPONSES:
        if key != "default" and key in text:
            return RESPONSES[key]
    return RESPONSES["default"]


# --- Streamlit UI ---
st.set_page_config(page_title="Personal Assistant", page_icon="🤖")
st.title("🤖 Personal Assistant Chatbot")
st.caption("Simple rule-based chatbot powered by Python + JSON + Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your personal assistant. Type 'help' to see what I can do."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    reply = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

with st.sidebar:
    st.header("Options")
    if st.button("Clear chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Chat cleared. How can I help you?"}
        ]
        st.rerun()
    st.markdown("---")
    st.markdown("Edit `responses.json` to add or change replies.")
