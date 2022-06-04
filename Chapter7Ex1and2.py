#1
employee = {'name1': 'Jake', 'salary1' : '100k', 'name2': 'Anand', 'salary2' : '120k'}
print("First employee name is {name1} with salary of {salary1} and second employee name {name2} with salary of {salary2}".format(**employee))

#2
user_input = ("LIST YOUR FRIENDS")
print("", user_input.lower())
friend=list()
while True:
  friends=input("")
  if friends == "STOP":
    break
  else:
    friend.append(friends)
print (": ")
for friends in friend:
  print (friends.upper())

