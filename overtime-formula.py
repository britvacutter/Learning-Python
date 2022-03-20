hrs = input("Enter Hours: ")
pay = input("Enter Rate: ")
p = float(pay)
h = float(hrs)

if h >= 40 :
    ot = h - 40
    otr = (ot) * (p * 1.5)
    r = (p * 40) + otr
    print(r)
elif h < 40 :
    r = h * p
    print(r)
    r = h * p
    print(r)