def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    rate= input("Enter Rate: ")
    
    hrs=float(hrs)
    rate=float(rate)

    if hrs>40:
        pay= 40*rate+1.5*(hrs-40)*rate
    else:
        pay=rate*hrs
    print("Pay: ",pay)
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
