solr-whosonfirst
==

`solr-whosonfirst` is an experimental Solr 4 core for mapping person names
between institutions using a number of tokenizers and analyzers.

How does it work?
--

The core contains the minimum viable set of data fields for doing concordances
between people from a variety of institutions: collection; collection_id; name
and when available year_birth; year_death.

The value of `name` is then meant to copied (literally, using Solr `copyField`
definitions) to a variety of specialized field definitions. For example the
`name` field is copied to a `name_phonetic` so that you can query the entire
corpus for names that sound alike.

The idea is to compile a broad collection of specialized fields to offer a
variety of ways to compare data sets. The point is not to presume that any one
tokenizer / analyzer will be able to meet everyone's needs but to provide a
common playground in which we might try things out and share tricks and lessons
learned.

For example:

	$> curl 'http://localhost:8984/solr/select?q=name_general:moggridge&wt=json&indent=on&fq=name_general:bill'

	{
		"response":{"numFound":2, "start":0,"docs":[
			{
				"collection_id":"18062553" ,
				"concordances":[
					"wikipedia:id= 1600591",
					"freebase:id=/m/05fpg1"],
				"uri":"x-urn:ch:id=18062553" ,
				"collection":"cooperhewitt" ,
				"name":["Bill Moggridge"],
				"_version_":1423275305600024577},
			{
				"collection_id":"OL3253093A" ,
				"uri":"x-urn:ol:id=OL3253093A" ,
				"collection":"openlibrary" ,
				"name":["Bill Moggridge"],
				"_version_":1423278698929324032}]
		}
	}

Or:

	$> http://localhost:8983/solr/whosonfirst/select?q=name_general:dreyfuss&wt=json&indent=on

	{
		"response":{"numFound":3,"start":0,"docs":[
			{
				"concordances":["ulan:id=500059346"],
				"name":["Dreyfuss, Henry"],
				"uri":"x-urn:imamuseum:id=656174",
				"collection":"imamuseum",
				"collection_id":"656174",
				"year_death":[1972],
				"year_birth":[1904],
				"_version_":1423872453083398149},
			{
				"concordances":["ulan:id=500059346",
						"wikipedia:id=1697559",
						"freebase:id=/m/05p6rp",
						"viaf:id=8198939",
						"ima:id=656174"],
				"name":["Henry Dreyfuss"],
				"uri":"x-urn:ch:id=18041501",
				"collection":"cooperhewitt",
				"collection_id":"18041501",
				"_version_":1423872563648397315},
			{
				"concordances":["wikipedia:id=1697559",
						"moma:id=1619"],
				"name":["Henry Dreyfuss Associates"],
				"uri":"x-urn:ch:id=18041029",
				"collection":"cooperhewitt",
				"collection_id":"18041029",
				"_version_":1423872563567656970}]
			}
	}

And so on. Queries can be made more complex by filtering, or comparing dates, or
by institution or by querying the `concordances_machinetags` related fields
described below. That's your business.

Sample data files and tools for importing them in to the `whosonfirst` Solr core
are available separately in the
[solr-whosonfirst-data](https://github.com/cooperhewitt/solr-whosonfirst-data)
repository.

How do I install it?
--

`solr-whosonfirst` does not come with a copy of Solr. Installing and configuring
a Solr server is left as an exercise to the reader (don't worry there's lot of
good documentation for Solr and so long as you're not trying to do anything
fancy it's all pretty straightforward).

In your `solr.xml` config file add the following line:

	<core name="whosonfirst" instanceDir="/path/to/solr-whosonfirst/solr-cores/whosonfirst" />

In your `/path/to/solr-whosonfirst/solr-cores/whosonfirst/conf` directory do one
of the following:

	$> cp schema.xml.example schema.xml

Or:

	$> ln -s schema.xml.example schema.xml

The point being: Your `schema.xml` file is your own and is explicitly excluded
from being checked-in to the `solr-whosonfirst` repository. If you've got a
handy new tokenizer/analyzer that you'd like to share with the community add it
to the `schema.xml.example` file.

**Important**: Any data you add to the `solr-whosonfirst` core is stored in the
`solr-cores/whosonfirst/data` directory whose contents are explicitly excluded
from being checked in this Git repository.

The (default) schema
--

### uri

	<field name="uri" type="string" indexed="true" stored="true" required="true" />

For example:

	"uri":"x-urn:ch:id=18062553"

_This is the primary key for each record._

### collection

	<field name="collection" type="string" indexed="true" stored="true" required="true" multiValued="false" /> 

For example:

	"collection":"cooperhewitt"

### collection_id

	<field name="collection_id" type="string" indexed="true" stored="true" required="true" multiValued="false" /> 

For example:

	"collection_id":"18062553"

### name

	<field name="name" type="string" indexed="true" stored="true" multiValued="true" required="true" />

For example:

	"name":["Bill Moggridge"]

### name_general _derived_

	<field name="name_general" type="name_general" indexed="true" stored="false" multiValued="true"/>

This is a copy field derived from `name` and is indexed by not stored.

### name_phonetic _derived_

	<field name="name_phonetic" type="phonetic" indexed="true" stored="false" multiValued="true"/>

This is a copy field derived from `name` and is indexed by not stored.

### year_birth _optional_
   
	<field name="date_birth" type="tint" indexed="true" stored="true" multiValued="true"/>

For example:

	"year_birth": "1943"

### date_death _optional_

	<field name="year_death" type="tint" indexed="true" stored="true" multiValued="true"/>

For example:

	"date_death": "2012"

### concordances _optional_

	<field name="concordances" type="string" indexed="false" stored="true" required="false" multiValued="true" /> 

For example:

	"concordances":["wikipedia:id= 1600591", "freebase:id=/m/05fpg1"]

This field is _not_ indexed as is left to individual applications to use it as
they see fit. If you want to query known concordances use the
`concordances_machinetags` and `concordances_machinetags_hierarchy`.

### concordances_machinetags  _optional_

	<field name="concordances_machinetags" type="machinetags" indexed="true" stored="false" multiValued="true" />

This is not a copy field but is a list derived by `concordances` and expected to
generated in code. These values are indexed but not stored. 

The `concordances_machinetags` field stores all the possible combinations that
you might use to query a machinetag. Because some of the characters used to
encode machinetags conflict with reserved characters in Solr each token needs to
also be encoded using "magic 8s". It ain't pretty but it works.

For example, given the machinetag `flickr:user=straup` you'd end up storing the
following: 

* raw: `flickr:` encoded: `flickr8c` – anything whose namespace is `flickr`

* raw: `flickr:user=` encoded: `flickr8cuser8e` - anything whose namespace is `flickr` with the predicate `user`

* raw: `flickr:user=straup` encoded: `flickr8cuser8estraup` - anything with an exact match

* raw: `=straup` encoded: `8estraup` - anything whose value is `straup`

* raw: `:user=`	encoded: `8cuser8e` - anything with a predicate that is `user`

* raw: `:user=straup` encoded: `8cuser8estraup` - anything with a predicate that is `user` and a value of `straup`

If you want working code (or just a reference implementation) for machinetags
and "magic 8s" take a look at the
[py-machinetag](https://github.com/straup/py-machinetag) repository.

There are links below in the `See also` section for anyone wanting to read up on
the history, theory and practice of machinetags.

### concordances_machinetags_hierarchy _optional_

	<field name="concordances_machinetags_hierarchy" type="machinetags_hierarchy" indexed="true" stored="false" multiValued="true" />

This is not a copy field but is a list derived by `concordances` and expected to
generated in code. These values are indexed but not stored. 

_TBW: "SolrPathHierarchyTokenizerFactory"_

See also
--

* [solr-whosonfirst-data](https://github.com/cooperhewitt/solr-whosonfirst-data)

* [Apache Solr](https://lucene.apache.org/solr/)

* [A machinetags reading list](https://github.com/straup/machinetags-readinglist)

