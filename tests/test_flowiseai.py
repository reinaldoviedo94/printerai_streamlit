from unittest import TestCase

from external_systems.flowiseai import FlowiseAIExternalSystem


class TestFlowiseAIExternalSystem(TestCase):
    def setUp(self):
        super().setUp()
        self.flowise = FlowiseAIExternalSystem()

    def test_a_prediction(self):
        prediction = self.flowise.prediction("1", "Hola", [])

        assert isinstance(prediction, str)

    def test_b_get_chat_history(self):
        chat_history = self.flowise.get_chat_history("1")

        assert isinstance(chat_history, list)
        assert chat_history[0]["content"] == "Hola"

    def test_c_delete_chat_history(self):
        self.flowise.delete_chat_history("1")

        chat_history = self.flowise.get_chat_history("1")

        assert len(chat_history) == 0
