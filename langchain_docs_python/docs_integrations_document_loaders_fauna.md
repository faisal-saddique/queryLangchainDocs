Fauna
=====

> [Fauna](https://fauna.com/) is a Document Database.

Query `Fauna` documents

    #!pip install fauna

Query data example[](#query-data-example "Direct link to Query data example")
------------------------------------------------------------------------------

    from langchain.document_loaders.fauna import FaunaLoadersecret = "<enter-valid-fauna-secret>"query = "Item.all()"  # Fauna query. Assumes that the collection is called "Item"field = "text"  # The field that contains the page content. Assumes that the field is called "text"loader = FaunaLoader(query, field, secret)docs = loader.lazy_load()for value in docs:    print(value)

### Query with Pagination[](#query-with-pagination "Direct link to Query with Pagination")

You get a `after` value if there are more data. You can get values after the curcor by passing in the `after` string in query.

To learn more following [this link](https://fqlx-beta--fauna-docs.netlify.app/fqlx/beta/reference/schema_entities/set/static-paginate)

    query = """Item.paginate("hs+DzoPOg ... aY1hOohozrV7A")Item.all()"""loader = FaunaLoader(query, field, secret)