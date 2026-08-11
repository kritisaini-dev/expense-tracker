# Expense Tracker Project

expensesList = [] #lists of expenses in form of dictionary
print("Welcome to Expence Tracker : Kharcha kam kiya karo ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice= int(input("Please Entre Your Choise : "))

#ADD Expense
    if(choice ==1):
        date= input("Kis date per kharcha kiya tha?:")
        category= input("Kis type ka kharcha kiya? (Food, Travel, Makeup, Books):")
        description= input("Aur detail dedo:")
        amount= float(input("Enter the amount: "))

        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n DONE bro! Expenses added succesfully")

# 2. VIEW ALL EXPENSES
    elif(choice == 2):
        if( len(expensesList)==0 ):
            print("No Expenses Added. Jao pehle kharcha karo. ")
        else:
            print("==== Ye apka sara expense ====")  
            count= 1
            for eachKharcha in expensesList:
                print(f"Kharcha Number {count} -> {eachKharcha["date"]}, {eachKharcha["category"]}, {eachKharcha["description"]}, {eachKharcha["amount"]}")  
                count= count+1

# 3. VIEW Total spending
    elif(choice == 3):
        total= 0
        for eachKharcha in expensesList:
            total = total + eachKharcha["amount"]

        print("\n TOTAL KHARCHA= ", total)    

# 4. EXIT
    elif(choice == 4):
        print("Dhanyawad apne humara system use kiya")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")    
