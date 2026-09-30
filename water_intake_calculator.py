#Alusta programmi.
#Määra eesmärgiks 2000 ml.
#Küsi kasutajalt: "Mitu klaasi vett oled täna joonud?"
#Salvesta vastus muutujasse cups.
#Arvuta joodud vee kogus , korrutades cups 250-ga.
#Arvuta, mitu protsenti päevasest eesmärgist on täidetud. 
#Väljasta täidetud protsent.
#Kui protsent on väiksem kui 50, siisväljasta ekraanile: "Joo rohkem vett, keha vajab seda!"
#Muidu, kui protsent on väiksem kui 100, siis väljasta ekraanile: "Tubli, jätka samas vaimus!"
#Muidu väljasta ekraanile: "Suurepärane, oled oma päevase eesmärgi täitnud!"
#Lõpeta programm.

goal = 2000
cups = int(input("Mitu klaasi vett oled täna joonud?: "))

water = cups * 250
percent = (water/goal) * 100

print(f"{percent}%")

if percent < 50 :
    print ("Joo rohkem vett, keha vajab seda!")
elif percent < 100:
    print ("Tubli, jätka samas vaimus!")
else :
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")
    

