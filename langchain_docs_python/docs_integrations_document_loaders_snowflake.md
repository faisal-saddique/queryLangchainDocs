Snowflake
=========

This notebooks goes over how to load documents from Snowflake

    pip install snowflake-connector-python

    import settings as sfrom langchain.document_loaders import SnowflakeLoader

    QUERY = "select text, survey_id from CLOUD_DATA_SOLUTIONS.HAPPY_OR_NOT.OPEN_FEEDBACK limit 10"snowflake_loader = SnowflakeLoader(    query=QUERY,    user=s.SNOWFLAKE_USER,    password=s.SNOWFLAKE_PASS,    account=s.SNOWFLAKE_ACCOUNT,    warehouse=s.SNOWFLAKE_WAREHOUSE,    role=s.SNOWFLAKE_ROLE,    database=s.SNOWFLAKE_DATABASE,    schema=s.SNOWFLAKE_SCHEMA,)snowflake_documents = snowflake_loader.load()print(snowflake_documents)

    from snowflakeLoader import SnowflakeLoaderimport settings as sQUERY = "select text, survey_id as source from CLOUD_DATA_SOLUTIONS.HAPPY_OR_NOT.OPEN_FEEDBACK limit 10"snowflake_loader = SnowflakeLoader(    query=QUERY,    user=s.SNOWFLAKE_USER,    password=s.SNOWFLAKE_PASS,    account=s.SNOWFLAKE_ACCOUNT,    warehouse=s.SNOWFLAKE_WAREHOUSE,    role=s.SNOWFLAKE_ROLE,    database=s.SNOWFLAKE_DATABASE,    schema=s.SNOWFLAKE_SCHEMA,    metadata_columns=["source"],)snowflake_documents = snowflake_loader.load()print(snowflake_documents)