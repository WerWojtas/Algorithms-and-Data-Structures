"""Mamy spis przedmiotów z ich cenami i wagami. Mamy plecak o określonej pojemności. Jak włożyć do niego przedmioty, aby ich łączna cena była
jak największa?"""

def Knapsack(WAGES,PRICES,max_weight):
    quantity=len(WAGES)
    F=[[0 for _ in range(max_weight+1)] for _ in range(quantity)]

    for weight in range(WAGES[0],max_weight+1):
        F[0][weight]=PRICES[0]                  
    
    for weight in range(max_weight+1):        
        for item in range(1,quantity):
            F[item][weight]=F[item-1][weight]
            if weight>=WAGES[item]:
                F[item][weight]=max(F[item][weight],F[item-1][weight-WAGES[item]]+PRICES[item])

    return F[quantity-1][max_weight]

"""Ustawiamy funkcje wagi i przedmiotów. Argumentami funkcji będzie największa wartość aktualnego plecaka dla danej wagi
Dla każdej możliwej dostępnej wagi pierwszego przedmiotu (od wagi pierwszego przedmiotu do max) ustawiamy funkcję na cenę
przedmiotu, to oznacza, że przedmiot został wzięty. Dla wszystkich wag przechodzimy po dostępnych przedmiotach. Funkcja ustawia od razu wartość
dla aktualnej wagi na wartość wcześniejszego przedmiotu dla tej wagi (czyli gdy nie bierzemy rozpatrywanego przedmiotu). Następnie sprawdzamy czy
przedmiot się mieści. Jeśłi tak to bierzemy max z wartości już ustawionej - przypadek gdy pomijamy aktualny przedmiot, albo wartości funkcji
z przedmiotu przed nim i wagi pomniejszonej przez wagę aktualnego przedmiotu (ta waga zostanie wykorzystana właśnie na przedmiot) i jego
ceny. Na koniec zwracamy wartość funkcji z ostatniego przedmiotu z max wagi"""
