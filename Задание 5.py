a=int(input("Vvedite vurychky"))
b=int(input("Vvedite izdershki"))
if a>b:
    rv=(a/b)
    print("Firma rabotaet v prubil")
    s=int(input("Vvedite kolichestvo sotrudnikov"))
    ps=rv/s
    print("Pribil firmu na 1go sotrudnika",ps)
else:
    print("Firma rabotaet v ubitok")
    #
