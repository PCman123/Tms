


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}   
print (Dict['Tiffany'])


#copy in dic
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
studentX=Boys.copy()
studentY=Girls.copy()
print (studentX)
print (studentY)


#@Updating Dictionary

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Dict.update({"Sarah":9})
print (Dict)

#Delete Keys from the dictionary

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
del Dict["Charlie"]
print (Dict)


#Dictionary items() Method
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))

#Dictionary len() Method

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Length : %d" % len (Dict))



#Merging Dictionaries

my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict2 = {"firstName" : "Nick", "lastName": "Price"}
my_dict1.update(my_dict2)

print(my_dict1)

#Dictionary Membership Test
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
print("email" in my_dict)
print("location" in my_dict)
print("test" in my_dict)

                                                                                    #Python Dictionary Append


my_dict = {"Name":[],"Address":[],"Age":[]};

my_dict["Name"].append("Pc")
my_dict["Address"].append("Ahemdabad")
my_dict["Age"].append(19)	
print(my_dict)

#Accessing elements of a dictionary

my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
print("username :", my_dict['username'])
print("email : ", my_dict["email"])
print("location : ", my_dict["location"])

#Deleting element(s) in a dictionary
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
del my_dict['username']  # it will remove "username": "XYZ" from my_dict
print(my_dict)

#second method
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict.pop("username")
print(my_dict)

#Updating existing element(s) in a dictionary
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict["username"] = "ABC"
print(my_dict)

