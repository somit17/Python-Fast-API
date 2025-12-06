message = 'Hello World'
print(message)


#Lower case
print(message.lower())

#upper case
print(message.upper())

#Count returns times it appears
print(message.count('l'))

#Find Index of that char if not found returns -1
print(message.find('i'))
print(message.find('W'))


#Replace
new_message = message.replace('World','Universe')
# or assign same var message = message.replace('World','Universe') --Same result
print(new_message)

###Concatination
greeting = 'Hello'
name = 'Somit'

new_concat = greeting+','+name+'. Welcome !'
print(new_concat)


#formatted string
new_concat_format = '{}, {}. Welcome !'.format(greeting,name)
print(new_concat_format)


#New format f method --Most effective
print('New Formatted Method')
new_formatted_f_method = f'{greeting},{name.upper()}'
print(new_formatted_f_method)


#All attributes and methods available to use this variable
print(dir(name))



#Info about need to pass datatype
print(help(str.lower))



