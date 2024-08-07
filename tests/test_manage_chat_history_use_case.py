from unittest import TestCase

from external_systems.flowiseai import FlowiseAIExternalSystem
from use_cases.manage_chat_history_use_case import ManageChatHistoryUseCase


class TestManageChatHistoryUseCase(TestCase):
    def setUp(self):
        super().setUp()
        self.flowise_external_system = FlowiseAIExternalSystem()

        self.manage_chat_history_use_case = ManageChatHistoryUseCase(
            self.flowise_external_system
        )

    def test_get_chat_history(self):
        self.flowise_external_system.prediction("1", "Hola", [])

        chat_history = self.manage_chat_history_use_case.get_chat_history("1")

        assert isinstance(chat_history, list)
        assert isinstance(chat_history[0], dict)
        assert chat_history[0]["content"] == "Hola"
