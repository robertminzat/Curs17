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