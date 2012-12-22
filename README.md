solr-whosonfirst
==

**THIS IS A WORK IN PROGRESS**

`solr-whosonfirst` is an experimental Solr 4 core for mapping person names
between institutions using a number of tokenizers and analyzers.

INSTALL
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
