from locust import HttpUser, task, between
from huggingface_hub import InferenceClient
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Time between consecutive requests

    @task
    def test_huggingface_endpoint(self):
        #interacting with the Hugging Face Inference Endpoint
        endpoint_url = ""
        hf_token = ""
        client = InferenceClient(endpoint_url, token=hf_token)

        gen_kwargs = dict(
            max_new_tokens=512,
            top_k=30,
            top_p=0.9,
            temperature=0.2,
            repetition_penalty=1.02,
            stop_sequences=["\nUser:", "", "</s>"],
        )

        prompt = "What can you do in Nuremberg, Germany? Give me 3 Tips"

        stream = client.text_generation(prompt, stream=True, details=True, **gen_kwargs)

        for r in stream:
            # skip special tokens
            if r.token.special:
                continue
            # stop if we encounter a stop sequence
            if r.token.text in gen_kwargs["stop_sequences"]:
                break
            # yield the generated token
            print(r.token.text, end = "")
            # yield r.token.text


