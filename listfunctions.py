
lucky = [47, 36, 33, 11, 8, 3]
friends = ["Jim", "John", "John", "Bob", "Fred", "Mary", "John", "Shaun"]
friends.extend(lucky)
print(friends)


friends.append("Append")
print(friends)
friends.insert(0, "Insert")
print(friends)
friends.remove("John")
print(friends)
print(friends.pop())
print(friends.index("Insert"))


print(friends)
print(friends.count("John"))

lucky.sort()
print(lucky)
lucky.reverse()
print(lucky)

luckagain = lucky.copy()
print(luckagain)