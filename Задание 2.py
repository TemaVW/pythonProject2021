time=int(input("Vvedite kolichestvo secund"))
#min=60sec
#hour=60min=3600sec
sec=time%60
min=(time//60)%60
hour=time//3600
chasu=f"{hour}:{min}:{sec}"
print(chasu)