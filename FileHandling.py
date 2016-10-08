import sys
file_name = "/Users/Raj/Desktop/raj.txt"
file_finish ="/Users/Raj/Desktop/raj1.txt"
try:
    file = open(file_name,"w")
except IOError:
    print("There was an error writing to", file_name)
    sys.exit()
print ("Enter '", file_finish,)
print "' When finished"
while file_text != file_finish:
    file_text = raw_input("Enter Text")
    if file_text == file_finish:
        file.close
        break
    file.write(file_text)
    file.write("\n")
file.close()
file_name=input("Enter filename")
if len(file_name)==0:
    print ("Next time please enter something")
    sys.exit()
try:
    file=open(file_name,"r")
except IOError:
    print("There was an error reading file")
    sys.exit()
file_text = file.read()
file.close()
print(file_text)
