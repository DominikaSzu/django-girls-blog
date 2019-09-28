#to jest instrukcja warunkowa

volume = 111
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
elif 100 <= volume < 120:
	print('Very loud')
else:
    print("My ears are hurting! :(")

def sayName(imie):
	print('Hej ' + imie)

sayName('Domninika')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']

for imie in dziewczyny:
	sayName(imie)
	print('next')


for a in range(1, 10):
	print(a)