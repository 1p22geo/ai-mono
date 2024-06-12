import lib
import re

TITLE = "Linux"

# STAGE 1 - generating outline

system = """
You are a helpful AI assistant.
Create short and informative responses, with no additional comments.
"""

prompt = f"""
Q: Create an outline of titles and subtitles for a Wikipedia article, using Markdown. Output just the article outline. The title of the article is "{TITLE}".
A:
"""

responses = []
for n in range(3):
    res = lib.ai(system, prompt)
    try:
        res = res.split("```")[1]
    except:
        pass
    try:
        if res.startswith("markdown"):
            res = "\n".join(res.split("\n")[1:])
    except:
        pass
    responses.append(res)


# Tree-of-thought algorythm, pick longest of all responses
responses = sorted(responses, key=(lambda r: len(r)))
outline = responses[-1]


# STAGE 2 - generating article based on outline

system = """
You are an experienced Wikpedia writer.
Write long, informative and creative articles.
"""

prompt = f"""
Create an article in Markdown with the style of Wikipedia.
Write a long and informative article.
Do not use links or references.
The topic is "{TITLE}".
Here is an outline of the article.
```markdown
{outline}
```
"""

responses = []
for n in range(3):
    res = lib.ai(system, prompt)
    try:
        res = res.split("```")[1]
    except:
        pass
    try:
        if res.startswith("markdown"):
            res = "\n".join(res.split("\n")[1:])
    except:
        pass
    responses.append(res)


# Tree-of-thought algorythm, pick longest of all responses
responses = sorted(responses, key=(lambda r: len(r)))
article = responses[-1]
