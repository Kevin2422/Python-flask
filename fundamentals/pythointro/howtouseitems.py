students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for x in some_list:
        print(x)
        # for key, values in some_list[x]:
        for key, values in x.items():
            print(key + " - " + values)
            # print(key + values)
    

iterateDictionary(students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfor(some_dict):
    
    for x in some_dict:
        
        print(x)
        print(len(some_dict[x]))
        for y in some_dict[x]:
            print(y)

printInfor(dojo)