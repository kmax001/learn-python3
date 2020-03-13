from sys import argv

script,filename=argv

print(f"We're going to erase {filename}.")
print("If you don't want that,hit CTRL-C (^C).")
print("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")
traget=open(filename,'w')

print("Truncating the file.Goodbye!")
traget.truncate()

print("Now I'm going to adk you for three lines.")

line1=input("line 1:")
line2=input("line 2:")
line3=input("line 3:")

print("I'm going to write these to the file.")

traget.write(line1)
traget.write("\n")
traget.write(line2)
traget.write("\n")
traget.write(line3)
traget.write("\n")

print("And finally,we close it.")
traget.close()