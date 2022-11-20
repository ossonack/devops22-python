
my_list = []
color = "red"

my_list.append(color)
print(my_list[0])
my_list.extend(["blue", "green"])

if "red" in my_list:
    print("red is in the list")
if "purple" not in my_list:
    print("purple is not in the list")

my_colors = ["yellow", "brown"]
my_colors = my_colors + my_list
print(my_colors)

new_colors = ["red", "yellow"]
new_colors = new_colors * 3
print(new_colors[0:4])
print(new_colors.count("red"))
print(new_colors.index("yellow"))
print(len(new_colors))

number_list = [1,2,3,4,5,6,7]
print(min(number_list))
print(max(number_list))
