#Exercise 39

things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])

print(things)

#dictionary
stuff = {'name':'Zed', 'age':39, 'height':6*12+2}

print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city'] = 'SF'
print(stuff['city'])


stuff[1] = 'Wow'
stuff[2] = 'Neato'

print(stuff)
del stuff[1]
del stuff[2]
print(stuff)

#create a mapping of a state to abbreviation
states = {
'Oregon':'OR',
'Florida':'FL',
'California':'CA',
'New York':'NY',
'Michigan':'MI'
}

cities = {
'CA':'San Fransisco',
'MI':'Detroit',
'FL':'Jacksonville'

}

#add some cities outside of dictionary
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out cities
print('-'*10)
print('NY State has:',cities['NY'])
print('OR State has', cities['OR'])

#print some states
print('-'*10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is", states['Florida'])

#do it by using hte state then cities dictionary
print('-'*10)
print("Michigan has", cities[states['Michigan']])
print('Florida has', cities[states['Florida']])

#print every state abbreviation
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in a state
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do them at the same time
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"{state} has the city {cities[abbrev]}")

print('-'*10)

#safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry no Texas")

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
