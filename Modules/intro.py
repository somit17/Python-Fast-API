import my_module as mm

#from my_module import find_index,test // * -> Import all but * not used

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses,'Math')
print(index)