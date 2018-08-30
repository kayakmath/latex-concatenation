f=open("main.tex","r")
g=f.read()
f.close()

def inputs(texfile):
    x=0
    while x < len(texfile):
        if texfile[x:x+7]=="\\input{":
            y=""
            z=x+7
            while not(texfile[z]=="}"):
                y+=texfile[z]
                z+=1
            z+=1
            f=open(y+".tex","r")
            h=f.read()
            f.close()
            return texfile[:x]+inputs(h + texfile[z:])
        x+=1
    return texfile

a=inputs(g)
b=open("main_concatenated.tex","w")
b.write(a)
b.close()
