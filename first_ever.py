#yo greetings ko lagi ho
print("\n\nwelcome to our caffey!!!!!!!!!!!\n")

print("MY NAME IS JARVIS AND I AM HERE TO HELP YOU :)\n")
#aaba malaii name chaiyo
name = (input("Can i ask your name please\n"))
#makhaan baji
print("Welcome " + name + " to our caffey may you have a great day ahead!!!!!:)\n")
print("Here is our menu please help your self\n")
#la menu hero
menu =  "We provide\t black_coffe\t expresso\t lattey\t cappucino\n"
input  (menu)
quantity = (input("how many coffies would you like to have " + name))

#if else chalauna laii variables
card = "card"
cash = "cash"

#aalikati maths bill ko total laii
rate = 8
bill = rate * int(quantity)

#order place vayo sang sangaiii card ki cash nii sodiyo
order = input( (name + " great choice" + ":) \n would you pay from " + str( card ) +" or " + str( cash ) + "\n" ))
 
#aaba check grxa card ki cash
if order == card:
    print("You can scan your card in our counter:\n")

elif order == cash:
    print("soo sweet of you to pay cash:)\n")
else:
    print(input("Please select the valid option!!!!!!!!!!!:(\n"))

#sakiyo last ma aali kati makhan baji
print("thankyou for the order your bill is\n $" + str(bill)+ "\n")
print("Give us 5 minutes of time to get your order ready")

# #aati vayo cancel pani rakhna pryo re
# print("Do you want to cancel your order?" + name)


#bonus nii rakhdim
ans= (input("would you like to rate us?"))
yes ="yes"
no="no"
if ans==yes:
    stars=int((input ("soo sweet of you how many stars you would give to us?")))
   
    if stars==5:
        print("Here is your 5% " + "dicount on your sweet review ")
        bill = int(bill)-5/100
        print(str(bill))

    elif stars==4:
        print("Here is your 4% " + "dicount on your sweet review ")
        bill = int(bill)-4/100
        print(str(bill))
    
    if stars==3:
        print("Here is your 3% " + "dicount on your sweet review ")
        bill = int(bill)-3/100
        print(str(bill))

    elif stars==3:
        print("Here is your 3% " + "dicount on your sweet review ")
        bill = int(bill)-3/100
        print(str(bill))
    
    if stars==2:
        print("Here is your 2% " + "dicount on your sweet review ")
        bill = int(bill)-2/100
        print(str(bill))

    elif stars==1:
        print("Here is your 1% " + "dicount on your sweet review ")
        bill = int(bill)-1/100
        print(str(bill))
    elif stars>=5:
        print("Invalid choice sorry no dicount:(\n please try next time:)")
else :
    print("Sad that you din't enjoy our service\n\n")
    print("Please visit us again:)")










