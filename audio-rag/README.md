# AudioRAG

Retrieval-augumented-generation as an Android app.

AI app to answer questions based on documents and voice recordings. Completely open-source, free and local. No data shared, no data saved. Not even conversation history is retained between app launches. Secure as f\*\*\*

# Running and deploying

## Install endpoint dependencies

- python libraries:
  - langchain
  - langchain_community
  - SpeechRecognition
- system dependencies:
  - ffmpeg
  - pocketsphinx
  - android SDK and Android development environment (refer to react native docs or [native/README.md](./native/README.md))
- services:
  - ollama

## Set up HTTP Endpoint

```
cd endpoint
python -m flask run -h 0.0.0.0 # start the server, don't close this terminal
```

## Set up connection to endpoint

Edit `native/src/constants.ts`, setting `ENDPOINT_URI` to the address of your endpoint server ( all mobile devices running the app will connect back to it )

## Build React Native app

refer to [native/README.md](./native/README.md)
```shell
cd native
yarn install
yarn build
```

## copy native/android/audiorag.apk to your mobile device and install the app.
