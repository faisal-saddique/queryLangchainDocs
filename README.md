# Query Langchain Docs

Query Langchain Docs is an open-source project that enables users to interact with the Langchain documentation through an AI-powered assistant. The project consists of scripts for scraping the Langchain documentation, converting it to Markdown format, and setting up an AI assistant using the OpenAI GPT-3.5 Turbo model to answer user queries based on the scraped content.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Scraping Documentation](#scraping-documentation)
  - [Creating the AI Assistant](#creating-the-ai-assistant)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Query Langchain Docs empowers developers and users to interact with the vast Langchain documentation in a more intuitive and conversational manner. The project utilizes web scraping techniques to extract the documentation content, converting it to a readable format, and employs AI-driven language models to provide helpful answers to user queries based on the available context.

## Requirements

Before getting started with Query Langchain Docs, ensure that you have the following dependencies and resources set up:

- Node.js and npm: To run the JavaScript-based scraping script.
- Python 3.x: For setting up the AI assistant and running related scripts.
- OpenAI API Key: Obtain an API key from OpenAI to access the GPT-3.5 Turbo model.
- Langchain Documentation URL: Specify the target Langchain documentation URL to scrape.

## Getting Started

Follow the steps below to set up the project and use the AI assistant.

### Scraping Documentation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/query-langchain-docs.git
cd query-langchain-docs
```

2. Edit the `scrapeLangchainDocs.js` script:

   - Set the `targetUrl` variable to the URL of the Langchain documentation you want to scrape.
   - Set the `outputDirectory` variable to the desired path where the scraped Markdown files will be saved.

3. Run the scraping script using Node.js:

```bash
node scrapeLangchainDocs.js
```

The script will fetch the HTML content, convert it to Markdown, and save each page's content as a separate Markdown file in the specified `outputDirectory`.

### Creating the AI Assistant

1. Install the required Python packages:

```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key as an environment variable with the name `OPENAI_API_KEY`.

3. Run the `createEmbeddings.py` script to create a vector store from the scraped Markdown documents:

```bash
python createEmbeddings.py
```

This script will split the large documents into smaller chunks, convert them to embeddings using OpenAI, and create a FAISS vector store.

## Usage

After setting up the AI assistant and creating the vector store, you can interact with it using the `interactWithLangchainDocs.py` script. The AI assistant will answer your queries based on the available context from the Langchain documentation.

To use the AI assistant, run the following command:

```bash
python interactWithLangchainDocs.py
```

Follow the instructions to enter your queries, and the AI assistant will respond based on the relevant context from the Langchain documentation.

## Contributing

We welcome contributions to improve Query Langchain Docs! If you find any issues or have ideas for enhancements, feel free to create a pull request or open an issue.

## License

Query Langchain Docs is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code according to the terms of the license.

---

Thank you for your interest in Query Langchain Docs! We hope this project simplifies your interactions with the Langchain documentation and provides valuable insights through AI-driven assistance. If you encounter any difficulties or have questions, please don't hesitate to reach out through the issues section or via email.

Happy coding!