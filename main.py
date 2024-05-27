#5. Scrieti o functie care citeste un string de la tastatura si afiseaza lungimea lui. 
#Tratati cazul in care textul nu este string

def citesteString():
    try:
        n=str(input('n='))
        lungime=len(n)
        print(lungime)
        return lungime
    except ValueError:
        print('Trebuie string')

citesteString()

#6. Fiind dat un dictionar {"a":1,"b":2,"c":3} scrieti o functie
#care primeste ca parametru cheia si returneaza valoarea
def dictionar():
    dict={
        "a":1,
        "b":2,
        "c":3
        }
    n=input("Alegeti a,b sau c=")
    key=dict[n]
    print(key)

dictionar()
