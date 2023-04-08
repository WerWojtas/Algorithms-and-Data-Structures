#How to search for the largest palindrome in s word.


def ceasar( s ):     
    n=len(s)
    max_lenght=1
    if n%2!=0:
        x=y=z=n//2
    else:
        x=n//2
        y=x-1
        z=n-x-1
    for i in range(z):
        lenght=1
        for j in range(1,n-(x+i)):
            if s[(x+i)+j]==s[(x+i)-j] or s[(y-i)+j]==s[(y-i)-j]: 
                lenght+=2
            else:
                break
        if lenght>max_lenght:
            max_lenght=lenght
    return max_lenght
