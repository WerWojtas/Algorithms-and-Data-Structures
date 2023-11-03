"""(problem sumy podzbioru) Dana jest tablica n liczb naturalnych A. Proszę podać i zaimplementować algorytm, który sprawdza,
czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T"""
 
def sum(A,T):
    n=len(A)
    expected_sum=T
    F=[[0 for _ in range(expected_sum+1)]for _ in range(n)]

    for i in range(A[0],expected_sum+1):
        F[0][i]=A[0]

    for sum in range(expected_sum+1):
        for number in range(1,n):
            F[number][sum]=F[number-1][sum]
            if sum-A[number]>=0:
                F[number][sum]=max(F[number][sum],F[number-1][sum-A[number]]+A[number])

    for i in range(n):
        if F[i][expected_sum]==expected_sum:
            return True
        


    return False



T=[0,7,12,2,2,10,5]
print(sum(T,20))
