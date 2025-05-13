#Creating string
name='Buddha'
message='Happy Buddha Purnima'

#Multiline string
long_text='''This is 
            a multi line string '''

#string concatinatio
greeting='Hello'+name
print(greeting)

#string Repetation
repeate ='om'
print(repeate*3)
print((repeate+'\t')*3)
print('\t'.join([repeate]*3))
print('\t'.join(repeate*3))

rr='umesh'*3
print(rr)

#accessing characters
first_letter=name[0]
print(name[0])
print(first_letter)

#string Method
print(name.upper())
print(message.lower())

#string formating
festival='Buddha purnima'
print(f"Happy  {festival},dear {name}.")

