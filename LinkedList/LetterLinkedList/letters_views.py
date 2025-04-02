from django.shortcuts import render
from django.http import HttpResponse

from LinkedList.LetterLinkedList.LetterNode import LetterNode
from LinkedList.LetterLinkedList.LetterLinkedList import LetterLinkedList
# Create your views here.

def letters(request):
    # Creating Letter nodes
    a = LetterNode("A")
    b = LetterNode("B")        
    c = LetterNode("C")    
    d = LetterNode("D")
    e = LetterNode("E")
    f = LetterNode("F")
    g = LetterNode("G")
    h = LetterNode("H")
    i = LetterNode("I")
    j = LetterNode("J")
    k = LetterNode("K")
    l = LetterNode("L")
    m = LetterNode("M")
    n = LetterNode("N")
    o = LetterNode("O")
    p = LetterNode("P")
    q = LetterNode("Q")
    r = LetterNode("R")
    s = LetterNode("S")
    t = LetterNode("T")
    u = LetterNode("U")
    v = LetterNode("V")
    w = LetterNode("W")
    x = LetterNode("X")
    y = LetterNode("Y")
    z = LetterNode("Z")

    a.setNextPointer(b)
    b.setNextPointer(c)
    c.setNextPointer(d)
    d.setNextPointer(e)
    e.setNextPointer(f)
    f.setNextPointer(g)
    g.setNextPointer(h)
    h.setNextPointer(i)
    i.setNextPointer(j)
    j.setNextPointer(k)
    k.setNextPointer(l)
    l.setNextPointer(m)
    m.setNextPointer(n)
    n.setNextPointer(o)
    o.setNextPointer(p)
    p.setNextPointer(q)
    q.setNextPointer(r)
    r.setNextPointer(s)
    s.setNextPointer(t)
    t.setNextPointer(u)
    u.setNextPointer(v)
    v.setNextPointer(w)
    w.setNextPointer(x)
    x.setNextPointer(y)
    y.setNextPointer(z)

    # Creating Linked List
    linkedList = LetterLinkedList(a)
    print(linkedList.printLinkedList())

    return HttpResponse(linkedList.printLinkedList())