import chainlit as cl
from model import generate_response


@cl.on_chat_start
def on_start():
    cl.user_session.set(
        "history",
        [
            {
                "role": "system",
                "content": "You're a helpful assistant. Your name is Ricardo.",
            }
        ],
    )


@cl.on_message
async def on_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    message = cl.Message(content="")

    await message.send()

    for token in generate_response(history):
        await message.stream_token(token)

    history.append({"role": "assistant", "content": message.content})
    await message.update()
