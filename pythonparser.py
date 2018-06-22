import os.path


def readFile():
    filePath = input("Enter file path including extension: ")
    while not (os.path.isfile(filePath) and filePath.lower().endswith("py")):
        filePath = input("File does not exist or is not a java file! Enter the correct file path: ")
            
    file=open(filePath, "r")
    java_file = file.readlines()
    file.close()
    return java_file

def parseCode():
    inIf = False
    inElseIf = False
    inElse = False
    lines = readFile()
    length = len(lines)
    for i in range(length):
        each_line = lines[i].lstrip()
        x = int((len(lines[i]) - len(each_line)) / 4)
##        print(x)
        each_line = each_line.strip()
        
        if str(each_line).strip().startswith("if"):
            if (inIf or inElseIf or inElse) and x == 0:
                print("],", end = " ")
            inIf = True
            inElse = False
            inElseIf = False
            print("[1:", end  = " ") 
                   
        elif str(each_line).strip().startswith("elif"):
            if (inIf or inElseIf or inElse) and x == 0:
                print("],", end = " ")
            inElseIf = True
            inIf = False
            inElse = False
            print("2:,")
        elif str(each_line).strip().startswith("else"):
            if (inIf or inElseIf or inElse) and x == 0:
                print("],", end = " ")
            inElse = True
            inIf = False
            inElseIf = False
            print("3:", end = " ")
        elif (each_line.startswith("if") or each_line.startswith("elif") or each_line.startswith("else")) and (inIf or inElse or inElseIf):
            
            if each_line.startswith("if"):
                if x == 1:
                    print("],", end = " ")
                print("[1:", end = " ")
           
            if str(each_line).strip().startswith("elif"):
                if x == 1:
                    print("],", end = " ")
                print("2:,", end = " ")
            if str(each_line).strip().startswith("else"):
                if x == 1:
                    print("],", end = " ")
                print("3:", end = " ")
                             
                        
                    
            
            
    
parseCode()
        
    
