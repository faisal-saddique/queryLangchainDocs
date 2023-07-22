Cube Semantic Layer
===================

This notebook demonstrates the process of retrieving Cube's data model metadata in a format suitable for passing to LLMs as embeddings, thereby enhancing contextual information.

### About Cube[​](#about-cube "Direct link to About Cube")

[Cube](https://cube.dev/) is the Semantic Layer for building data apps. It helps data engineers and application developers access data from modern data stores, organize it into consistent definitions, and deliver it to every application.

Cube’s data model provides structure and definitions that are used as a context for LLM to understand data and generate correct queries. LLM doesn’t need to navigate complex joins and metrics calculations because Cube abstracts those and provides a simple interface that operates on the business-level terminology, instead of SQL table and column names. This simplification helps LLM to be less error-prone and avoid hallucinations.

### Example[​](#example "Direct link to Example")

`Cube Semantic Loader` requires 2 arguments: | Input Parameter | Description | | --- | --- | | `cube_api_url` | The URL of your Cube's deployment REST API. Please refer to the [Cube documentation](https://cube.dev/docs/http-api/rest#configuration-base-path) for more information on configuring the base path. | | `cube_api_token` | The authentication token generated based on your Cube's API secret. Please refer to the [Cube documentation](https://cube.dev/docs/security#generating-json-web-tokens-jwt) for instructions on generating JSON Web Tokens (JWT). |

    import jwtfrom langchain.document_loaders import CubeSemanticLoaderapi_url = "https://api-example.gcp-us-central1.cubecloudapp.dev/cubejs-api/v1/meta"cubejs_api_secret = "api-secret-here"security_context = {}# Read more about security context here: https://cube.dev/docs/securityapi_token = jwt.encode(security_context, cubejs_api_secret, algorithm="HS256")loader = CubeSemanticLoader(api_url, api_token)documents = loader.load()

Returns:

A list of documents with the following attributes:

*   `page_content`
*   `metadata`
    *   `table_name`
    *   `column_name`
    *   `column_data_type`
    *   `column_title`
    *   `column_description`

> page\_content='table name: orders\_view, column name: orders\_view.total\_amount, column data type: number, column title: Orders View Total Amount, column description: None' metadata={'table\_name': 'orders\_view', 'column\_name': 'orders\_view.total\_amount', 'column\_data\_type': 'number', 'column\_title': 'Orders View Total Amount', 'column\_description': 'None'}