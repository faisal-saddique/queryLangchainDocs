Confluence
==========

Compatibility

Only available on Node.js.

This covers how to load document objects from pages in a Confluence space.

Credentials[](#credentials "Direct link to Credentials")
---------------------------------------------------------

*   You'll need to set up an access token and provide it along with your confluence username in order to authenticate the request
*   You'll also need the `space key` for the space containing the pages to load as documents. This can be found in the url when navigating to your space e.g. `https://example.atlassian.net/wiki/spaces/{SPACE_KEY}`
*   And you'll need to install `html-to-text` to parse the pages into plain text

*   npm
*   Yarn
*   pnpm

    npm install html-to-text

    yarn add html-to-text

    pnpm add html-to-text

Usage[](#usage "Direct link to Usage")
---------------------------------------

    import { ConfluencePagesLoader } from "langchain/document_loaders/web/confluence";const username = process.env.CONFLUENCE_USERNAME;const accessToken = process.env.CONFLUENCE_ACCESS_TOKEN;if (username && accessToken) {  const loader = new ConfluencePagesLoader({    baseUrl: "https://example.atlassian.net/wiki",    spaceKey: "~EXAMPLE362906de5d343d49dcdbae5dEXAMPLE",    username,    accessToken,  });  const documents = await loader.load();  console.log(documents);} else {  console.log(    "You must provide a username and access token to run this example."  );}

#### API Reference:

*   [ConfluencePagesLoader](/docs/api/document_loaders_web_confluence/classes/ConfluencePagesLoader) from `langchain/document_loaders/web/confluence`