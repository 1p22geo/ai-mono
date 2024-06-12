
async function ollamaPrompt(system, req) {
  return new Promise((resolve, reject) => {
    fetch(new URL("/api/generate", "http://minisforum:9000"), {
      body: JSON.stringify({
        model: "llama3",
        stream: false,
        raw: false,
        system: system,
        prompt: req,
      }),
      method: "POST",
    }).then((res) => {
      if (!res.ok) reject()
      res.json().then((_js) => {
        const json = _js
        resolve(json.response)
      })
    })
  })
}

async function generateOutline(title, retries){
  const system = `
You are a helpful AI assistant.
Create short and informative responses, with no additional comments.
`
  const prompt = `
Q: Create an outline of titles and subtitles for a Wikipedia article, using Markdown. Output just the article outline. The title of the article is "${title}".
A: 
`
  let responses = []

  for (let n = 0; n < retries; n++) {
    let res = await ollamaPrompt(system, prompt)
    try{
      res = res.split("```")[1] || res
    }
    catch{}
    try{
      if(res.startsWith("markdown")){
        res = res.split("\n").slice(1).join("\n") || res
      }
    }
    catch{}
    responses.push(res)
  }
  responses = responses.sort((a,b)=>a.length<b.length)
  return responses[0]
}
async function generateArticle(title, retries_article, retries_outline){
  const outline = await generateOutline(title, retries_outline)
  const system = `
You are an experienced Wikpedia writer.
Write long, informative and creative articles.
`
  const prompt = `
Create an article in Markdown with the style of Wikipedia.
Write a long and informative article.
Do not use links or references.
The topic is "${title}".
Here is an outline of the article.
\`\`\`markdown
${outline}
\`\`\`
`
  let responses = []

  for (let n = 0; n < retries_article; n++) {
    let res = await ollamaPrompt(system, prompt)
    try{
      res = res.split("```")[1] || res
    }
    catch{}
    try{
      if(res.startsWith("markdown")){
        res = res.split("\n").slice(1).join("\n") || res
      }
    }
    catch{}
    responses.push(res)
  }
  responses = responses.sort((a,b)=>a.length<b.length)
  return responses[0]
}

async function main(){
  const title = "Linux"
  console.log(await generateArticle(title, 3, 5))
}

main()
