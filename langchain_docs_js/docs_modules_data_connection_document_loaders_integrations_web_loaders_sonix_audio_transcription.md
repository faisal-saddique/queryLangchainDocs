Sonix Audio
===========

Compatibility

Only available on Node.js.

This covers how to load document objects from an audio file using the [Sonix](https://sonix.ai/) API.

Setup[](#setup "Direct link to Setup")
---------------------------------------

To run this loader you will need to create an account on the [https://sonix.ai/](https://sonix.ai/) and obtain an auth key from the [https://my.sonix.ai/api](https://my.sonix.ai/api) page.

You'll also need to install the `sonix-speech-recognition` library:

*   npm
*   Yarn
*   pnpm

    npm install sonix-speech-recognition

    yarn add sonix-speech-recognition

    pnpm add sonix-speech-recognition

Usage[](#usage "Direct link to Usage")
---------------------------------------

Once auth key is configured, you can use the loader to create transcriptions and then convert them into a Document. In the `request` parameter, you can either specify a local file by setting `audioFilePath` or a remote file using `audioUrl`. You will also need to specify the audio language. See the list of supported languages [here](https://sonix.ai/docs/api#languages).

    import { SonixAudioTranscriptionLoader } from "langchain/document_loaders/web/sonix_audio";const loader = new SonixAudioTranscriptionLoader({  sonixAuthKey: "SONIX_AUTH_KEY",  request: {    audioFilePath: "LOCAL_AUDIO_FILE_PATH",    fileName: "FILE_NAME",    language: "en",  },});const docs = await loader.load();console.log(docs);

#### API Reference:

*   [SonixAudioTranscriptionLoader](/docs/api/document_loaders_web_sonix_audio/classes/SonixAudioTranscriptionLoader) from `langchain/document_loaders/web/sonix_audio`