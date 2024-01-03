# Loan-Calculator

Console application

Use -h argument to show information about application

usage: creditcalc.py [-h] [--payment PAYMENT] [--principal PRINCIPAL]
                     [--periods PERIODS] [--interest INTEREST] [--type TYPE]

optional arguments:
  -h, --help            show this help message and exit
  --payment PAYMENT
  --principal PRINCIPAL
  --periods PERIODS
  --interest INTEREST
  --type TYPE

  --type argument must be specified very time and contains value 'diff'(differentiated payments) or 'annuity'(annuity payment)

 Calculate months payment with 'diff' argument (you have to provide 'principal', 'periods' and 'interest')
 - python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
 
 Calculate the annuity payment with 'annuity' argument (you have to provide 'principal', 'periods' and 'interest')
 - python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
 
 Calculate the principal with 'annuity' argument (you have to provide 'payment', 'periods' and 'interest')
 - python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
 
 Calculate periad with 'annuity' argument (you have to provide 'principal', 'payment' and 'interest')
 - python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8

 You cannot calculate 'interest'
