
movies = ["The Holy Grail",
          "The Life of Brian",
          "The Meaning of Life"]
print(movies[1])

cast = ['Clesse', 'Palin', 'Jones', 'Idle']
print(cast)

#BIF len
print(len(cast))

#Lists methon append(), pop(), extends,

#append()
cast.append('Gilliam')
print('Append Done, added ', cast[-1])
print(cast)

#pop()
print('Poping out',cast[-1])
print(cast, ' <--',cast.pop())
print(cast)

#extends()
new_casts = (['Gillam', 'Chapman'])
print('extending ' , new_casts)
cast.extend(new_casts)
print(cast)

#remove()
print("Removing",cast[-1])
cast.remove('Chapman')
print(cast)

#insert()
cast.insert(0, "Chapman")
print("New Cast Added at position 0 ", cast[0])
print(cast)
