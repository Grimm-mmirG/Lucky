# Open the file to read the file
with open ("mydefaults.ini") as file:
    data = file.read()

# Starting point for counting
number = 0
lower = 0
upper = 0

#Makes the file actually readable by the editor 
line = data.split("\n")
keys = dict()

# Itterates line by line 
for i in line:
    if "=" in i:
        fields = i.split("=")

# Start counting n = num l = letter
    for n in i:
        if n.isnumeric():
            number+=1
    for l in i:
        if l.isupper():
            upper+=1
        elif l.islower():
            lower+=1

#output
print (f" {number} total numbers in mydefaults.ini")
print (f" {lower} total lowercase letters in mydefaults.ini")
print (f" {upper} total uppercase letters in mydefaults.ini")
    