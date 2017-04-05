from yapsy.IPlugin import IPlugin
from configparser import ConfigParser
from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
import os,glob,xlrd
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
                	tree=ET.parse(file)
                	doc=ET.tostring(tree.getroot(), encoding='utf-8',method='text')
                	print("result is",doc)
                	print("after ",doc.splitlines())
                	out = open(file + ".txt", "w")
                	out.write(str(doc))
                	return True
 
    def convert_from_xlsx(self,arg):
        print("args is==>",arg)    
        glob.glob(arg)
        os.chdir(arg)
        print(os)
        for file in glob.glob("*.xlsx"):
            print("filename==>",file)
            workbook=xlrd.open_workbook(file)
           #print(workbook.nsheet)
            arr=workbook.sheet_names()
            print(arr) 
            out=open(file+".txt","w") 
            for sheet in arr:            
                arr=workbook.sheet_names()
                sh=workbook.sheet_by_name(sheet)
                print("row is",sh.nrows)
                print("column is",sh.ncols)
                print(sheet)
                n=0
                i=0     
                for n in range(sh.nrows):
                    out.write("\t")
                    for i in range(sh.ncols):
                        data =sh.cell_value(n,i)
                        print(data)
                        out.write(str(data))
                        out.write("\t")
                    
  

  
    