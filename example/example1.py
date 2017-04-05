import elasticsearch
import requests
import base64
import glob
import os
import sys
from yapsy.PluginManager import PluginManager
import logging
logging.basicConfig(level=logging.DEBUG)
from yapsy.IPlugin import IPlugin

es = elasticsearch.Elasticsearch() # by default it takes 9200
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


def main():   
    global p
    #  Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()
    # Loop round the plugins and print their names.
    for plugin in manager.getAllPlugins():
        p=plugin.plugin_object.print_name()
        print("path is:",p)
        plugin.plugin_object.convert_from_xml(p)  
        plugin.plugin_object.convert_from_xlsx(p)
        

   
if __name__ == "__main__":
    main()

glob.glob(p)
os.chdir(p) 
for file in glob.glob("*.txt"):
        with open(file, 'r') as f:
        	data = base64.b64encode(bytes(f.read(),'utf-8')).decode('ascii');
        	result2 = es.index(index='my_index', doc_type='my_type', pipeline='attachment',body={'data': data})
print(result2)
