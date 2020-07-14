class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doublelinkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        node=Node(data)
        if(self.head is None):
            self.head=node
            return
        p=self.head
        while(p.next):
            p=p.next
        p.next=node
        node.prev=p
    def prepend(self,data):
        node=Node(data)
        if(self.head is None):
            self.head=node
            return
        else:
            p=self.head
            node.next=p
            p.prev=node
            self.head=node
    def insertatposi(self,data,posi):
        node=Node(data)
        if(posi<0 or self.length()<posi):
            print("Invalid position")
            return
        if(posi==0):
            self.prepend(data)
            return
        temp=self.head
        for _ in range(posi-1):
            temp=temp.next
        p=temp.next
        temp.next=node
        node.prev=temp
        node.next=p
        node.next.prev=node
    def pop(self):
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.prev.next=None
    def delhead(self):
        if(self.length!=0):
            temp=self.head
            self.head=temp.next
            self.head.prev=None
        else:
            print("list is empty")
    def length(self):
        temp=self.head
        len=0
        while(temp is not None):
            len+=1
            temp=temp.next
        return len
    def delatloc(self,posi):
        if(posi<0 or self.length()<posi):
            print("Invalid position")
            return
        if(posi==0):
            self.delhead()
            return
        if(self.length()!=0):
            temp=self.head
            for _ in range(posi-1):
                temp=temp.next
            p=temp.next.next
            temp.next=p
            p.prev=temp
    def printrev(self):
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        while(temp):
            print(temp.data)
            temp=temp.prev

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    
t=Doublelinkedlist() 
while(True):
    print("Select option from below:")
    print("""1.append
2.prepend1
3.insertatmid
4.pop
5.deletehead
6.deleteatloc
7.printreverse
8.length
9.printlist
10.Break""")
    s=int(input())
    if(s==1):
        t.append(input())
    elif(s==2):
        t.prepend(input("Enter value: "))
    elif(s==3):
        t.insertatposi(input("Enter value: "),int(input("Enter location: ")))
    elif(s==4):
        t.pop()
    elif(s==5):
        t.delhead()
    elif(s==6):
        t.delatloc(int(input("Enter location: ")))
    elif(s==7):
        t.printrev()
    elif(s==8):
        print(t.length())
    elif(s==9):
        t.printlist()
    elif(s==10):
        break

