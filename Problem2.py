#Problem 1 - Paying Debt off in a Year

balance = input()
annualInterestRate = input()
monthlyPaymentRate = input()
interest = 0
for i in range(12):
    balance = balance+interest
    minamount=balance*monthlyPaymentRate/100
    balance=balance-minamount
    interest=balance*annualInterestRate/1200
balance = balance + interest
print("Remaining balance: " + "%.2f" %balance)


###############################################################################################################


#Problem 2 - Paying Debt Off in a Year

def calculate(month, balance, min_amount, annualInterestRate):
    while month <12:
        balance = balance - min_amount
        balance = balance + (annualInterestRate * balance)/1200
        month = month +1
    return balance
min_amount = 10
balance = input()
annualInterestRate = input()
while True:
      if calculate(0, balance, min_amount, annualInterestRate) <= 0:
          break
      min_amount = min_amount+10
print('Lowest Payment: ' + str(min_amount))


####################################################################################################################


#Problem 3 - Using Bisection Search to Make the Program Faster

balance = input()
annualInterestRate = input()
monthlyinterestrate = annualInterestRate/12.0
def calculate(month, balance, min_amount, monthlyinterestrate):
    while month <12:
        balance = balance - min_amount
        balance = balance + (monthlyinterestrate * balance)
        month = month+1
    return balance
lower = balance/12.0
high = balance * (1 + monthlyinterestrate)**12 / 12.0
while True:
       min_amount=(lower+high)/2
       if abs(calculate(0, balance, min_amount, monthlyinterestrate))<0.001:
          break
       elif calculate(0, balance, min_amount,monthlyinterestrate) > 0:
          lower=min_amount
       elif calculate(0, balance, min_amount, monthlyinterestrate) < 0:
          high=min_amount
print('Lowest Payment: ' + '%.2f' %min_amount)
