name_tuple = ()
for i in range(5):
    name = input(("Input 5 names for the tuple (" + str(5-i) + " remaining): "))
    new_tuple = name_tuple + (name,)
    name_tuple = new_tuple
new_name = input("Input name: ")
if new_name in name_tuple:
    print(f"Welcome {new_name}, you are on the list.")
else:
    print(f"Sorry {new_name}, you are not on the list.")