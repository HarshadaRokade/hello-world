import elasticsearch
import requests
import base64
import os
import glob
import sys


url='http://www.cbu.edu.zm/downloads/pdf-sample.pdf'
response=requests.get(url)
with open('Downloads','wb') as f:
    f.write(response.content)

    es = elasticsearch.Elasticsearch()
    print(es.cat.health())
body = {
  "description" : "Extract attachment information",
  "processors" : [
    {
      "attachment" : {
        "field" : "data"
      }
    }
  ]
}
es.index(index='_ingest', doc_type='pipeline', id='attachment', body=body)

result1 = es.index(index='my_index1', doc_type='my_type', pipeline='attachment',
                  body={'data': "e1xydGYxXGFuc2kNCkxvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0DQpccGFyIH0="})
print(result1)

print('Argument List:',sys.argv[1])
dname=sys.argv[1];

glob.glob(dname)

print(glob.glob("C:\Python3\dir\*.txt"))
for file in glob.glob("*.txt"):
    print(file)

with open(file,'r') as f:
            data=base64.b64encode(bytes(f.read(),'utf-8')).decode('ascii');
            print(data)
            result2 = es.index(index='my_index1', doc_type='my_type', pipeline='attachment',body={'data': data})
print(result2)
