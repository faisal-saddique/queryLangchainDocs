S3 File
=======

Compatibility

Only available on Node.js.

This covers how to load document objects from an s3 file object.

Setup[](#setup "Direct link to Setup")
---------------------------------------

To run this index you'll need to have Unstructured already set up and ready to use at an available URL endpoint. It can also be configured to run locally.

See the docs [here](https://js.langchain.com/docs/modules/indexes/document_loaders/examples/file_loaders/unstructured) for information on how to do that.

You'll also need to install the official AWS SDK:

*   npm
*   Yarn
*   pnpm

    npm install @aws-sdk/client-s3

    yarn add @aws-sdk/client-s3

    pnpm add @aws-sdk/client-s3

Usage[](#usage "Direct link to Usage")
---------------------------------------

Once Unstructured is configured, you can use the S3 loader to load files and then convert them into a Document.

You can optionally provide a s3Config parameter to specify your bucket region, access key, and secret access key. If these are not provided, you will need to have them in your environment (e.g., by running `aws configure`).

    import { S3Loader } from "langchain/document_loaders/web/s3";const loader = new S3Loader({  bucket: "my-document-bucket-123",  key: "AccountingOverview.pdf",  s3Config: {    region: "us-east-1",    credentials: {      accessKeyId: "AKIAIOSFODNN7EXAMPLE",      secretAccessKey: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",    },  },  unstructuredAPIURL: "http://localhost:8000/general/v0/general",  unstructuredAPIKey: "", // this will be soon required});const docs = await loader.load();console.log(docs);

#### API Reference:

*   [S3Loader](/docs/api/document_loaders_web_s3/classes/S3Loader) from `langchain/document_loaders/web/s3`