from locust import HttpUser, task, between
hf_token = ""


class MyUser(HttpUser):
    wait_time = between(1, 3)  # Time between consecutive requests

    @task
    def test_api_request(self):
        query = 'I want you to act as an expert in named entitiy recognition. I will give you the text and i want you to respond with name and organization in json format.Query text: Hello, My name is Elon Musk. I work at Tesla. '
                
        max_token = 512

        self.client.get("", json={"query": query, "max_token": max_token})


