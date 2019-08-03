file="D:\Mahi\\todo.txt"
complete="D:\\Mahi\\complete.txt"

def readFile():
    with open(file,"r") as f:
        todol = f.read().splitlines()
    return todol

def readcomplete():
    with open(complete,"r") as f:
        completel = f.read().splitlines()
    return completel

def writefile(todol):
    with open(file,"w") as f:
        for i in range(len(todol)):
            f.write(todol[i])
            f.write("\n")

def writecomplete(cl):
    with open(complete,"w") as f:
        for i in range(len(cl)):
            f.write(cl[i])
            f.write("\n")
