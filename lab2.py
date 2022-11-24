f = open("code.txt", "r")
s = open("symbolTable.txt", "w")
p = open("pif.txt", "w")

tokenTable = {"identifier" : 0, "constant" : 1, "integer" : 2, "main" : 3,
            "(" : 4, ")" : 5, "{" : 6, ";" : 7, "=": 8, "+": 9,
            "print" : 10, "}" : 11, "string" : 12, "function" : 13, 
            "boolean" : 14, ":" : 15, "<=" : 16, "%" : 17, "==" : 18,
            "then" : 19, "False" : 20, "True" : 21, "return" : 22, 
            ',' : 23, "getinput" : 24, "var" : 25, "if" : 26, 
            "for" : 27, "to" : 28, "displayoutput" : 29, "program" : 30}

reservedWords = {"integer", "main", "string", "print", "function", "boolean", 
                    "then", "False", "True", "return", "getinput", "var", "if",
                    "for", "to", "displayoutput", "program"}

operators = {'=', '+', '%', '=='}

separators = {';', '(', ')', '{', '}', ',', ':', '<=', ','}


pif = {}
symbolTable = {}
position = 0  # position in the ST
count = 1     # used to keep track of the line we are at
ok = 0        # checks if the token is valid


for line in f:
    if ok:
        break

    list = line.split() # we split the file into lines and start analysing each one of them
    
    for elem in list:
        if elem in reservedWords or elem in operators or elem in separators:
            pif[elem] = [tokenTable[elem], -1]
            toWrite = elem + " " + str(pif[elem]) + "\n"
            p.write(toWrite)

        elif elem.isidentifier():
            if elem not in symbolTable.keys():
                symbolTable[elem] = position
                position += 1
                symbolToWrite = elem + " " + str(symbolTable[elem]) + "\n"
                s.write(symbolToWrite)
                p.write(symbolToWrite)

            pif[elem] = [0, symbolTable[elem]]
            toWrite = elem + " " + str(pif[elem]) + "\n"
            p.write(toWrite)

        elif (elem.startswith('"') and elem.endswith('"')) or (elem.startswith("-") and elem[1:].isnumeric()) or elem.isnumeric():
            if elem not in symbolTable.keys():
                symbolTable[elem] = position
                position += 1
                symbolToWrite = elem + " " + str(symbolTable[elem]) + "\n"
                s.write(symbolToWrite)
                p.write(symbolToWrite)

            pif[elem] = [1, symbolTable[elem]]
            toWrite = elem + " " + str(pif[elem]) + "\n"
            p.write(toWrite)

        else:
            print("Lexical error in line ", count, " at token ", elem)
            ok = 1
            break

    count += 1      # we go on to the next line


print("Program Internal Form (PIF):\n")
for elem in pif:
    print(elem," ", pif[elem])

print("\nSymbol Table:\n")
for elem in symbolTable:
    print(elem, " ", symbolTable[elem])

f.close()
s.close()
p.close()
