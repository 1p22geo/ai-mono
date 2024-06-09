CHAT_SYSTEM = {
    "casual": """
You are Checkm8, an AI companion chatbot.
Answer casually, without special introductions and useless text.
Do not brag and speak about yourself being an AI.
Try to act cool, like a human, and only admit to being a chatbot once EXPLICITLY asked for it.
Provide short, compact, casual responses.
""",
    "professional":
    """
You are Checkm8, a revolutionary AI chatbot.
You are an entirely new class of technology, powerful and flexible.
Answer dynamically and informatively.
Provide professional and compact responses, with no extra introductions.
""",
    "creative": """
You are Checkm8, a revolutionary AI chatbot.
You are an entirely new class of technology, powerful and flexible.
Answer dynamically and creatively.
Provide lengthy, but creative and informational responses.
"""}

SENTIMENT = """
Analyze the following sentiment in terms of various factors, such as constructiveness, helpfulness, humor and various other factors you can find.
Answer only using JSON.
Do not be afraid to use nested objects and complicated structures.
Provide a long and informative response.
Output only the answer.
"""


def MK_SLOGANS(prod, info): return f"""
Create some marketing slogans for a product described as: "{prod}".
Here's some more information about it:
```
{info}
```
Answer only using JSON.
Answer a single JSON array with the marketing slogans, named as `slogans`.
Output only the answer.
"""


def MK_BODY(prod, info, slogans, style): return f"""
Create some marketing copy text for a product described as: "{prod}".
Here's some more information about it:
```
{info}
```
Your style should match the following description:
```
{style}
```
Here's some ready marketing slogans done by a professional:
```
{slogans}
```
The text should be reusable, among all leaflets, scripts, campaigns and webpages refering to "{prod}"
"""


def MK_ITEM(prod, info, slogans, style, copy, item): return f"""
Create a/n "{item}" as part of a marketing campaign for a product described as: "{prod}"
Here's some more information about it:
```
{info}
```
Your style should match the following description:
```
{style}
```
Here's some ready marketing slogans done by a professional:
```
{slogans}
```
Here's some body copy text:
```
{copy}
```
Output just the {item}
"""
