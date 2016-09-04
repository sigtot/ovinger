# -*- coding: utf8 -*-
def main():
	print("Et program for å beregne nettopris på bil")
	name = input("Navnet på bilen: ")
	price = int(input("Bruttopris på bilen [kr]: "))
	weight = int(input("Vekt på bilen: "))
	hp = int(input("Antall hestekrafter på bilen: "))
	co2 = int(input("Antall gram Co2 utslipp på bilen: "))
	vol = int(input("Motorvolum på bilen [liter]: "))
	string = "Utsalgspris på %s vil bli %f kr" %(name,tax(price,weight,hp,co2,vol))
	print(string)

def tax(price,weight,hp,co2,vol):
	weight = price * weight * 0.00034
	hp = price * hp * 0.00015
	co2 = price * co2 * 0.004
	vol = price * vol * 0.00055
	return price + weight + hp + co2 + vol

def calc(name,price,weight,hp,co2,vol):
	# Alternative to asking the user for each value
	string = "Utsalgspris på %s vil bli %f kr" %(name,tax(price,weight,hp,co2,vol))
	print(string)

# Uncomment to let the user input values
#main()

calc('Ford Mondeo 1.8', 120000, 1680, 125, 125, 1800)
calc('Ford Mondeo 1.0', 130000, 1000, 125, 114, 1000)
calc('BMV M5 3.0', 260000, 1980, 350, 150, 3000)
calc('BMV M5 1.5', 270000, 1980, 350, 125, 1300)