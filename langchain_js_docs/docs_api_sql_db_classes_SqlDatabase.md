SqlDatabase
===========

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Serializable`](/docs/api/load_serializable/classes/Serializable).**SqlDatabase**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`SqlDatabaseOptionsParams`](/docs/api/sql_db/interfaces/SqlDatabaseOptionsParams)
*   [`SqlDatabaseDataSourceParams`](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> `Protected` **new SqlDatabase**(`fields`: [`SqlDatabaseDataSourceParams`](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams)): [`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`SqlDatabaseDataSourceParams`](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams)

#### Returns[​](#returns "Direct link to Returns")

[`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase)

#### Overrides[​](#overrides "Direct link to Overrides")

[Serializable](/docs/api/load_serializable/classes/Serializable).[constructor](/docs/api/load_serializable/classes/Serializable#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/sql\_db.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L39)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### allTables[​](#alltables "Direct link to allTables")

> **allTables**: `SqlTable`\[\] = `[]`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/sql\_db.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L31)

### appDataSource[​](#appdatasource "Direct link to appDataSource")

> **appDataSource**: `DataSource`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[SqlDatabaseDataSourceParams](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams).[appDataSource](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams#appdatasource)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/sql\_db.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L29)

### appDataSourceOptions[​](#appdatasourceoptions "Direct link to appDataSourceOptions")

> **appDataSourceOptions**: `DataSourceOptions`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[SqlDatabaseOptionsParams](/docs/api/sql_db/interfaces/SqlDatabaseOptionsParams).[appDataSourceOptions](/docs/api/sql_db/interfaces/SqlDatabaseOptionsParams#appdatasourceoptions)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/sql\_db.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L27)

### ignoreTables[​](#ignoretables "Direct link to ignoreTables")

> **ignoreTables**: `string`\[\] = `[]`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[SqlDatabaseDataSourceParams](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams).[ignoreTables](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams#ignoretables)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/sql\_db.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L35)

### includesTables[​](#includestables "Direct link to includesTables")

> **includesTables**: `string`\[\] = `[]`

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[SqlDatabaseDataSourceParams](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams).[includesTables](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams#includestables)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/sql\_db.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L33)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_kwargs](/docs/api/load_serializable/classes/Serializable#lc_kwargs)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_namespace](/docs/api/load_serializable/classes/Serializable#lc_namespace)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/sql\_db.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L21)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_serializable](/docs/api/load_serializable/classes/Serializable#lc_serializable)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### sampleRowsInTableInfo[​](#samplerowsintableinfo "Direct link to sampleRowsInTableInfo")

> **sampleRowsInTableInfo**: `number` = `3`

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[SqlDatabaseDataSourceParams](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams).[sampleRowsInTableInfo](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams#samplerowsintableinfo)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/sql\_db.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L37)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

Serializable.lc\_aliases

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_aliases](/docs/api/load_serializable/classes/Serializable#lc_aliases)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

Serializable.lc\_attributes

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_attributes](/docs/api/load_serializable/classes/Serializable#lc_attributes)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

Serializable.lc\_secrets

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_secrets](/docs/api/load_serializable/classes/Serializable#lc_secrets)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### getTableInfo()[​](#gettableinfo "Direct link to getTableInfo()")

Get information about specified tables.

Follows best practices as specified in: Rajkumar et al, 2022 ([https://arxiv.org/abs/2204.00498](https://arxiv.org/abs/2204.00498))

If `sample_rows_in_table_info`, the specified number of sample rows will be appended to each table description. This can increase performance as demonstrated in the paper.

> **getTableInfo**(`targetTables`?: `string`\[\]): `Promise`<`string`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`targetTables?`

`string`\[\]

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/sql\_db.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L94)

### run()[​](#run "Direct link to run()")

Execute a SQL command and return a string representing the results. If the statement returns rows, a string of the results is returned. If the statement returns no rows, an empty string is returned.

> **run**(`command`: `string`, `fetch`: "all" | "one" = `"all"`): `Promise`<`string`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

Default value

`command`

`string`

`undefined`

`fetch`

"all" | "one"

`"all"`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/sql\_db.ts:131](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L131)

### serialize()[​](#serialize "Direct link to serialize()")

> **serialize**(): `SerializedSqlDatabase`

#### Returns[​](#returns-6 "Direct link to Returns")

`SerializedSqlDatabase`

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/sql\_db.ts:146](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L146)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-7 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[Serializable](/docs/api/load_serializable/classes/Serializable).[toJSON](/docs/api/load_serializable/classes/Serializable#tojson)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/sql\_db.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L23)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-8 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[toJSONNotImplemented](/docs/api/load_serializable/classes/Serializable#tojsonnotimplemented)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### fromDataSourceParams()[​](#fromdatasourceparams "Direct link to fromDataSourceParams()")

> `Static` **fromDataSourceParams**(`fields`: [`SqlDatabaseDataSourceParams`](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams)): `Promise`<[`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`fields`

[`SqlDatabaseDataSourceParams`](/docs/api/sql_db/interfaces/SqlDatabaseDataSourceParams)

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase)\>

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/sql\_db.ts:52](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L52)

### fromOptionsParams()[​](#fromoptionsparams "Direct link to fromOptionsParams()")

> `Static` **fromOptionsParams**(`fields`: [`SqlDatabaseOptionsParams`](/docs/api/sql_db/interfaces/SqlDatabaseOptionsParams)): `Promise`<[`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`fields`

[`SqlDatabaseOptionsParams`](/docs/api/sql_db/interfaces/SqlDatabaseOptionsParams)

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<[`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase)\>

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/sql\_db.ts:73](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/sql_db.ts#L73)