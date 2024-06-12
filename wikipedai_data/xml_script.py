import xml.etree.ElementTree as ET
import os

schema = "{http://www.mediawiki.org/xml/export-0.10/}"

tree = ET.parse('wiki_smol.xml')
root = tree.getroot()
for page in root:
    if page.tag == f"{schema}page":
        name = ""
        for title in page:
            if title.tag == f"{schema}title":
                name = title.text
        for revision in page:
            if revision.tag == f"{schema}revision":
                for text in revision:
                    if text.tag == f"{schema}text":
                        with open(f"{name}.mediawiki", "w") as f:
                            f.write(text.text)
                        os.system(f"pandoc --from mediawiki --to markdown_github --no-highlight -o {name}.md {name}.mediawiki")
