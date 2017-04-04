import sys
import os
from xml.etree.ElementTree import ElementTree

def Readthexml(f):
    """Read the file from the argument list and dump the title contents and keywords"""
    xcontent = ElementTree()
    xcontent.parse(f)
    doc = [xcontent.find("title").text, xcontent.find("content").text, xcontent.find("keywords").text]
    out = open(f + ".txt", "w")
    out.write("\n\n".join(doc))
    return True

def main(argv=None):
    if argv is None:
        argv = sys.argv
        args = argv[1:]
        for arg in args:
            if os.path.exists(arg):
                Readthexml(arg)

if __name__ == "__main__":
    main()
