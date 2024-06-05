#fubmitted by Sandesh Rai
users = {
    "123-456-789":{"pin":4321,"balance":10000,"withdraw_limit":9000},
    "321-654-987":{"pin":1234,"balance":5000,"withdraw_limit":4000}
}

card_number = input("Enter your card number : ")
if card_number in users:
    pin= int(input("Enter your pin number: "))
    if pin == users[card_number]["pin"]:
        print("Sucessfully login")
        while True:
            print("\n1) check balance \n2)Withdraw balance \n3) Exit")
            choice = int(input("Enter : "))
            if choice == 1:
                print("You're current balance is ", users[card_number]["balance"])
            elif choice == 2:
                withdraw_amout = int(input("Enter withdraw amout: "))
                if withdraw_amout <= users[card_number]["balance"]:
                    if withdraw_amout <= users[card_number]["withdraw_limit"]:
                        users[card_number]["balance"] -= withdraw_amout
                        print("Thankyou for withdrawing money, VISIT AGAIN!!")
                        break;
                    else:
                        print("Amoout greater than withdraw limti, Please try Again")
                else:
                    print("ERROR : INSUFFICENT AMOUNT")
            elif choice == 3:
                print("THANK YOU , VISIT AGAIN ")
                break;
            else:
                print("Invalic choid , please try agian !!")
    else:
        print("INVALID PIN")

else:
    print("INVALID CARD NUMBER")        

