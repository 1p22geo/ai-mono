import xml.etree.ElementTree as ET
import os
import base64

schema = "{http://www.mediawiki.org/xml/export-0.10/}"

tree = ET.parse('wiki.xml')
root = tree.getroot()
for page in root:
    if page.tag == f"{schema}page":
        name = ""
        for title in page:
            if title.tag == f"{schema}title":
                name = base64.b64encode(
                    bytes(title.text, "utf-8"), altchars=b"-_").decode("utf-8")
        for revision in page:
            if revision.tag == f"{schema}revision":
                for text in revision:
                    if text.tag == f"{schema}text":
                        with open(f"data/{name}.mediawiki", "w") as f:
                            f.write(text.text)
                        os.system(
                            f"pandoc --from mediawiki --to markdown_github --no-highlight -o data/{name} data/{name}.mediawiki")
