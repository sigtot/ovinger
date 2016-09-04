print("Verdens minst brukervennlige kalkulator")
def add(x,y):
	return x+y
def subtract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def devide(x,y):
	return x/y

def main():
	operator = str(input("Velg operator, (+,-,*,/): "))
	if operator not in ['+','-','*','/']:
		print('Du skrev ikke inn en operator')
		main()
	print("Du valgte",operator)

	num1 = float(input("Skriv inn tall #1 :"))
	num2 = float(input("Skriv inn tall #2 :"))

	if(operator == '+'): print(add(num1,num2))
	if(operator == '-'): print(subtract(num1,num2))
	if(operator == '*'): print(multiply(num1,num2))
	if(operator == '/'): print(devide(num1,num2))
	main()
main()