#Developed by Jordi Vicens Farrus
import string

#Create class and function
class User:
    name=""
    age=""
    kind=""

    def description(self):
        desc = "Hi! My name is %s and I am %i years old. And this is a %s for show you how I can program." % (self.name, self.age, self.kind)
        return desc

#Create an object
user1= User()
user1.name="Jordi Vicens Farrus"
user1.age=23
user1.kind="test"


#Write the file
fo = open("test_by_Jordi_Vicens.txt", "wb")
fo.write(user1.description())
fo.close()

#read the file
fo=open("test_by_Jordi_Vicens.txt", "r+")
stri = fo.read()
print stri
fo.close()
