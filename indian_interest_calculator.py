import datetime
import decimal

#Input
interest = 1.5
borrowed_amount = 200000
borrowedTime = datetime.date(2018, 6, 1)

today = datetime.date.today()
daily_interest = (borrowed_amount * interest / 100) / 30

var1 = today - borrowedTime
time_period = var1.days
#time_period >= 365
years = time_period // 365

#Cumilative amounts consecutively year wise
borrowed_amount_y1 = borrowed_amount + (borrowed_amount * interest / 100 * 12)
daily_interest_y1 = (borrowed_amount_y1 * interest / 100) / 30
borrowed_amount_y2 = borrowed_amount_y1 + (borrowed_amount_y1 * interest / 100 * 12)
daily_interest_y2 = (borrowed_amount_y2 * interest / 100) / 30
borrowed_amount_y3 = borrowed_amount_y2 + (borrowed_amount_y2 * interest / 100 * 12)
daily_interest_y3 = (borrowed_amount_y3 * interest / 100) / 30

def interestable_time():
    if years == 1:
        monthly_int_borrowed_amount_y1 = borrowed_amount * interest / 100 
        year1_add_days = time_period - (years * 365)
        int_year1_add_days = year1_add_days * (daily_interest_y1)
        total_amount_y1 = borrowed_amount_y1 + int_year1_add_days
        print("The amount Originally borrowed "+str(borrowed_amount)+ " after added 1 annual interests "+str(borrowed_amount_y1)+" the remaining days "+str(year1_add_days)+ \
            " and interest for the remaing days "+str(int_year1_add_days)+" Grand Total Payable is: "+str(total_amount_y1)+".")

    elif years == 2:
        monthly_int_borrowed_amount_y2 = borrowed_amount_y1 * interest / 100 
        year2_add_days = time_period - (years * 365)
        int_year2_add_days = year2_add_days * (daily_interest_y2)
        total_amount_y2 = borrowed_amount_y2 + int_year2_add_days
        print("The amount Originally borrowed "+str(borrowed_amount)+ " after added 2 annual interests "+str(borrowed_amount_y2)+" the remaining days "+str(year2_add_days)+ \
            " and interest for the remaing days "+str(int_year2_add_days)+" Grand Total Payable is: "+str(total_amount_y2)+".")
    elif years == 3:
        monthly_int_borrowed_amount_y3 = borrowed_amount_y2 * interest / 100 
        year3_add_days = time_period - (years * 365)
        int_year3_add_days = year3_add_days * (daily_interest_y2)
        total_amount_y3 = borrowed_amount_y3 + int_year3_add_days
        print("The amount Originally borrowed "+str(borrowed_amount)+ " after added 3 annual interests "+str(borrowed_amount_y3)+" the remaining days "+str(year3_add_days)+ \
            " and interest for the remaing days "+str(int_year3_add_days)+" Grand Total Payable is: "+str(total_amount_y3)+".")
    else:
         borrowed_year = borrowed_amount + (time_period * daily_interest)
         print("The amount payable for days: "+str(time_period)+ " days is Rs." +str(borrowed_year)+".")

interestable_time()


