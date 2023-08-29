"""Chcemy wybrać wierzchołki o największej sumie, takie, że żadne dwa nie są połączone krawędzią"""


class Employee:
    def __init__(self,fun):
        self.emp=[]
        self.fun=fun
        self.max_party=-1
        self.without_person=-1

def max_party(person):
    if person.max_party>=0:
        return person.max_party
    x=person.fun
    for workers in person.emp:
        x+=g(workers)
    y=g(person)
    person.max_party=max(x,y)
    return person.max_party

def g(person):
    if person.without_person>=0:
        return person.without_person
    x=0
    for workers in person.emp:
        x+=max_party(workers)
    person.without_person=x
    return person.without_person
