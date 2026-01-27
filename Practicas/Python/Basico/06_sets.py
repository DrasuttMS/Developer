## Sets ##

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Hello", "World"}
print(type(my_other_set))

print("Hello" in my_other_set)

my_other_set.add("MaxSalas")
print(my_other_set)

my_other_set.remove("World")
print(my_other_set)