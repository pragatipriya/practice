def Ci(p,t,r):
    amount=p*pow((1+r/100),t)
    compound=amount-p
    return compound

print(Ci(1200,2,5.4))