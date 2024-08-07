class ManageChatHistoryUseCase:
    def __init__(self, flowise_external_system):
        self.flowise_external_system = flowise_external_system

    def get_chat_history(self, session_id):
        chat_history = []
        flowise_chat_history = self.flowise_external_system.get_chat_history(session_id)
        for message in flowise_chat_history:
            chat_message = {
                "content": message["content"],
                "role": ("user" if message["role"] == "userMessage" else "assistant"),
            }
            chat_history.append(chat_message)
        return chat_history
