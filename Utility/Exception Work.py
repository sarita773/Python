#user_input1=input("enter first number")
#user_input2=input("enter second number")

#c=int(user_input1)+ int(user_input2)
#print(c)

from configparser import ConfigParser
#create object of Configparser calss
config=ConfigParser()

#read data from config file
#config.read("C:/Users/User/PycharmProjects/TestAutomation/Utility/Config.cfg")
#print(config.get("section1","username"))
config.read("../InputFile/Config.cfg")
print(config.get("section1","username"))