f=open("main.tex","r")
g=f.readlines()
f.close()

def comment_remover(texfile_lines):
    h=[]
    for x in texfile_lines:
        if x[0]=="%":
            t=0
        else:
            h.append(x)
    return h

a=comment_remover(g)

f=open("no_comments.tex","w")
f.writelines(a)
f.close()
