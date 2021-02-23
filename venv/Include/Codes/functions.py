#generate coupon




#ouput on a slack chanel the usages of coupons

############### emails
#                   send email for creation
#                   send email for use (you have x left)

import email1

def creationEmail(client_email, coupon_code, expirecy_date, init_balance):
    return email1.opening(client_email, coupon_code, expirecy_date, init_balance)
def updateEmail(client_email, coupon_code, expirecy_date, current_balance):
    return email1.update(client_email, coupon_code, expirecy_date, current_balance)



############# validation

#validate if still active
#function validates if the coupon can be used for purchase

#validate location (Later)

def isActive(coupon_code):
    # look in database
    active = True
    return active

def canPurchase(coupon_code, new_transaction):
    # look in database
    curent_balance = 1
    return curent_balance >= new_transaction

############### fund update

#remove funcds
#    v1
#        inputs (curent balance, new transaction)
#        outpurs (new current balance, nb of transactions, avg transaction value)
#    v2
#        migrate v1 to coupon datastruct




