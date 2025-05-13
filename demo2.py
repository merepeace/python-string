#string formating operator
name='Umesh'
age=30
print("My name is %s and i am %d years old." %(name,age))

text="Python"
print(text[2:4])
print(text[1:5])

print("Py" in "Python")
print("Java" not in "Python")

print("abc" < "bcd")  # True
#for loop for string
message='Hello'
for ch in message:
#for ch in message.upper(): #is used for uppercase letter output
    print(ch)

#The string module
import string
print( string.ascii_lowercase +'\t' + string.ascii_uppercase )
print("\t".join(string.ascii_lowercase))
print("\t".join(string.ascii_uppercase))