solr-whosonfirst
==

**THIS IS A WORK IN PROGRESS**

`solr-whosonfirst` is an experimental Solr 4 core for mapping person names
between institutions using a number of tokenizers and analyzers.

How does it work?
--

TBW.

For example:

	$> curl 'http://localhost:8984/solr/select?q=name_general:moggridge&wt=json&indent=on&fq=name_general:bill'

	{
		"response":{"numFound":2, "start":0,"docs":[
			{
				"collection_id":"18062553" ,
				"concordances":["wikipedia:id= 1600591",
				"freebase:id=/m/05fpg1"],
				"uri":"x-urn:ch:id=18062553" ,
				"collection":"cooper-hewitt" ,
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

The (default) schema
--

### uri

   <field name="uri" type="string" indexed="true" stored="true" required="true" />

For example:

	"uri":"x-urn:ch:id=18062553"

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

### name_general

   <field name="name_general" type="name_general" indexed="true" stored="false" multiValued="true"/>

This is a copy field derived from `name` and is indexed by not stored.

### name_phonetic (copy field from `name`)

   <field name="name_phonetic" type="phonetic" indexed="true" stored="false" multiValued="true"/>

This is a copy field derived from `name` and is indexed by not stored.

### date_birth _optional_
   
   <field name="date_birth" type="tdate" indexed="true" stored="true" multiValued="true"/>

### date_death _optional_

   <field name="date_death" type="tdate" indexed="true" stored="true" multiValued="true"/>

### concordances _optional_

   <field name="concordances" type="string" indexed="false" stored="true" required="false" multiValued="true" /> 

For example:

	"concordances":["wikipedia:id= 1600591", "freebase:id=/m/05fpg1"]

### concordances_machinetags  _optional_

   <field name="concordances_machinetags" type="machinetags" indexed="true" stored="false" multiValued="true" />

_TBW: "lazy8s"_ (and Flickr machine tags)

### concordances_machinetags_hierarchy _optional_

   <field name="concordances_machinetags_hierarchy" type="machinetags_hierarchy" indexed="true" stored="false" multiValued="true" />

_TBW: "SolrPathHierarchyTokenizerFactory"_

How do I install it?
--

TBW.

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


See also
--

* [solr-whosonfirst-data](https://github.com/cooperhewitt/solr-whosonfirst-data)

* [Apache Solr](https://lucene.apache.org/solr/)

* [Machine tags (at Flickr)](http://www.flickr.com/groups/api/discuss/72157594497877875/)
