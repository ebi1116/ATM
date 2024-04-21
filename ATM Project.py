class bank:
    def opening_account(s):
        s.name=input("Enter customer name:")
        s.accno=int(input("Enter Account number:"))
        s.bal=int(input("Opening balance:"))
    def deposit(s):
        s.accnum=int(input("Enter Account number:"))
        if (s.accno==s.accnum):
            print("Hai",s.name,"!")
            s.dep=int(input("Deposit amount:"))
            s.bal=s.bal+s.dep
            print("Avail balance is:",s.bal)
        else:
            print("Invalid number")
    def withdrawl(s):
        s.accnum=int(input("Enter Account number:"))
        if (s.accno==s.accnum):
            print("Hai",s.name,"!")
            s.wd=int(input("Withdrawl amount:"))
            s.bal=s.bal-s.wd
            print("Avail balance is:",s.bal)
        else:
            print("Invalid number")
    def bal_info(s):
        s.accnum=int(input("Enter Account number:"))
        if (s.accno==s.accnum):
            print("Hai",s.name,"!")
            print("Your Avail balance is:",s.bal)
        else:
            print("Invalid number")

st=bank()
print("\t\t\t UCO BANK")
print("\t\t\t --- ----")
print("\t 1) OPENING BAANCE")
print("\t 2) DEPOSIT")
print("\t 3) WITHDRAWAL")
print("\t 4) BALANCE INFORMATION")
print("\t 5) EXIT")
while(True):
    ch=int(input("Enter your option:"))
    if (ch==1):
        st.opening_account()
    elif (ch==2):
        st.deposit()
    elif (ch==3):
        st.withdrawl()
    elif (ch==4):
        st.bal_info()
    elif (ch==5):
        print("Thanks for using")
        print("Have a Nice Day")
        exit(0)
    else:
        print("Invalid")
        exit(0)
