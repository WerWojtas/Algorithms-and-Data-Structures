#Weronika Wojtas
"""Algorytm rekurencyjny - algorytm szuka możliwych przepięć w grafie dwudzielnym. Dla każdego pracownika odwiedzamy maszyny które umie
obsługiwać i nie zostały jeszcze odwiedzone, jeśli maszyna nie jest do nikogo przypisana automatycznie zwracamy 1 -> maszyna została
przypisana więc ilość pracujących pracowników zwiększyliśmy o jeden, jeśli natomiast jest przypisana wykonujemy te same kroki dla osoby
do której maszyna została przypisana w ten sposób sznurkiem rekurencji możemy dotrzeć do tego czy osobę "kolidującą" możemy przepisać
na inną maszynę, jeżeli nie funkcja zwraca 0 więc suma pracowników się nie zwiększa. Wykonujemy te kroki dla każdego pracownika aby
znaleźć najoptymalniejsze przypisanie."""



def binworker(M):
    n=len(M)
    MACHINE=[None for _ in range(n)]
    sum=0

    for i in range(n):
        VISITED=[False for _ in range(n)]
 
        def recurention(ppl):
            for j in range(len(M[ppl])):
                if VISITED[M[ppl][j]]==False:
                    VISITED[M[ppl][j]]=True
                    if MACHINE[M[ppl][j]]==None or recurention(MACHINE[M[ppl][j]])==1:
                        MACHINE[M[ppl][j]]=ppl
                        return 1
            return 0
        
        sum+=recurention(i)
 
    return sum
                    
