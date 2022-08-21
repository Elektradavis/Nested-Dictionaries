x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney'],
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

def iterateDictionary(list):
    for entry in list:
        output = ''
        for key in entry.keys():
            output = output + key + ' - ' + entry[key] + ', '
        print(output[:-2])

def iterateDictionary2(key, list):
    for dict in list:
        print(dict[key])

music = [
         {'song':  'Butterfly Fields', 'artist' : 'Christian French', 'album' : 'Butterfly Fields'},
         {'song':  'Something to Someone', 'artist' : 'Dermot Kennedy', 'album' : 'Sonder'},
         {'song':  'Taste of You', 'artist' : 'Rezz', 'album' : 'Spiral'},
         {'song':  'Like a Girl', 'artist' : 'Lizzo', 'album' : 'Cuz I Love You'}
    ]
iterateDictionary(music)
iterateDictionary2('song', music)
iterateDictionary2('artist', music)
iterateDictionary2('album', music)

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(str(len(val)) + ' ' + key.upper())
        for item in val:
            print(item)
        print('')

dogs = {
   'names': ['Pikachu', 'Zoey', 'Arya', 'Spade'],
   'ages': ['15', '14', '3', '1']
}

printInfo(dogs)
