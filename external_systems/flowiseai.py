import httpx

from settings import get_settings

settings = get_settings()


class FlowiseAIExternalSystem:
    def __init__(self):
        self.flowise_base_url = settings.flowise_base_url
        self.flowise_chatflow_id = settings.flowise_chatflow_id
        self.flowise_username = settings.flowise_username
        self.flowise_password = settings.flowise_password

    def prediction(
        self,
        session_id: str,
        question: str,
        history: list,
    ):
        timeout = httpx.Timeout(timeout=60)

        with httpx.Client(base_url=self.flowise_base_url,timeout=timeout) as client:
            json = {
                "question": question,
                "history": history,
                "overrideConfig": {
                    "sessionId": session_id,
                },
            }

            response = client.post(
                url=f"/api/v1/prediction/{self.flowise_chatflow_id}",
                json=json,
            )

            response.raise_for_status()

            data = response.json()

            content = data["text"]

            return content

    def get_chat_history(
        self,
        session_id: str,
    ):
        auth = httpx.BasicAuth(
            username=self.flowise_username,
            password=self.flowise_password,
        )

        timeout = httpx.Timeout(timeout=60)

        with httpx.Client(base_url=self.flowise_base_url, auth=auth,timeout=timeout) as client:
            params = {
                "sessionId": session_id,
            }

            response = client.get(
                url=f"/api/v1/chatmessage/{self.flowise_chatflow_id}",
                params=params,
            )

            response.raise_for_status()

            data = response.json()

            return data

    def delete_chat_history(
        self,
        session_id: str,
    ):
        auth = httpx.BasicAuth(
            username=self.flowise_username,
            password=self.flowise_password,
        )

        timeout = httpx.Timeout(timeout=60)

        with httpx.Client(base_url=self.flowise_base_url, auth=auth,timeout=timeout) as client:
            params = {
                "sessionId": session_id,
            }

            response = client.delete(
                url=f"/api/v1/chatmessage/{self.flowise_chatflow_id}",
                params=params,
            )

            response.raise_for_status()

            data = response.json()

            return data
