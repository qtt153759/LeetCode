def cabin_split(X, number):
    return [x.split("/")[number] for x in X]


print(cabin_split(["B/0/P", "A/1/D", "C/2/T"], 1))
