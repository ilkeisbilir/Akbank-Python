import csv
import datetime 
from tabulate import tabulate

#Üst sınıf pizza 
#get_description ve get_cost methodları olacak
#Alt sınıf pizza
#Pizza türleri tanımlanacak: Klasik, margharita, türk, dominos
#Üst sınıf decorator Soslar olacak
#Pizza class özelliklerini kullanarak 

pizza_list = {
    "classicpizza":"Klasik Pizza ", 
    "classicpizza_cost": 10,
    "classicpizza_disc": "Italyan lahmacunu",
    "margaritapizza": "Margarita Pizza",
    "margaritapizza_cost": 13,
    "margaritapizza_disc":"Italya'nin Napoli şehrinde, halkin yoksullugundan ortaya cikmistir",
    "turkpizza": "Turk Pizza",
    "turkpizza_cost": 12,
    "turkpizza_disc":"Pide ama pizza hamurunda",
    "sadepizza":"Sade Pizza",
    "sadepizza_cost": 11,
    "sadepizza_disc": "Sadece hamur ve sos",
}

topping_list= {
    "zeytin":"Zeytin",
    "zeytin_cost": 3,
    "mantar":"Mantarlar",
    "mantar_cost": 4,
    "kecipeyniri":"Keçi Peyniri",
    "kecipeyniri_cost": 7,
    "et": "Et", 
    "et_cost": 10,
    "sogan":"Soğan",
    "sogan_cost":3,
    "misir": "Misir",
    "misir_cost": 5
}

class Pizza():
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class classicpizza(Pizza):
    def __init__(self):
        super().__init__(pizza_list["classicpizza"], pizza_list["classicpizza_cost"])

class margaritapizza(Pizza):
    def __init__(self):
        super().__init__(pizza_list["margaritapizza"], pizza_list["margaritapizza_cost"])

class turkpizza(Pizza):
    def __init__(self):
        super().__init__(pizza_list["turkpizza"], pizza_list["turkpizza_cost"])

class sadepizza(Pizza):
    def __init__(self):
        super().__init__(pizza_list["sadepizza"], pizza_list["sadepizza_cost"])

#Decorator
class decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
            return self.component.get_cost() + self.cost

    def get_description(self):
            return self.component.get_description() + " " + self.description

#Soslar
class zeytin(decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = topping_list["zeytin"]
        self.cost = topping_list["zeytin_cost"]

class mantar(decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = topping_list["mantar"]
        self.cost = topping_list["mantar_cost"]

class kecipeyniri(decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = topping_list["kecipeyniri"]
        self.cost = topping_list["kecipeyniri_cost"]

class et(decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = topping_list["et"]
        self.cost = topping_list["et_cost"]

class sogan(decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = topping_list["sogan"]
        self.cost = topping_list["sogan_cost"]

class misir(decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = topping_list["misir"]
        self.cost = topping_list["misir_cost"]


    
def get_order():

    with open("menu.txt", "r") as f:
        for line in f:
            print(line, end="")
    
    pizza_kod = int(input("Lutfen istediğiniz pizza kodunu giriniz: "))
    
    if pizza_kod == 1:
        pizza = classicpizza()
    elif pizza_kod == 2:
        pizza = margaritapizza()
    elif pizza_kod == 3:
        pizza = turkpizza()
    elif pizza_kod == 4:
        pizza = sadepizza()
    else:
        print("Geçersiz pizza secimi yaptiniz")
    sos_kod = int(input("Lutfen istediginiz malzemeyi seciniz:" ))
    if sos_kod == 11:
        sos = zeytin(pizza)
    elif  sos_kod == 12:
        sos = mantar(pizza)
    elif  sos_kod == 13:
        sos = kecipeyniri(pizza)
    elif  sos_kod == 14:
        sos = et(pizza)
    elif  sos_kod == 15:
        sos = sogan(pizza)
    elif  sos_kod == 16:
        sos = misir(pizza)
    else:
        print("Geçersiz malzeme secimi yaptiniz")
    total_cost = sos.get_cost()
    print("Toplam Fiyat: ", total_cost , "TL")  

def main():
    get_order()

if __name__ == "__main__":
    main()