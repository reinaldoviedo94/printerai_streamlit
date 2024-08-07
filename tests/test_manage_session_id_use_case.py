from unittest import TestCase

from use_cases.manage_session_id_use_case import ManageSessionIdUseCase


class TestManageSessionIdUseCase(TestCase):
    def setUp(self):
        super().setUp()
        self.manage_session_use_case = ManageSessionIdUseCase()

    def test_save_session_id(self):
        session_id = self.manage_session_use_case.save_session_id()

        assert isinstance(session_id, str)

    def test_read_session_id(self):
        session_id = self.manage_session_use_case.read_session_id()

        assert isinstance(session_id, str)
