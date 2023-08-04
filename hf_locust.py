from gevent import monkey
monkey.patch_all()

from huggingface_hub import InferenceClient

# HF Inference Endpoints parameter
endpoint_url = ""
hf_token = ""

# Streaming Client
client = InferenceClient(endpoint_url, token=hf_token)

# generation parameter
gen_kwargs = dict(
    max_new_tokens=512,
    top_k=30,
    top_p=0.9,
    temperature=0.2,
    repetition_penalty=1.02,
    stop_sequences=["\nUser:", "<|endoftext|>", "</s>"],
)
# prompt
prompt = "I want you to act as an expert in named entitiy recognition. I will give you the text and i want you to respond with name and organization in json format.Query text: Hello, My name is Elon Musk. I work at Tesla."

stream = client.text_generation(prompt, stream=True, details=True, **gen_kwargs)

# yield each generated token
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







