from openai import OpenAI
from config import OPENAI_KEY
from context_memory import add, get
from personality import get_prompt

client = OpenAI(api_key=OPENAI_KEY)

def ask_ai(prompt):
    add("user", prompt)

    messages = [{"role": "system", "content": get_prompt()}]
    messages.extend(get())

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        add("assistant", reply)
        return reply

    except:
        return "I am currently offline."

