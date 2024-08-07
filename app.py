import streamlit as st

from external_systems.flowiseai import FlowiseAIExternalSystem
from settings import get_settings
from use_cases.manage_chat_history_use_case import ManageChatHistoryUseCase
from use_cases.manage_session_id_use_case import ManageSessionIdUseCase

settings = get_settings()

prompt_disabled = True

prompt_placeholder = "Set an OpenAI API Key first!!!"

manage_session_id_use_case = ManageSessionIdUseCase()

flowise_ai_external_system = FlowiseAIExternalSystem()

manage_chat_history_use_case = ManageChatHistoryUseCase(flowise_ai_external_system)

st.set_page_config(
    page_title=settings.page_title,
    page_icon=settings.page_icon,
    layout=settings.layout,
)

session_id = manage_session_id_use_case.read_session_id()

st.session_state.session_id = session_id

if "chat_history" not in st.session_state:
    try:
        chat_history = manage_chat_history_use_case.get_chat_history(session_id)
        st.session_state.chat_history = chat_history
    except Exception as e:
        st.session_state.chat_history = []
        st.error(str(e))


def delete_chat_history():
    flowise_ai_external_system.delete_chat_history(session_id)
    st.session_state.chat_history = []


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")

    st.button("Clear Chat History", on_click=delete_chat_history)

    if openai_api_key != "":
        prompt_placeholder = "Ask to Weather Chatbot"

        prompt_disabled = False

        flowise_ai_external_system.set_openai_api_key(openai_api_key)

st.title(f"{settings.page_icon} {settings.page_title}")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(prompt_placeholder, disabled=prompt_disabled)

if prompt:
    message = {
        "role": "user",
        "content": prompt,
    }

    st.chat_message("user").markdown(prompt)

    st.session_state.chat_history.append(message)

    try:
        prediction = flowise_ai_external_system.prediction(
            st.session_state.session_id,
            prompt,
            st.session_state.chat_history,
        )

        message = {
            "role": "assistant",
            "content": prediction,
        }

        st.chat_message("assistant").markdown(prediction)

        st.session_state.chat_history.append(message)

    except Exception as e:
        st.error(str(e))
