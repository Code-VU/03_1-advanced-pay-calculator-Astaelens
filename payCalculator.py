def calculatePay():
    # This first line is provided for you
    try:
        hrs = float(input("Enter Hours: "))
    except:
        print("Error, please enter numeric imput")
    try:
        rate= float(input("Enter Rate: "))
    except:
        print("Error, please enter numeric imput")
    
    if hrs>40:
        pay= 40*rate+1.5*(hrs-40)*rate
    else:
        pay=rate*hrs
    print("Pay:",pay)
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
