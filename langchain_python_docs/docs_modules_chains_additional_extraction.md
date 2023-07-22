Extraction
==========

The extraction chain uses the OpenAI `functions` parameter to specify a schema to extract entities from a document. This helps us make sure that the model outputs exactly the schema of entities and properties that we want, with their appropriate types.

The extraction chain is to be used when we want to extract several entities with their properties from the same passage (i.e. what people were mentioned in this passage?)

    from langchain.chat_models import ChatOpenAIfrom langchain.chains import create_extraction_chain, create_extraction_chain_pydanticfrom langchain.prompts import ChatPromptTemplate

        /Users/harrisonchase/.pyenv/versions/3.9.1/envs/langchain/lib/python3.9/site-packages/deeplake/util/check_latest_version.py:32: UserWarning: A newer version of deeplake (3.6.4) is available. It's recommended that you update to the latest version using `pip install -U deeplake`.      warnings.warn(

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

Extracting entities[​](#extracting-entities "Direct link to Extracting entities")
---------------------------------------------------------------------------------

To extract entities, we need to create a schema where we specify all the properties we want to find and the type we expect them to have. We can also specify which of these properties are required and which are optional.

    schema = {    "properties": {        "name": {"type": "string"},        "height": {"type": "integer"},        "hair_color": {"type": "string"},    },    "required": ["name", "height"],}

    inp = """Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.        """

    chain = create_extraction_chain(schema, llm)

As we can see, we extracted the required entities and their properties in the required format (it even calculated Claudia's height before returning!)

    chain.run(inp)

        [{'name': 'Alex', 'height': 5, 'hair_color': 'blonde'},     {'name': 'Claudia', 'height': 6, 'hair_color': 'brunette'}]

Several entity types[​](#several-entity-types "Direct link to Several entity types")
------------------------------------------------------------------------------------

Notice that we are using OpenAI functions under the hood and thus the model can only call one function per request (with one, unique schema)

If we want to extract more than one entity type, we need to introduce a little hack - we will define our properties with an included entity type.

Following we have an example where we also want to extract dog attributes from the passage. Notice the 'person_' and 'dog_' prefixes we use for each property; this tells the model which entity type the property refers to. In this way, the model can return properties from several entity types in one single call.

    schema = {    "properties": {        "person_name": {"type": "string"},        "person_height": {"type": "integer"},        "person_hair_color": {"type": "string"},        "dog_name": {"type": "string"},        "dog_breed": {"type": "string"},    },    "required": ["person_name", "person_height"],}

    inp = """Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.Alex's dog Frosty is a labrador and likes to play hide and seek.        """

    chain = create_extraction_chain(schema, llm)

People attributes and dog attributes were correctly extracted from the text in the same call

    chain.run(inp)

        [{'person_name': 'Alex',      'person_height': 5,      'person_hair_color': 'blonde',      'dog_name': 'Frosty',      'dog_breed': 'labrador'},     {'person_name': 'Claudia',      'person_height': 6,      'person_hair_color': 'brunette'}]

Unrelated entities[​](#unrelated-entities "Direct link to Unrelated entities")
------------------------------------------------------------------------------

What if our entities are unrelated? In that case, the model will return the unrelated entities in different dictionaries, allowing us to successfully extract several unrelated entity types in the same call.

Notice that we use `required: []`: we need to allow the model to return **only** person attributes or **only** dog attributes for a single entity (person or dog)

    schema = {    "properties": {        "person_name": {"type": "string"},        "person_height": {"type": "integer"},        "person_hair_color": {"type": "string"},        "dog_name": {"type": "string"},        "dog_breed": {"type": "string"},    },    "required": [],}

    inp = """Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.Willow is a German Shepherd that likes to play with other dogs and can always be found playing with Milo, a border collie that lives close by."""

    chain = create_extraction_chain(schema, llm)

We have each entity in its own separate dictionary, with only the appropriate attributes being returned

    chain.run(inp)

        [{'person_name': 'Alex', 'person_height': 5, 'person_hair_color': 'blonde'},     {'person_name': 'Claudia',      'person_height': 6,      'person_hair_color': 'brunette'},     {'dog_name': 'Willow', 'dog_breed': 'German Shepherd'},     {'dog_name': 'Milo', 'dog_breed': 'border collie'}]

Extra info for an entity[​](#extra-info-for-an-entity "Direct link to Extra info for an entity")
------------------------------------------------------------------------------------------------

What if.. _we don't know what we want?_ More specifically, say we know a few properties we want to extract for a given entity but we also want to know if there's any extra information in the passage. Fortunately, we don't need to structure everything - we can have unstructured extraction as well.

We can do this by introducing another hack, namely the _extra\_info_ attribute - let's see an example.

    schema = {    "properties": {        "person_name": {"type": "string"},        "person_height": {"type": "integer"},        "person_hair_color": {"type": "string"},        "dog_name": {"type": "string"},        "dog_breed": {"type": "string"},        "dog_extra_info": {"type": "string"},    },}

    inp = """Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.Willow is a German Shepherd that likes to play with other dogs and can always be found playing with Milo, a border collie that lives close by."""

    chain = create_extraction_chain(schema, llm)

It is nice to know more about Willow and Milo!

    chain.run(inp)

        [{'person_name': 'Alex', 'person_height': 5, 'person_hair_color': 'blonde'},     {'person_name': 'Claudia',      'person_height': 6,      'person_hair_color': 'brunette'},     {'dog_name': 'Willow',      'dog_breed': 'German Shepherd',      'dog_extra_information': 'likes to play with other dogs'},     {'dog_name': 'Milo',      'dog_breed': 'border collie',      'dog_extra_information': 'lives close by'}]

Pydantic example[​](#pydantic-example "Direct link to Pydantic example")
------------------------------------------------------------------------

We can also use a Pydantic schema to choose the required properties and types and we will set as 'Optional' those that are not strictly required.

By using the `create_extraction_chain_pydantic` function, we can send a Pydantic schema as input and the output will be an instantiated object that respects our desired schema.

In this way, we can specify our schema in the same manner that we would a new class or function in Python - with purely Pythonic types.

    from typing import Optional, Listfrom pydantic import BaseModel, Field

    class Properties(BaseModel):    person_name: str    person_height: int    person_hair_color: str    dog_breed: Optional[str]    dog_name: Optional[str]

    chain = create_extraction_chain_pydantic(pydantic_schema=Properties, llm=llm)

    inp = """Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.Alex's dog Frosty is a labrador and likes to play hide and seek.        """

As we can see, we extracted the required entities and their properties in the required format:

    chain.run(inp)

        [Properties(person_name='Alex', person_height=5, person_hair_color='blonde', dog_breed='labrador', dog_name='Frosty'),     Properties(person_name='Claudia', person_height=6, person_hair_color='brunette', dog_breed=None, dog_name=None)]