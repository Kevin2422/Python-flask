

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)


z[0]['y'] = 30
print(z)

def iterateDictionary(some_list):
    string = ''
    for x in range(0, len(some_list)):
        keys = list(some_list[x])
        for y in range(0, len(keys)):
            if len(string) == 0: 
                string = string + str( keys[y] + ' - ' + some_list[x][keys[y]] )
            elif len(string) > 0:
                string = string + ', ' + str( keys[y] + ' - ' + some_list[x][keys[y]] )
            if y == len(keys)-1:
                print(string)
                string = ''



students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
def iterateDictionary2( key_name, some_list):
    for x in range(0, len(some_list)):
        print(some_list[x][key_name])
iterateDictionary2('last_name', students)
iterateDictionary2('first_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfor(some_dict):
    diclist = list(some_dict)
    for x in range(0, len(diclist)):
        length = len(some_dict[diclist[x]])
        print(length)
        print(diclist[x])
        for y in range(0, len(some_dict[diclist[x]])):
            print(some_dict[diclist[x]][y])
        

printInfor(dojo)

