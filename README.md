# LLama 3.1 Instruct Chat Sample

This repository contains a simple demo to build a streaming chat interface for the LLama 3.1 8B instruct model from Meta.
Please note that this demo is pretty rough. We use this to quickly check out new TPU-enabled machines.

## System requirements

- [Rye](https://rye.astral.sh)
- [Hugging Face account](https://huggingface.co)

## Getting started

Run the following commands to sync the environment:

```bash
rye sync
```

Next, make sure you're logged in with the hugging face. You can use the following command to log in:

```bash
source .venv/bin/activate
huggingface-cli login
```

After that, run the following command to start the app:

```bash
chainlit run src/main.py
```
