SerpAPIParameters
=================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseParameters`.**SerpAPIParameters**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### q[](#q "Direct link to q")

> **q**: `string`

Search Query Parameter defines the query you want to search. You can use anything that you would use in a regular Google search. e.g. `inurl:`, `site:`, `intitle:`. We also support advanced search query parameters such as as\_dt and as\_eq. See the [full list](https://serpapi.com/advanced-google-query-parameters) of supported advanced search query parameters.

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:47](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L47)

### as\_dt?[](#as_dt "Direct link to as_dt?")

> **as\_dt**: `string`

as\_dt Parameter controls whether to include or exclude results from the site named in the as\_sitesearch parameter.

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:136](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L136)

### as\_epq?[](#as_epq "Direct link to as_epq?")

> **as\_epq**: `string`

as\_epq Parameter identifies a phrase that all documents in the search results must contain. You can also use the [phrase search](https://developers.google.com/custom-search/docs/xml_results#PhraseSearchqt) query term to search for a phrase.

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:144](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L144)

### as\_eq?[](#as_eq "Direct link to as_eq?")

> **as\_eq**: `string`

as\_eq Parameter identifies a word or phrase that should not appear in any documents in the search results. You can also use the [exclude query](https://developers.google.com/custom-search/docs/xml_results#Excludeqt) term to ensure that a particular word or phrase will not appear in the documents in a set of search results.

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L153)

### as\_lq?[](#as_lq "Direct link to as_lq?")

> **as\_lq**: `string`

as\_lq Parameter specifies that all search results should contain a link to a particular URL. You can also use the [link:](https://developers.google.com/custom-search/docs/xml_results#BackLinksqt) query term for this type of query.

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:161](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L161)

### as\_nhi?[](#as_nhi "Direct link to as_nhi?")

> **as\_nhi**: `string`

as\_nhi Parameter specifies the ending value for a search range. Use as\_nlo and as\_nhi to append an inclusive search range.

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:173](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L173)

### as\_nlo?[](#as_nlo "Direct link to as_nlo?")

> **as\_nlo**: `string`

as\_nlo Parameter specifies the starting value for a search range. Use as\_nlo and as\_nhi to append an inclusive search range.

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:167](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L167)

### as\_oq?[](#as_oq "Direct link to as_oq?")

> **as\_oq**: `string`

as\_oq Parameter provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms. You can also use the [Boolean OR](https://developers.google.com/custom-search/docs/xml_results#BooleanOrqt) query term for this type of query.

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:182](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L182)

### as\_q?[](#as_q "Direct link to as_q?")

> **as\_q**: `string`

as\_q Parameter provides search terms to check for in a document. This parameter is also commonly used to allow users to specify additional terms to search for within a set of search results.

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:189](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L189)

### as\_qdr?[](#as_qdr "Direct link to as_qdr?")

> **as\_qdr**: `string`

as\_qdr Parameter requests search results from a specified time period (quick date range). The following values are supported: `d[number]`: requests results from the specified number of past days. Example for the past 10 days: `as_qdr=d10` `w[number]`: requests results from the specified number of past weeks. `m[number]`: requests results from the specified number of past months. `y[number]`: requests results from the specified number of past years. Example for the past year: `as_qdr=y`

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:201](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L201)

### as\_rq?[](#as_rq "Direct link to as_rq?")

> **as\_rq**: `string`

as\_rq Parameter specifies that all search results should be pages that are related to the specified URL. The parameter value should be a URL. You can also use the [related:](https://developers.google.com/custom-search/docs/xml_results#RelatedLinksqt) query term for this type of query.

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:209](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L209)

### as\_sitesearch?[](#as_sitesearch "Direct link to as_sitesearch?")

> **as\_sitesearch**: `string`

as\_sitesearch Parameter allows you to specify that all search results should be pages from a given site. By setting the as\_dt parameter, you can also use it to exclude pages from a given site from your search resutls.

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:216](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L216)

### device?[](#device "Direct link to device?")

> **device**: "desktop" | "tablet" | "mobile"

Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser (currently using iPhones).

#### Inherited from[](#inherited-from "Direct link to Inherited from")

BaseParameters.device

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L22)

### filter?[](#filter "Direct link to filter?")

> **filter**: `string`

Results Filtering Parameter defines if the filters for 'Similar Results' and 'Omitted Results' are on or off. It can be set to `1` (default) to enable these filters, or `0` to disable these filters.

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:243](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L243)

### gl?[](#gl "Direct link to gl?")

> **gl**: `string`

Country Parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the [Google countries page](https://serpapi.com/google-countries) for a full list of supported Google countries.

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:113](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L113)

### google\_domain?[](#google_domain "Direct link to google_domain?")

> **google\_domain**: `string`

Domain Parameter defines the Google domain to use. It defaults to `google.com`. Head to the [Google domains page](https://serpapi.com/google-domains) for a full list of supported Google domains.

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:104](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L104)

### hl?[](#hl "Direct link to hl?")

> **hl**: `string`

Language Parameter defines the language to use for the Google search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). Head to the [Google languages page](https://serpapi.com/google-languages) for a full list of supported Google languages.

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:121](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L121)

### ijn?[](#ijn "Direct link to ijn?")

> **ijn**: `string`

Page Number (images) Parameter defines the page number for [Google Images](https://serpapi.com/images-results). There are 100 images per page. This parameter is equivalent to start (offset) = ijn \* 100. This parameter works only for [Google Images](https://serpapi.com/images-results) (set tbm to `isch`).

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:279](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L279)

### kgmid?[](#kgmid "Direct link to kgmid?")

> **kgmid**: `string`

Google Knowledge Graph ID Parameter defines the id (`KGMID`) of the Google Knowledge Graph listing you want to scrape. Also known as Google Knowledge Graph ID. Searches with kgmid parameter will return results for the originally encrypted search parameters. For some searches, kgmid may override all other parameters except start, and num parameters.

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:88](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L88)

### location?[](#location "Direct link to location?")

> **location**: `string`

Location Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to [/locations.json API](https://serpapi.com/locations-api) if you need more precise control. location and uule parameters can't be used together. Avoid utilizing location when setting the location outside the U.S. when using Google Shopping and/or Google Product API.

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L57)

### lr?[](#lr "Direct link to lr?")

> **lr**: `string`

Set Multiple Languages Parameter defines one or multiple languages to limit the search to. It uses `lang_{two-letter language code}` to specify languages and `|` as a delimiter. (e.g., `lang_fr|lang_de` will only search French and German pages). Head to the [Google lr languages page](https://serpapi.com/google-lr-languages) for a full list of supported languages.

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:130](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L130)

### lsig?[](#lsig "Direct link to lsig?")

> **lsig**: `string`

Additional Google Place ID Parameter that you might have to use to force the knowledge graph map view to show up. You can find the lsig ID by using our [Local Pack API](https://serpapi.com/local-pack) or [Places Results API](https://serpapi.com/places-results). lsig ID is also available via a redirect Google uses within [Google My Business](https://www.google.com/business/).

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:79](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L79)

### ludocid?[](#ludocid "Direct link to ludocid?")

> **ludocid**: `string`

Google Place ID Parameter defines the id (`CID`) of the Google My Business listing you want to scrape. Also known as Google Place ID.

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L69)

### nfpr?[](#nfpr "Direct link to nfpr?")

> **nfpr**: `string`

Exclude Auto-corrected Results Parameter defines the exclusion of results from an auto-corrected query that is spelled wrong. It can be set to `1` to exclude these results, or `0` to include them (default).

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:236](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L236)

### no\_cache?[](#no_cache "Direct link to no_cache?")

> **no\_cache**: `boolean`

Parameter will force SerpApi to fetch the Google results even if a cached version is already present. A cache is served only if the query and all parameters are exactly the same. Cache expires after 1h. Cached searches are free, and are not counted towards your searches per month. It can be set to `false` (default) to allow results from the cache, or `true` to disallow results from the cache. `no_cache` and `async` parameters should not be used together.

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

BaseParameters.no\_cache

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L31)

### num?[](#num "Direct link to num?")

> **num**: `string`

Number of Results Parameter defines the maximum number of results to return. (e.g., `10` (default) returns 10 results, `40` returns 40 results, and `100` returns 100 results).

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:271](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L271)

### safe?[](#safe "Direct link to safe?")

> **safe**: `string`

Adult Content Filtering Parameter defines the level of filtering for adult content. It can be set to `active`, or `off` (default).

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:229](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L229)

### si?[](#si "Direct link to si?")

> **si**: `string`

Google Cached Search Parameters ID Parameter defines the cached search parameters of the Google Search you want to scrape. Searches with si parameter will return results for the originally encrypted search parameters. For some searches, si may override all other parameters except start, and num parameters. si can be used to scrape Google Knowledge Graph Tabs.

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:97](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L97)

### start?[](#start "Direct link to start?")

> **start**: `number`

Result Offset Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `10` is the 2nd page of results, `20` is the 3rd page of results, etc.). Google Local Results only accepts multiples of `20`(e.g. `20` for the second page results, `40` for the third page results, etc.) as the start value.

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:265](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L265)

### tbm?[](#tbm "Direct link to tbm?")

> **tbm**: `string`

Search Type (to be matched) parameter defines the type of search you want to do. It can be set to: `(no tbm parameter)`: regular Google Search, `isch`: [Google Images API](https://serpapi.com/images-results), `lcl` - [Google Local API](https://serpapi.com/local-results) `vid`: [Google Videos API](https://serpapi.com/videos-results), `nws`: [Google News API](https://serpapi.com/news-results), `shop`: [Google Shopping API](https://serpapi.com/shopping-results), or any other Google service.

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:256](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L256)

### tbs?[](#tbs "Direct link to tbs?")

> **tbs**: `string`

Advanced Search Parameters (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. (e.g., advanced search for patents, dates, news, videos, images, apps, or text contents).

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:223](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L223)

### timeout?[](#timeout "Direct link to timeout?")

> **timeout**: `number`

Specify the client-side timeout of the request. In milliseconds.

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

BaseParameters.timeout

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L35)

### uule?[](#uule "Direct link to uule?")

> **uule**: `string`

Encoded Location Parameter is the Google encoded location you want to use for the search. uule and location parameters can't be used together.

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/serpapi.ts#L63)