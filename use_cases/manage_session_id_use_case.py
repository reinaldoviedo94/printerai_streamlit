import uuid


class ManageSessionIdUseCase:
    def __init__(self):
        pass

    @staticmethod
    def save_session_id():
        session_id = str(uuid.uuid4())
        with open("session_id", "w") as f:
            f.write(session_id)
        return session_id

    def read_session_id(self):
        try:
            with open("session_id", "r") as f:
                session_id = f.read()
                return session_id
        except:
            return self.save_session_id()
