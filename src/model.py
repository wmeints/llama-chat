from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

# Make sure you have a license to use this model!
model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

model = AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# The streamer returns an iterator that yields tokens as they are generated.
# This allows the model to generate tokens in the background while the client
# processes the tokens that have already been generated.
#
# Note: we skip the prompt, as we already know what the user said.
# Note: we skip special tokens, because we don't need to see them either.
streamer = TextIteratorStreamer(
    tokenizer, skip_prompt=True, decode_kwargs=dict(skip_special_tokens=True)
)


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
