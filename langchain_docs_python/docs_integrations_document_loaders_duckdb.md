DuckDB
======

> [DuckDB](https://duckdb.org/) is an in-process SQL OLAP database management system.

Load a `DuckDB` query with one document per row.

    #!pip install duckdb

    from langchain.document_loaders import DuckDBLoader

    Team,PayrollNationals,81.34Reds,82.20

        Writing example.csv

    loader = DuckDBLoader("SELECT * FROM read_csv_auto('example.csv')")data = loader.load()

    print(data)

        [Document(page_content='Team: Nationals\nPayroll: 81.34', metadata={}), Document(page_content='Team: Reds\nPayroll: 82.2', metadata={})]

Specifying Which Columns are Content vs Metadata[](#specifying-which-columns-are-content-vs-metadata "Direct link to Specifying Which Columns are Content vs Metadata")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    loader = DuckDBLoader(    "SELECT * FROM read_csv_auto('example.csv')",    page_content_columns=["Team"],    metadata_columns=["Payroll"],)data = loader.load()

    print(data)

        [Document(page_content='Team: Nationals', metadata={'Payroll': 81.34}), Document(page_content='Team: Reds', metadata={'Payroll': 82.2})]

Adding Source to Metadata[](#adding-source-to-metadata "Direct link to Adding Source to Metadata")
---------------------------------------------------------------------------------------------------

    loader = DuckDBLoader(    "SELECT Team, Payroll, Team As source FROM read_csv_auto('example.csv')",    metadata_columns=["source"],)data = loader.load()

    print(data)

        [Document(page_content='Team: Nationals\nPayroll: 81.34\nsource: Nationals', metadata={'source': 'Nationals'}), Document(page_content='Team: Reds\nPayroll: 82.2\nsource: Reds', metadata={'source': 'Reds'})]