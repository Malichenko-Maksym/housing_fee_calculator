import datetime, csv,os


def money_input(message):
    bad_input_money=True
    while bad_input_money:
        print(message)
        amount=input()
        try:
            amount=int(amount)
            if(amount>0):
                bad_input_money=False
            else:
                print("you have to pay something")
        except:
            print("must be a number")
    return amount

def year_input(message):
    bad_input_year=True
    while bad_input_year:
        print(message)
        year=input()
        try:
            year=int(year)
            # datetime.date.today().year - to know current year
            if(year<=datetime.date.today().year and year>=2003 ):
                bad_input_year=False
            else:
                print("We have no information about future...  And we aren't  historians...")
        except:
            print("must be a number")
    return year

def mount_input(message):
    bad_input_month=True
    while bad_input_month:
        print(message)
        mount=input()
        try:
            mount=int(mount)
            if(1<=mount and mount<=12):
                bad_input_month=False
            else:
                print("There are only 12 of them...")
        except:
            print("must be a number")
    return mount

def data_format(year,month):
    if(month//10==0):
        return str(year)+"M0"+str(month)
    else:
        return str(year)+"M"+str(month)



#money input
old_payment=money_input("How much you have been paying before?")
new_payment=money_input("How much you pay now?")



incorrect_input=True
while incorrect_input:
    #year input
    year_old_payment=year_input("When housing payment was set(only year)")
    month_old_payment=mount_input("When housing payment was set(only month)")
    year_new_payment=year_input("When housing payment was changed(only year)")
    mount_new_payment=mount_input("When housing payment was changed(only month)")
    
    if year_new_payment==datetime.date.today().year and mount_new_payment>=datetime.date.today().month-1:
        print("We don't have data yet")
        input("Press Enter to continue")
    else:
        if year_old_payment<year_new_payment or (year_old_payment==year_new_payment and month_old_payment<=mount_new_payment ):
            incorrect_input=False
        else:
            print("Payment must be setted before changed")
            input("Press Enter to continue")
            

# we will count in months
old_payment_months= year_old_payment*12+month_old_payment
new_payment_months= year_new_payment*12+mount_new_payment


if(new_payment_months-old_payment_months>=12):
    
    old_payment_date=data_format(year_old_payment,month_old_payment)
    new_payment_date=data_format(year_new_payment,mount_new_payment)
    allowed_to_pay=old_payment
    
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
    except:
        print("Error")
    
    try:
        with open("dane.csv", 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            
            allowed_to_pay=old_payment
            for row in csvreader:
                if(row[0]>old_payment_date and row[0]<=new_payment_date):
                    allowed_to_pay=allowed_to_pay+allowed_to_pay/100*float(row[1])
                    #print(allowed_to_pay)
        if(allowed_to_pay<new_payment):
            print("illegal, max ammount: "+str(round(allowed_to_pay, 3)))
        else:
            print("legal")
    except:
        print("Error")     
    
        
else:
    print("there are less then 12 months since last change")
    

input("Press Enter to exit")


    
