from queue import PriorityQueue
from collections import Counter

class Tree:
    def __init__(self,sign,right,left):
        self.sign=sign
        self.right=right
        self.left=left




def szyfr():
    with open("kod_huffmana.txt", "r") as file:
        text = file.read()
    symbol_counts = Counter(text)
    unique_symbols = set(text)
    unique_symbol_list = list(unique_symbols)
    root=kod_huffmana(unique_symbol_list,symbol_counts)
    
    def prefix(z,ROAD):
        nonlocal file
        if z.right==None and z.left==None:
            file.write(z.sign+" "+"".join(ROAD)+"\n")
        else:
            if z.right!=None:
                ROAD.append("1")
                prefix(z.right,ROAD)
                ROAD.remove("1")
            if z.left!=None:
                ROAD.append("0")
                prefix(z.left,ROAD)
                ROAD.remove("0")

    with open("code.txt", "w") as file:
        prefix(root,[])

    
        


def kod_huffmana(unique_symbols,symbol_counts):
    n=len(symbol_counts)
    Q=PriorityQueue()
    counter=n
    for symbol in unique_symbols:
        frequency=symbol_counts[symbol]
        ascii_code=ord(symbol)
        sign=Tree(symbol,None,None)
        Q.put((frequency,ascii_code,sign))

    i=1
    while counter!=1:
        x=Q.get()
        y=Q.get()
        connected_sign=Tree("connected",x[2],y[2])
        sum=x[0]+y[0]
        Q.put((sum,counter,connected_sign))
        counter-=1

    z=Q.get()
    return z[2]





szyfr()
