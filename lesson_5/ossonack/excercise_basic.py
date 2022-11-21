firstname = "john"
lastname = "smith"
tele = "00468123456789"

print(firstname, lastname, tele)

fullname = firstname + " " + lastname
print(len(fullname))
print(fullname + "\n" + tele)

print(firstname, lastname + "\n" + tele)
print(f"{firstname} {lastname}\n{tele}")
print("{0} {1}\n{2}".format(firstname, lastname, tele))
print("%s %s\n%s" % (firstname, lastname, tele))