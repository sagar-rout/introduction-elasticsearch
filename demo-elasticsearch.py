from datetime import datetime
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(
)  # This will connect with default elasticsearch connection http://localhost:9200

INDEX_NAME = 'favourite-foods'

# Create index in the elasticsearch

index_settings = {
    "settings": {
        "index": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    }
}

# if index is already there and you are trying to create index with same name,
# elasticsearch will not like it and throw
# raise HTTP_EXCEPTIONS.get(status_code, TransportError)(
# elasticsearch.exceptions.RequestError: RequestError(400, 'resource_already_exists_exception', 'index [favourite-foods/379Q_MsQS1yqPohqXylDPg] already exists')

try:
    es.indices.create(index=INDEX_NAME, body=index_settings)
except:
    print('Indices is already there.')
    pass

# Index(Store) this document
sagar_doc = {
    'user_name': 'Sagar',
    'text': 'banana bread and espresso',
    'timestamp': datetime.now()
}

divya_doc = {
    'user_name': 'Divya',
    'text': 'Cheese cake and cappuccino',
    'timestamp': datetime.now()
}

geetika_doc = {
    'user_name': 'Geetika',
    'text': 'Tea',
    'timestamp': datetime.now()
}

# Index data in the

sagar_res = es.index(
    index=INDEX_NAME, id=1, body=sagar_doc
)  # Don't use custom id until you want to use id for searching because it slows down indexing
divya_res = es.index(index=INDEX_NAME, id=2, body=divya_doc)
geetika_res = es.index(index=INDEX_NAME, id=3, body=geetika_doc)

# Search the document using filter
print('Search the document using filter')
body = {"query": {"match": {"text": "banana"}}}
print('Who likes banana bread ? ')

searched_data = es.search(index=INDEX_NAME, body=body)
print(json.dumps(searched_data))

# Search the document using _id
print('Search the document using _id')
document_by_id = es.get(index=INDEX_NAME, id=2)
print(json.dumps(document_by_id))
