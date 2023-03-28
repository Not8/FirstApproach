objeto = "#### #Hello!# ####"


def convertir(objeto) -> str:
    for i in enumerate(objeto.strip()):
        if objeto[i[0]] == " " and objeto[i[0]-1] == "#":
            return ("<h" + str(i[0]) + ">" + objeto[i[0]+1:len(objeto)-i[0]-1] + "<h" + str(i[0]) + ">")


print(convertir(objeto))
