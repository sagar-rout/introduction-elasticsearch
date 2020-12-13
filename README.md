# Elasticsearch

It is an open source search and analytics engine based on [Apache Lucene](https://lucene.apache.org/). [Elasticsearch](https://www.elastic.co/what-is/elasticsearch) is centre for Elastic stack which contains tools like kibana, logstash and beats like metricbeat and filebeat.

## Installation 

You can install elasticsearch many ways :
- Using package manager - deb, rpm
- Using binaries, exe or msi (windows), brew (mac os) 

Please go through this [link](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) and configure as per your need.

I recommended docker for local development and learning. I find it clean and easier to maintain.

```bash
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.1
```

This will download elasticsearch 7.10.1 from docker hub and install single node of elasticsearch. This is not recommended for production system. For production system, multiple nodes are mandatory for propert replication and sharding.


## Elasticsearch basic concepts

- Index
- Sharding : No of shards should be less than equal to data nodes
- Replication
- Index's mapping settings
- Master Node and data nodes - What type of instance we should choose ? For master node, we should choose compute type instance and for data nodes - memory intensive instances.

## Index Creation
Index in elasticsearch is like logical storage unit. It is like a database in RDBMS. 

For more info : https://www.elastic.co/blog/what-is-an-elasticsearch-index

```java

PUT /index-name
{
  "settings": {
    "index": {
      "number_of_shards": 3, // best practice it should be less than equal to data nodes 
      "number_of_replicas": 2
    }
  }
}
```

## Mapping

- Dynamic Mapping : When elasticsearch creates mapping based on the first time entered data.

- Custom/static Mapping : When user defines mapping and elasticsearch stores this information before we index data.