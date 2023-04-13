import random
from PIL import Image


sygnaly = ("Ciagly okresowy", "Ciagly nieokresowy", "Dyskretny okresowy", "Dyskretny nieokresowy")

CO = Image.open(r"C:\Users\Marcin\Desktop\Python\VSC\testownik\CO.JPG") 
CNO = Image.open(r"C:\Users\Marcin\Desktop\Python\VSC\testownik\CNO.JPG") 
DNO = Image.open(r"C:\Users\Marcin\Desktop\Python\VSC\testownik\DNO.JPG") 
DO = Image.open(r"C:\Users\Marcin\Desktop\Python\VSC\testownik\DO.JPG") 

new_var = 100
proba = 10
pytanie = random.choice(sygnaly)


#while proba  < new_var:
print(pytanie)

if pytanie == "Ciagly okresowy":
    widmo = input("Jakie widmo?: ")
    if widmo == "nieokresowe dyskretne":
#       im = Image.open(CO, mode="r") 
        print("Gratulacje")
        CO.show()
    else:
        print("Niestety nie")
else:
    pass

if pytanie == "Ciagly nieokresowy":
    widmo = input("Jakie widmo?: ")
    if widmo == "nieokresowe ciagle":
        #im = Image.open(CNO, mode="r") 
        print("Gratulacje")
        CNO.show()
    else:
        print("Niestety nie")
else:
    pass

if pytanie == "Dyskretny Okresowy":
    widmo = input("Jakie widmo?: ")
    if widmo == "okresowe dyskretne":
        print("Gratulacje")
            #im = Image.open(DO, mode="r") 
        DO.show()
    else:
        print("Niestety nie")
else:
    pass
if pytanie == "Dyskretny nieokresowy":
    widmo = input("Jakie widmo?: ")
    if widmo == "okresowe ciagle":
        print("Gratulacje")
            #im = Image.open(DNO, mode="r") 
        DNO.show()
    else:
        print("Niestety nie")
else:
    pass

proba+=1