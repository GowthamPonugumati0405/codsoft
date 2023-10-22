names=[]
phone_numbers=[]
num=3
for i in range(num):
    name= input("Name: ")
    phone_number= input("Phone number: ")
    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhonenumber\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i],phone_number[i]))

search_term=input("\nEnter Search term: ")
print("Search Result")
if search_term in names:
    index = names.index(search_term)
    phone_number=phone_number[index]
    print("Name {},Phone Number: {}".format(search_term,phone_number))

else:
    print("Name not found")
    