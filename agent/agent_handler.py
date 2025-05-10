import openai
import os
from agent.functions import query_executive_orders

openai.api_base = os.getenv("OLLAMA_API_BASE")
openai.api_key = "ollama"  # dummy key for local ollama

tool_schema = {
    "name": "query_executive_orders",
    "description": "Get executive orders by president and month",
    "parameters": {
        "type": "object",
        "properties": {
            "president": {"type": "string"},
            "month": {"type": "string"},
        },
        "required": ["president", "month"]
    }
}

async def run_agent(user_query: str):
    response = await openai.ChatCompletion.acreate(
        model="qwen:0.5b",
        messages=[{"role": "user", "content": user_query}],
        tools=[{"type": "function", "function": tool_schema}],
        tool_choice="auto"
    )

    message = response.choices[0].message
    if message.tool_calls:
        tool = message.tool_calls[0]
        if tool.function.name == "query_executive_orders":
            args = eval(tool.function.arguments)
            result = await query_executive_orders(**args)
            summary = await openai.ChatCompletion.acreate(
                model="qwen:0.5b",
                messages=[
                    {"role": "user", "content": f"Summarize these executive orders: {result}"}
                ]
            )
            return summary.choices[0].message.content
    return message.content

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")  # fallback model

async def run_agent(query: str) -> str:
    try:
        chat = model.start_chat(history=[])
        response = chat.send_message(query)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"



# import openai
# from openai import AsyncOpenAI

# client = AsyncOpenAI(api_key="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")  # OR use environment variable

# async def run_agent(query: str) -> str:
#     response = await client.chat.completions.create(
#         model="gpt-3.5-turbo",  # or "gpt-4"
#         messages=[
#             {"role": "user", "content": query}
#         ]
#     )
#     return response.choices[0].message.content.strip()
