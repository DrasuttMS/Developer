##listas##

my_list = list()
my_other_list = []

print(len(my_list))
print(type(my_other_list))

my_list = [35, 24, 62, 52, 12]
print(my_list)
print(len(my_list))

my_other_list = [35, 24.5, "Hello", "World", True]
print(my_other_list)

print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[1:3])

my_other_list.append("New Element")
print(my_other_list)

my_other_list.insert(1, "Inserted Element")
print(my_other_list)

my_other_list.remove("Hello")
print(my_other_list)

print(my_other_list.pop())
print(my_other_list)

del my_other_list[0]
print(my_other_list)

my_other_list.clear()
print(my_other_list)

my_new_list = my_list.copy()
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)