from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

model = AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
streamer = TextIteratorStreamer(tokenizer)


def generate_response(history):
    inputs = tokenizer.apply_chat_template(history, return_tensors="pt")

    def internal_generate_response(inputs):
        model.generate(inputs, streamer=streamer, max_new_tokens=2500)

    generation_thread = Thread(
        target=internal_generate_response, kwargs=dict(inputs=inputs)
    )

    generation_thread.start()

    for token in streamer:
        yield token
