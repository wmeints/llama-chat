# LLama 3.1 Instruct Chat Sample

This repository contains a simple demo to build a streaming chat interface for the LLama 3.1 8B instruct model from Meta.
Please note that this demo is pretty rough. We use this to quickly check out new TPU-enabled machines.

## System requirements

- [Rye](https://rye.astral.sh)
- [Hugging Face account](https://huggingface.co)

## Getting started

Run the following commands to sync and activate the environment:

```bash
rye sync
source .venv/bin/activate
```

Next, login in with the hugging face CLI using the following command:

```bash
huggingface-cli login
```

After that, run the following command to start the app:

```bash
chainlit run src/main.py
```

## How does the sample work?

This sample uses the Llama 3.1 8B Instruct model with a basic system prompt to implement a chat scenario.
It doesn't have a conversation history other than the messages in the current chat session. I've left building history functionality up to you as an exercise. 

This sample supports streaming the response back to the user using the appropriate tools from the `transformers` library.
