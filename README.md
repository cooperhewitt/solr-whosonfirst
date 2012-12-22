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

   <field name="name" type="text_general" indexed="true" stored="true" multiValued="true" required="true" />

### name_phonetic

   <field name="name_phonetic" type="phonetic" indexed="true" stored="false" multiValued="true"/>

### name_ws

   <field name="name_ws" type="text_ws" indexed="true" stored="false" multiValued="true"/>

### date_birth
   
   <field name="date_birth" type="tdate" indexed="true" stored="true" multiValued="true"/>

### date_death

   <field name="date_death" type="tdate" indexed="true" stored="true" multiValued="true"/>

### concordances

   <field name="concordances" type="machinetag_hierarchy" indexed="true" stored="true" required="false" multiValued="true" /> 


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

* [Apache Solr](https://lucene.apache.org/solr/)
