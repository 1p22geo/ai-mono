# Checkm8 chatbot

## [checkm8](https://github.com/erexpl/checkm8) idea by [@ErexPL](https://github.com/erexpl)

## Running and deploying

1. Install dependencies

- langchain
- langchain_community
- numpy
- flask
- requests

2. Install and run Ollama
   models needed:

- llama3 (or Mistral)
- nomic-embed-text

3. replace Ollama URLs
   in file `checkm8/chat.py`:

```
12.      embeddings = OllamaEmbeddings(
13. -        base_url="http://minisforum:9000", model="nomic-embed-text")
13. +        base_url="http://localhost:11434", model="nomic-embed-text")
(similarly for other files)
```

Your server propably is not named `minisforum`

4. Run the server

```
cd checkm8
python -m flask run -h 0.0.0.0
```

5.(optional) Open the app [http://localhost:5000](http://localhost:5000)
