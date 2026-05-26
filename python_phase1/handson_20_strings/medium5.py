string1 = input().split("=")[1].strip('”"')

w1, w2, w3 = string1.split()

print("Print String in default order: {} {} {}".format(w1, w2, w3))

print("Print String in Positional order: {1} {0} {2}".format(w1, w2, w3))

print("Print String in order of Keywords: {c} {b} {a}".format(a=w1, b=w2, c=w3))