GraphSparqlQAChain
==================

Graph databases are an excellent choice for applications based on network-like models. To standardize the syntax and semantics of such graphs, the W3C recommends Semantic Web Technologies, cp. [Semantic Web](https://www.w3.org/standards/semanticweb/). [SPARQL](https://www.w3.org/TR/sparql11-query/) serves as a query language analogously to SQL or Cypher for these graphs. This notebook demonstrates the application of LLMs as a natural language interface to a graph database by generating SPARQL.\\ Disclaimer: To date, SPARQL query generation via LLMs is still a bit unstable. Be especially careful with UPDATE queries, which alter the graph.

There are several sources you can run queries against, including files on the web, files you have available locally, SPARQL endpoints, e.g., [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), and [triple stores](https://www.w3.org/wiki/LargeTripleStores).

    from langchain.chat_models import ChatOpenAIfrom langchain.chains import GraphSparqlQAChainfrom langchain.graphs import RdfGraph

    graph = RdfGraph(    source_file="http://www.w3.org/People/Berners-Lee/card",    standard="rdf",    local_copy="test.ttl",)

Note that providing a `local_file` is necessary for storing changes locally if the source is read-only.

Refresh graph schema information[](#refresh-graph-schema-information "Direct link to Refresh graph schema information")
------------------------------------------------------------------------------------------------------------------------

If the schema of the database changes, you can refresh the schema information needed to generate SPARQL queries.

    graph.load_schema()

    graph.get_schema

        In the following, each IRI is followed by the local name and optionally its description in parentheses.     The RDF graph supports the following node types:    <http://xmlns.com/foaf/0.1/PersonalProfileDocument> (PersonalProfileDocument, None), <http://www.w3.org/ns/auth/cert#RSAPublicKey> (RSAPublicKey, None), <http://www.w3.org/2000/10/swap/pim/contact#Male> (Male, None), <http://xmlns.com/foaf/0.1/Person> (Person, None), <http://www.w3.org/2006/vcard/ns#Work> (Work, None)    The RDF graph supports the following relationships:    <http://www.w3.org/2000/01/rdf-schema#seeAlso> (seeAlso, None), <http://purl.org/dc/elements/1.1/title> (title, None), <http://xmlns.com/foaf/0.1/mbox_sha1sum> (mbox_sha1sum, None), <http://xmlns.com/foaf/0.1/maker> (maker, None), <http://www.w3.org/ns/solid/terms#oidcIssuer> (oidcIssuer, None), <http://www.w3.org/2000/10/swap/pim/contact#publicHomePage> (publicHomePage, None), <http://xmlns.com/foaf/0.1/openid> (openid, None), <http://www.w3.org/ns/pim/space#storage> (storage, None), <http://xmlns.com/foaf/0.1/name> (name, None), <http://www.w3.org/2000/10/swap/pim/contact#country> (country, None), <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> (type, None), <http://www.w3.org/ns/solid/terms#profileHighlightColor> (profileHighlightColor, None), <http://www.w3.org/ns/pim/space#preferencesFile> (preferencesFile, None), <http://www.w3.org/2000/01/rdf-schema#label> (label, None), <http://www.w3.org/ns/auth/cert#modulus> (modulus, None), <http://www.w3.org/2000/10/swap/pim/contact#participant> (participant, None), <http://www.w3.org/2000/10/swap/pim/contact#street2> (street2, None), <http://www.w3.org/2006/vcard/ns#locality> (locality, None), <http://xmlns.com/foaf/0.1/nick> (nick, None), <http://xmlns.com/foaf/0.1/homepage> (homepage, None), <http://creativecommons.org/ns#license> (license, None), <http://xmlns.com/foaf/0.1/givenname> (givenname, None), <http://www.w3.org/2006/vcard/ns#street-address> (street-address, None), <http://www.w3.org/2006/vcard/ns#postal-code> (postal-code, None), <http://www.w3.org/2000/10/swap/pim/contact#street> (street, None), <http://www.w3.org/2003/01/geo/wgs84_pos#lat> (lat, None), <http://xmlns.com/foaf/0.1/primaryTopic> (primaryTopic, None), <http://www.w3.org/2006/vcard/ns#fn> (fn, None), <http://www.w3.org/2003/01/geo/wgs84_pos#location> (location, None), <http://usefulinc.com/ns/doap#developer> (developer, None), <http://www.w3.org/2000/10/swap/pim/contact#city> (city, None), <http://www.w3.org/2006/vcard/ns#region> (region, None), <http://xmlns.com/foaf/0.1/member> (member, None), <http://www.w3.org/2003/01/geo/wgs84_pos#long> (long, None), <http://www.w3.org/2000/10/swap/pim/contact#address> (address, None), <http://xmlns.com/foaf/0.1/family_name> (family_name, None), <http://xmlns.com/foaf/0.1/account> (account, None), <http://xmlns.com/foaf/0.1/workplaceHomepage> (workplaceHomepage, None), <http://purl.org/dc/terms/title> (title, None), <http://www.w3.org/ns/solid/terms#publicTypeIndex> (publicTypeIndex, None), <http://www.w3.org/2000/10/swap/pim/contact#office> (office, None), <http://www.w3.org/2000/10/swap/pim/contact#homePage> (homePage, None), <http://xmlns.com/foaf/0.1/mbox> (mbox, None), <http://www.w3.org/2000/10/swap/pim/contact#preferredURI> (preferredURI, None), <http://www.w3.org/ns/solid/terms#profileBackgroundColor> (profileBackgroundColor, None), <http://schema.org/owns> (owns, None), <http://xmlns.com/foaf/0.1/based_near> (based_near, None), <http://www.w3.org/2006/vcard/ns#hasAddress> (hasAddress, None), <http://xmlns.com/foaf/0.1/img> (img, None), <http://www.w3.org/2000/10/swap/pim/contact#assistant> (assistant, None), <http://xmlns.com/foaf/0.1/title> (title, None), <http://www.w3.org/ns/auth/cert#key> (key, None), <http://www.w3.org/ns/ldp#inbox> (inbox, None), <http://www.w3.org/ns/solid/terms#editableProfile> (editableProfile, None), <http://www.w3.org/2000/10/swap/pim/contact#postalCode> (postalCode, None), <http://xmlns.com/foaf/0.1/weblog> (weblog, None), <http://www.w3.org/ns/auth/cert#exponent> (exponent, None), <http://rdfs.org/sioc/ns#avatar> (avatar, None)    

Querying the graph[](#querying-the-graph "Direct link to Querying the graph")
------------------------------------------------------------------------------

Now, you can use the graph SPARQL QA chain to ask questions about the graph.

    chain = GraphSparqlQAChain.from_llm(    ChatOpenAI(temperature=0), graph=graph, verbose=True)

    chain.run("What is Tim Berners-Lee's work homepage?")

                > Entering new GraphSparqlQAChain chain...    Identified intent:    SELECT    Generated SPARQL:    PREFIX foaf: <http://xmlns.com/foaf/0.1/>    SELECT ?homepage    WHERE {        ?person foaf:name "Tim Berners-Lee" .        ?person foaf:workplaceHomepage ?homepage .    }    Full Context:    []        > Finished chain.    "Tim Berners-Lee's work homepage is http://www.w3.org/People/Berners-Lee/."

Updating the graph[](#updating-the-graph "Direct link to Updating the graph")
------------------------------------------------------------------------------

Analogously, you can update the graph, i.e., insert triples, using natural language.

    chain.run(    "Save that the person with the name 'Timothy Berners-Lee' has a work homepage at 'http://www.w3.org/foo/bar/'")

                > Entering new GraphSparqlQAChain chain...    Identified intent:    UPDATE    Generated SPARQL:    PREFIX foaf: <http://xmlns.com/foaf/0.1/>    INSERT {        ?person foaf:workplaceHomepage <http://www.w3.org/foo/bar/> .    }    WHERE {        ?person foaf:name "Timothy Berners-Lee" .    }        > Finished chain.    'Successfully inserted triples into the graph.'

Let's verify the results:

    query = (    """PREFIX foaf: <http://xmlns.com/foaf/0.1/>\n"""    """SELECT ?hp\n"""    """WHERE {\n"""    """    ?person foaf:name "Timothy Berners-Lee" . \n"""    """    ?person foaf:workplaceHomepage ?hp .\n"""    """}""")graph.query(query)

        [(rdflib.term.URIRef('https://www.w3.org/'),),     (rdflib.term.URIRef('http://www.w3.org/foo/bar/'),)]