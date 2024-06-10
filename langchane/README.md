# Simpler version of [audio-rag](../audio-rag/README.md)

## Running and deploying
1. Install libraries
   - flask
   - langchain
   - langchain_community
2. install Ollama and set up URLs
   - your server is propably not named `minisforum:9000`, rather `localhost:11434`
   - edit `rag_set.py` to update the server address
3.
```shell
python -m flask -h 0.0.0.0
``` 
