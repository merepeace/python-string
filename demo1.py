#basic operation
str1='Hello'
str2='World'
str3=str1+str2
print("\n The co-catinated string is",str3)

#string Slicing
name="Buddha"
print(name[0:3])
print(name[2:])
#string count
print(name.count('d'))
#To check string
#name="Buddha"
print(name.startswith("Bud"))
print(name.endswith('h'))
#replace
print(name.replace('Buddha','Gautam'))
#print(name)

#split word
quot="Peace comes from within"
word=quot.split()
print(word)
#join word
print('-'.join(word))

#check if word is in string
print('Peace' in quot)
print('war' in quot)
