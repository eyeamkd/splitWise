#------------------------------SplitWise Menu -----------------------------------# 
def menu():  
    while(1):
        print(''' 
                1.Add Expenses 
                2.Show Expenses 
                3. Show Users 
                4. Remove Users 
                5. Show expenses for specific user   
                6. Show Payable Amount
                7. Exit the application''')   
        print('Enter your choice')
        choice = int(input())
        if(choice not in range(1,8)):
            print('Please enter the options from the menu above')  
        else: 
            break 
    return choice 
#------------------------------Check User----------------------------------------# 
def checkUser(user): 
    if user not in names:
        return False 
    else: 
        return True  
#------------------------------Calculate User Share -----------------------------# 
def calculateUserShare(user,amount): 
    share = amount/numberOfPeople 
    for mainKey in payableAmount.keys():
        if(mainKey!=user):  
            #if the person who paid owes anything to the 'mainkey' person
            if(payableAmount[user][mainKey]!=0): 
                if(payableAmount[user][mainKey]>share):
                    payableAmount[user][mainKey]-=share 
                else:
                    payableAmount[mainKey][user]=share-payableAmount[user][mainKey] 
                    payableAmount[user][mainKey]=0  
            #if the 'mainKey' person doesnot own anything to the user
            payableAmount[mainKey][user]=share

#------------------------------Add Expenses--------------------------------------# 
def addExpenses(): 
    amount=0
    print('Enter the user who had paid the expense amount') 
    user = input() 
    if(checkUser(user)==False): 
        print('''User Name not found, please enter the correct name, you might want to 
        look at the users list ''') 
        showUsers() 
    else: 
        amount = int(input("Enter the expense amount: ")) 
    expenses[user]+=amount  
    calculateUserShare(user,amount)

#------------------------------Show Expenses------------------------------------# 
def showExpenses(): 
    for user in names:
        print("The Amount of Money ",user,"Owes ") 
        print("--------------------------------------------------") 
        for ower in payableAmount[user].keys():
            print(user,"Owes ",ower," ",payableAmount[user][ower]) 
        print("---------------------------------------------------")

#-------------------------------Show Users Function------------------------------# 
def showUsers():  
    print("---------------------------") 
    print("S.no |\tName")  
    print("---------------------------")
    sno = 1
    for name in names: 
        print(sno,"   |",end="\t") 
        print(name) 
        sno+=1 
    print("----------------------------")
#------------------------------Remove Users Function----------------------------# 
def removeUsers():
    userToBeRemoved=''
    while(checkUser(userToBeRemoved)==False): 
        userToBeRemoved = input("Enter the name of the user whom you want to remove : ") 
        print('''Please enter correct name of the user to be removed you might want to refer to the user list below''')  
        showUsers()  
    names.remove(userToBeRemoved) 
    print("User Successfully Removed")
#--------------------------------Show Expenses for Specific user-----------------# 
def showExpensesForSpecificUser():
    print("Show expenses for specific user is still under development, you can try other options")
#-------------------------------Driver Code--------------------------------------#
numberOfPeople = int(input("enter the number of people present : "))
print('number of people are ',numberOfPeople) 
names=[]  
for i in range(0,numberOfPeople):
    print("Enter the name of #",(i+1),"Member")  
    name = input()
    names.append(name)  
expenses = dict.fromkeys(names,0) 
payableAmount = {mainKey:{} for mainKey in names} 
for user in names:
    for username in names:
        if(username!=user):
            payableAmount[user][username]=0 
choice = 0 
while(choice!=7): 
    #you can use a switch case here   
    choice = menu()
    if(choice==1): 
        addExpenses() 
    elif(choice==2): 
        showExpenses() 
    elif(choice==3):
        showUsers()
    elif(choice==4): 
        removeUsers()
    elif(choice==5): 
        showExpensesForSpecificUser() 
    elif(choice==6):
        calculateUserShare()


