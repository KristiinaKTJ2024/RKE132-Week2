#Alusta programmi
#Küsi kasutajalt:"Mis on sinu perekonnanimi?"
#Salvesta vastus muutujasse surname.
#Küsi kasutajalt: "Vali sugu (m/n)"
#Salvesta vastus muutujasse gender.
#Kui sugu on võrdne tähega "m", siis väljasta ekraanile: "Tere, härra [surname]!"
#Muidu, kui gender on võrdne tähega "n", siis väljasta ekraanile "Tere, proua [surname]!"
#Muidu (kui sisestus on midagi muud), siis väljasta ekraanile "Tere, tulemast, [surname]!(sugu ei olegi tähtis)" """
 

surname = input("Mis on Sinu perekonnanimi?: ")
gender = input ("Vali sugu (m/n): ")

if gender =="m":
    print ("Tere, härra " + surname + "!")
elif gender =="n":
    print ("Tere, proua " + surname + "!")
else :
    print("Tere tulemast, " + surname + "! (sugu ei olegi tähtis)" )


