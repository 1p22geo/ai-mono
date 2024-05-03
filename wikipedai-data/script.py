import os
import re
import base64


files = [f for f in os.listdir(
    "data/") if os.path.isfile(os.path.join("data", f))]

for f in files:
    outline = ""
    content = ""
    with open("data/"+f, "r") as file:
        content = file.read()
        file.seek(0)
        for line in file.readlines():
            if re.match(r"^#", line):
                outline += line
    title = base64.b64decode(f, "-_").decode("utf-8")
    print(
        f"<s>[INST] You are an experienced Wikpedia writer.\nWrite long, informative and creative articles.\n Create an article in Markdown with the style of Wikipedia.\nWrite a long and informative article.\nDo not use links or references.\nThe topic is \"{title}\".\nHere is an outline of the article.\n```markdown {outline}``` [/INST] {content} </s>")
