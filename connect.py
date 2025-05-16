from martypy import Marty

IP = input("Enter the IP address of your Marty: ")

my_marty = Marty("wifi", IP)
my_marty.dance()