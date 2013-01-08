solr-whosonfirst
==

**THIS IS A WORK IN PROGRESS**

`solr-whosonfirst` is an experimental Solr 4 core for mapping person names
between institutions using a number of tokenizers and analyzers.

How does it work?
--

The (default) schema
--

### uri

   <field name="uri" type="string" indexed="true" stored="true" required="true" />

### collection

   <field name="collection" type="string" indexed="true" stored="true" required="true" multiValued="false" /> 

### collection_id

   <field name="collection_id" type="string" indexed="true" stored="true" required="true" multiValued="false" /> 

### name

   <field name="name" type="string" indexed="true" stored="true" multiValued="true" required="true" />

### name_general

   <field name="name_general" type="name_general" indexed="true" stored="false" multiValued="true"/>

This is a copy field derived from `name`.

### name_phonetic (copy field from `name`)

   <field name="name_phonetic" type="phonetic" indexed="true" stored="false" multiValued="true"/>

This is a copy field derived from `name`.

### date_birth
   
   <field name="date_birth" type="tdate" indexed="true" stored="true" multiValued="true"/>

### date_death

   <field name="date_death" type="tdate" indexed="true" stored="true" multiValued="true"/>

### concordances

   <field name="concordances" type="string" indexed="false" stored="true" required="false" multiValued="true" /> 

### concordances_machinetags

   <field name="concordances_machinetags" type="machinetags" indexed="true" stored="false" multiValued="true" />

_TBW: "lazy8s"_

### concordances_machinetags_hierarchy

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
