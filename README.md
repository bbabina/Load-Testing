# Hugging Face Inference Endpoint Load Testing with Locust

This README provides instructions on how to use Locust to load test the Hugging Face Inference Endpoint using the provided Python script.

## Requirements

- Python 3.6 or higher
- Locust (install with `pip install locust`)
- Hugging Face Hub (install with `pip install huggingface-hub`)

## Setup

1. Install the required libraries by running the following command:

```bash
pip install locust huggingface-hub
```

2. Copy and paste the provided Python script into a file named `locustfile.py`.

3. Replace the placeholders in the script:
   - `endpoint_url`: Replace with the URL of your Hugging Face Inference Endpoint.
   - `hf_token`: Replace with your Hugging Face authentication token.

## Running the Load Test

1. Open a terminal window and navigate to the directory where `locustfile.py` is located.

2. Start the Locust web UI by running the following command:

```bash
locust -f locustfile.py
```

3. Open your web browser and go to `http://localhost:8089` to access the Locust web UI.

4. Enter the total number of users and the spawn rate (users spawned per second) you want to simulate.

5. Click the "Start swarming" button to begin the load test.

## Understanding the Load Test Script

The provided Python script `locustfile.py` contains a Locust user class named `MyUser`. This class represents a user that will interact with the Hugging Face Inference Endpoint. Here's what the script does:

1. Import necessary libraries and configure logging.

2. Define the `MyUser` class that inherits from `HttpUser`. The `wait_time` attribute determines the time between consecutive requests.

3. Inside the `MyUser` class, there's a `@task` decorated function named `test_huggingface_endpoint`. This function simulates user interactions with the Hugging Face Inference Endpoint.

4. In the `test_huggingface_endpoint` function, the script initializes the `InferenceClient` from the Hugging Face Hub, which will handle interactions with the Inference Endpoint.

5. The script defines a set of keyword arguments (`gen_kwargs`) that control the text generation process. You can modify these arguments to customize the generated output.

6. The `prompt` variable contains the text prompt provided to the model for generating responses.

7. The script uses the `InferenceClient` to start text generation in streaming mode, and it prints the generated text until a stop sequence is encountered.

## Customization

Feel free to customize the load test script according to your specific requirements. You can adjust the `gen_kwargs` to change the text generation behavior or modify the `prompt` to test different types of inputs.

Happy Load Testing!
