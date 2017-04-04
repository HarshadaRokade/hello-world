from yapsy.IPlugin import IPlugin
from configparser import ConfigParser
from xml.etree.ElementTree import ElementTree
import os,glob
class PluginOne(IPlugin):
    def print_name(self):
        print("This is plugin 1")
        parser = ConfigParser()
        print(parser.read('C:\Python34\example\c1.ini'))
        print(parser.get('path', 'dirpath'))
        path=parser.get('path', 'dirpath')
        return path

    def convert_from_xml(self,f):
        print(f)
        glob.glob(f)
        os.chdir(f)
        for file in glob.glob("*.xml"):
        	with open(file, 'r') as f:
        		xcontent=ElementTree()
        		xcontent.parse(file)
        		doc = [xcontent.find("title").text, xcontent.find("content").text, xcontent.find("keywords").text]
        		out = open(file + ".txt", "w")
        		out.write("\n\n".join(doc))
        		return True



