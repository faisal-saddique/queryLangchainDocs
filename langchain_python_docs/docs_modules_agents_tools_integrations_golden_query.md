Golden Query
============

This notebook goes over how to use the golden-query tool.

*   Go to the [Golden API docs](https://docs.golden.com/) to get an overview about the Golden API.
*   Create a Golden account if you don't have one on the [Golden Website](/docs/modules/agents/tools/integrations/golden.com).
*   Get your API key from the [Golden API Settings](https://golden.com/settings/api) page.
*   Save your API key into GOLDEN\_API\_KEY env variable

    import osos.environ["GOLDEN_API_KEY"] = ""

    from langchain.utilities.golden_query import GoldenQueryAPIWrapper

    golden_query = GoldenQueryAPIWrapper()

    import jsonjson.loads(golden_query.run("companies in nanotech"))

        {'results': [{'id': 4673886,       'latestVersionId': 60276991,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'Samsung', 'citations': []}]}]},      {'id': 7008,       'latestVersionId': 61087416,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'Intel', 'citations': []}]}]},      {'id': 24193,       'latestVersionId': 60274482,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'Texas Instruments', 'citations': []}]}]},      {'id': 1142,       'latestVersionId': 61406205,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'Advanced Micro Devices', 'citations': []}]}]},      {'id': 193948,       'latestVersionId': 58326582,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'Freescale Semiconductor', 'citations': []}]}]},      {'id': 91316,       'latestVersionId': 60387380,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'Agilent Technologies', 'citations': []}]}]},      {'id': 90014,       'latestVersionId': 60388078,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'Novartis', 'citations': []}]}]},      {'id': 237458,       'latestVersionId': 61406160,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'Analog Devices', 'citations': []}]}]},      {'id': 3941943,       'latestVersionId': 60382250,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'AbbVie Inc.', 'citations': []}]}]},      {'id': 4178762,       'latestVersionId': 60542667,       'properties': [{'predicateId': 'name',         'instances': [{'value': 'IBM', 'citations': []}]}]}],     'next': 'https://golden.com/api/v2/public/queries/59044/results/?cursor=eyJwb3NpdGlvbiI6IFsxNzYxNiwgIklCTS04M1lQM1oiXX0%3D&pageSize=10',     'previous': None}