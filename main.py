i = 0
serverlist = []
while i < 5:
    server_name = input("Please input server names: ")
    CI_NAME = "\'CI Name*\'" + " = " + "\"" + server_name + "\""
    serverlist.append(CI_NAME)
    i+= 1
    
for i in range(len(serverlist)):
    if i != len(serverlist) - 1: 
        print(serverlist[i], end=" OR ")
    else:
        print(serverlist[i], end = "")
