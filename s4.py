import xlrd
import sys,os,glob

def convert(arg):
    print("args is==>",arg)    
    glob.glob(arg)
    os.chdir(arg)
    print(os)
    for file in glob.glob("*.xlsx"):
        print("file",file)
        workbook=xlrd.open_workbook(file)
        sh=workbook.sheet_by_name("Sheet1")
        print(" ",sh.nrows)
        print(" ",sh.ncols)
        n=0
        i=0     
        file=open(file + ".txt", "w")
        print(file)
        for n in range(sh.nrows):
            for i in range(sh.ncols):
                data =sh.cell_value(n,i)+" "
                print(data)
                file.write(data+" ")
             

def main(argv=None):
    if argv is None:
         argv = sys.argv
         args = argv[1:]
         for arg in args:
            if os.path.exists(arg):
                convert(arg)

if __name__ == "__main__":
    main()


