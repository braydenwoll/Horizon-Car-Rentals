# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 16:09:21 2022

@author: brayd
"""
import math


BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
 
PROMPT = '''\nWould you like to continue (A/B)? '''

customer_code = "\nCustomer code (BD, D, W): "
days = "\nNumber of days: "
odometer_start = "Odometer reading at the start: "
odometer_end = "Odometer reading at the end:   "
invalid = "\n\t*** Invalid customer code. Try again. ***"
customer_summary = "\nCustomer summary:"
"\tclassification code:"
"\trental period (days):"
"\todometer reading at start:"
"\todometer reading at end:  "
"\tnumber of miles driven: "
"\tamount due: $"
Loyalty = "Thank you for your loyalty."

print(BANNER)
#input
total_cost = 0
prompt = input(PROMPT)
# while loop
while prompt == 'A':
    Customer_Code = input(customer_code)
    while not(Customer_Code == 'BD' or Customer_Code == 'D' or Customer_Code == 'W'):
        print(invalid)
        Customer_Code = input(customer_code)
    if Customer_Code == 'BD' or Customer_Code == 'D' or Customer_Code == 'W':
        DAYS = int(input(days))
        Odometer_Start = int(input(odometer_start))
        Odometer_End = int(input(odometer_end))
    
        #odometer
        
        if Odometer_End >= Odometer_Start:
            miles = Odometer_End - Odometer_Start
            miles = miles / 10.0
        else: 
            miles = 1000000 - Odometer_Start + Odometer_End
            miles = miles / 10.0
            
            #amount due
        if Customer_Code == 'BD':
                BD = 40.00 * DAYS
                m = 0.25 * miles
                total_cost = BD + m
                
        elif Customer_Code == 'D':
                D = 60.00 * DAYS
                avg_miles = miles / DAYS
                if avg_miles <= 100:
                    m = 0
                else:
                    m = 0.25 * (miles - (100 * DAYS))
                total_cost = m + D
                
        elif Customer_Code == 'W':
                W = math.ceil(DAYS/7)
                avg_miles = miles / W
                W_cost = W * 190.00
                mil = 0
                if avg_miles <= 900:
                    m = 0
                elif avg_miles > 900 and avg_miles <= 1500:
                    m = W * 100.00
                else:
                    m = W * 200.00
                    mil = miles - (1500 * W)
                    mil = mil * 0.25
                total_cost = W_cost + m + mil
                
        #print statements
        
        print(customer_summary)
        print("\tclassification code:",Customer_Code)
        print("\trental period (days):",DAYS)
        print("\todometer reading at start:",Odometer_Start)
        print("\todometer reading at end:  ",Odometer_End)
        print("\tnumber of miles driven: ",miles)
        print("\tamount due: $",total_cost)
    
    prompt = input(PROMPT)
if prompt == 'B':
    print(Loyalty)
