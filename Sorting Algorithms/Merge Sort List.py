# Merge-Sort Algorithm on Cross-reference list

class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

        
def merge(p,q):                   # Merging two sorted lists.
    if p==None and q==None:
        return None
    if p==None:
        return q
    if q==None:
        return p
    
    if p.val>=q.val:
        new=q
        q=q.next
    else:
        new=p
        p=p.next
    new_head=new
    new.next=None

    while p !=None and q !=None:
        if p.val>=q.val:
            new.next=q
            q=q.next
        else:
            new.next=p
            p=p.next
        new=new.next
        new.next=None

    if q==None:
        new.next=p
    else:
        new.next=q
    return new_head
  
  
def separate(head):       # Separating the biggest sorted element from the start of the list.
    p=head
    if p==None:
        return None, None
    while p.next!=None:
        if p.val>p.next.val:
            q=p.next
            p.next=None
            return head, q
        p=p.next
    return head, None
    
    
def merge_sort(head):     # Merge sort algorithm.
    while True:
        new=Node(-1)
        tail=new
        counter=0
        while head!=None:
            a,head=separate(head)
            b,head=separate(head)
            tail.next=merge(a,b)
            while tail.next!=None:
                tail=tail.next
            counter+=1
        if counter==1:
            return new.next
        head=new.next
