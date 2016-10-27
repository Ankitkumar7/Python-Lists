
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

"""
Let's take a bit of time to try to work out which strategy to use adding data to our listin this case
Adding more data to list

"""

#Given the following list-creation code
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

"""
Code requred to insert numeric year
Given data: ["The Holy Grail", 1975, "The Life of Brian", 1979,"The Meaning of Life, 1983"]

"""
print("Inserting 1975 at position 1")
movies.insert(1,1975)
print(movies[1]," inserted")
print("Inserting 1979 at position 3")
movies.insert(3,1979)
print(movies[3], " inserted")
print(movies)
print("Inserting 1983 at postion last")
movies.append(1983)
print(movies[-1], " inserted")
print(movies)
print("Insertion Process Finished")


#inserting item all in one go
movies = ["The Holy Grail", 1975,
          "The Life of Brian", 1979,
          "The Meaning of Life, 1983"]
print(movies)
