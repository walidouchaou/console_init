import time
import  sys

heurs = time.strftime('%H', time.localtime())

if(int(heurs)>6 and int(heurs)<17):
    print("Bonjour")
else:
    print("bonsoir")

while True:
    word = input()
    if str(word) == "".join(reversed(word)) :
        print("bien dit ")
        print(word)
    else:
        print(word)

