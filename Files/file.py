#File Objects


#But not used
f = open('test.txt','r') #2nd Parameter mode
print(f.name)
f.close()


#Recommended
with open('test.txt','r') as m:
    m_contents = m.read() #read(100) ex - read 100 characters
    #readlines() All Lines comes as list
    print(m_contents)

    for line in m:
        print(line , end='')



with open('test.txt','r') as n:
    size_to_read = 10
    n_contents = n.read(size_to_read)
    #tell() current position
    #seek() sets beginning of file
    while len(n_contents) > 0:
        print(n_contents,end='*')
        n_contents = n.read(size_to_read)

with open('test2.txt', 'a') as o:  #w- write ,  a-append , rb-Read Binary
    o.write('It will create one file')



 #copy from 1 file to another
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)