def arithmetix (a, b, c):
    if c == "+":
        result = a + b
        print result
    elif c == "-":
        result = a - b
        print result
    elif c == "/":
        result = a/b
        print result
    elif c == "*":
        result = a*b
        print result
    else:
        print "insupported opperation"
result = 0

stop = True
while stop:
    a = input("Enter first number ")
    b = input("Enter second number ")
    c = raw_input("Enter opperation ")
    arithmetix (a, b, c)
    stop = raw_input("Enter False to stop ")
    if stop == "False":
        break
    elif stop == " ":
        continue
    else:
        continue