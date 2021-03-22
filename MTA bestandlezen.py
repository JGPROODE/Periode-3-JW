invoer=open("C:/Users/ROOJ/GIT/Python/Periode-3-JW/invoer.txt",'r')
eof=False
while eof==False:
    regel=invoer.readline()
    if regel !="":
        if regel !="\n":
            print(regel)
    else:
        print("End of file")
        eof=True
        invoer.close()
            