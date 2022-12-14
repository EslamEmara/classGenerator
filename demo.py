import tkinter
methods = []
attributes = []

className = input("Enter class name: ")
numberOfMethods = 0
numberOfAttributes = 0
while(True):

    method = input("Enter " + str(numberOfMethods+1) + " Method ")
    if (method.upper() == "QUIT" or method.upper() == "Q"):
        break;
    methods.append(method)
    numberOfMethods+=1

while(True):
    attribute = input("Enter " + str(numberOfAttributes+1) + " attribute ")
    if (attribute.upper() == "QUIT" or attribute.upper() == "Q"):
        break;
    attributes.append(attribute)
    numberOfAttributes+=1

open(className+".h", 'w').close()
header_file = open(className+".h", "a")

header_file.write("#ifndef " + className.upper() + "_H")
header_file.write("\n#define " + className.upper() + "_H")
header_file.write("\n\nclass " + className.upper() + "{\n")
header_file.write("private: \n")
for i in range(numberOfAttributes):
    header_file.write("\t" + attributes[i] + ";\n")

header_file.write("public: \n")
for i in range(numberOfMethods):
    header_file.write("\t" + methods[i] + ";\n")

header_file.write("};\n\n\n\n\n#endif")

open(className+".cpp", 'w').close()
c_file = open(className+".cpp","a")

c_file.write("#include \""+className+".h\"")
