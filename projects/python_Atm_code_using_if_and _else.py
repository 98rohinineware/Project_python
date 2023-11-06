print("welcome to the ATM")
correct_code="1234"
amount=10000

print("Enter pin number")
p=input()
 
if p==correct_code:
	print("Menu")
	print("1. change pin")
	print("2. Deposit cash")
	print("3. Withdraw Cash")
	print("4. check balance")

	choice=int(input())

if choice==1:
	print("Enter new pin")
	new_pin=input()
	correct_code=new_pin
	print("Successfully pin Changed")


elif choice==2:
	print("Enter pin number")
	p=int(input())
	if correct_code==str(p):
		print("How much money you want to deposit")
		a=int(input())
		amount+=a
		print("Total balance is:",amount)
		

elif choice==3:
	print("Enter pin number")
	p=int(input())
	if correct_code==str(p):
		print("Enter how much money do you want to withdraw:")
		w=int(input())
		if w<=amount:
			amount-=w
			print("Withdraw cash successfully")
		else:
			print("Not sufficient balance")
	else:
		print("Check the pin") 



elif choice==4:
	print("Enter pin number")
	p=int(input())
	if correct_code==str(p):
	    print("Total balance is:",amount)
	else:
		print("Check the pin") 

else:
	print("Exit")		
