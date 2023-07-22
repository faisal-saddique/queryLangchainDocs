GitHub
======

This example goes over how to load data from a GitHub repository. You can set the `GITHUB_ACCESS_TOKEN` environment variable to a GitHub access token to increase the rate limit and access private repositories.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

The GitHub loader requires the [ignore npm package](https://www.npmjs.com/package/ignore) as a peer dependency. Install it like this:

*   npm
*   Yarn
*   pnpm

    npm install ignore

    yarn add ignore

    pnpm add ignore

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { GithubRepoLoader } from "langchain/document_loaders/web/github";export const run = async () => {  const loader = new GithubRepoLoader(    "https://github.com/hwchase17/langchainjs",    { branch: "main", recursive: false, unknown: "warn" }  );  const docs = await loader.load();  console.log({ docs });};

#### API Reference:

*   [GithubRepoLoader](/docs/api/document_loaders_web_github/classes/GithubRepoLoader) from `langchain/document_loaders/web/github`

The loader will ignore binary files like images.

### Using .gitignore syntax[​](#using-gitignore-syntax "Direct link to Using .gitignore syntax")

To ignore specific files, you can pass in an `ignorePaths` array into the constructor:

    import { GithubRepoLoader } from "langchain/document_loaders/web/github";export const run = async () => {  const loader = new GithubRepoLoader(    "https://github.com/hwchase17/langchainjs",    { branch: "main", recursive: false, unknown: "warn", ignorePaths: ["*.md"] }  );  const docs = await loader.load();  console.log({ docs });  // Will not include any .md files};

#### API Reference:

*   [GithubRepoLoader](/docs/api/document_loaders_web_github/classes/GithubRepoLoader) from `langchain/document_loaders/web/github`