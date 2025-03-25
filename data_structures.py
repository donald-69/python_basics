#data structures
# collection
#List,dictionary,set
scores = [78,43,22,35,20,18,55,41,32,40,50,43,73,12,21,93,34,54,45,54,64,45,84,32]

#access a specific score
print(scores[0])
print(scores[1])

#add a score
scores.append(90)
print(scores)

#remove a score
scores.remove(43)
print(scores)

print(len(scores))

print(scores.count(45))

scores.sort() #ascending
print(scores)

scores.sort(reverse=True) #descending
print(scores)

#slice a list
top_5 = scores[-5:] #cutting the list
print(top_5)

#Dictionary
person = {"name" : "Halima","age":19,"weight":58,"county":"Nairobi"}
print(person["name"])
print(person["age"])


#set
days = {"mon","tue","wed","thu","fri","sat","sun","mon"}
print(days)

for s in scores: #for each score in scores
    if s < 50:
        pass
    print(s)

for d in days: #for each day in days
    print(d)
























