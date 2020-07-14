class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def length(self):
        len=0
        temp=self.head
        while(temp is not None):
            len+=1
            temp=temp.next
        return len
    def append(self,data):
        node=Node(data)
        if(self.head is None):
            self.head=node
        else:
            p=self.head
            while True:
                if(p.next is None):
                    break
                p=p.next
            p.next=node
    def insertatbegi(self,data):
        node=Node(data)
        if(self.head is None):
            self.head=node
            return
        temp=self.head
        self.head=node
        self.head.next=temp
        del temp
    def insertatmid(self,data,posi):
        node=Node(data)
        if(posi<0 or self.length()<posi):
            print("Invalid position")
            return
        if(posi==0):
            self.insertatbegi(node)
            return
        temp=self.head
        for _ in range(posi-1):
            temp=temp.next
        p=temp.next
        temp.next=node
        temp.next.next=p
        del temp
        del p
    def pop(self):
        temp=self.head
        while(temp.next is not None):
            p=temp
            temp=temp.next
        p.next=None
        del p
    def deletehead(self):
        if(self.length()!=0):
            temp=self.head
            self.head=self.head.next
            temp.next=None
        else:
            print("list is empty. NO element to delete")
    def deleteat(self,posi):
        if(posi<0 or self.length()<posi):
            print("Invalid position")
            return
        if(posi==0):
            self.deletehead()
            return
        if(self.length()!=0):
            temp=self.head
            for _ in range(posi-1):
                temp=temp.next
            p=temp.next.next
            temp.next=p
    def reverse(self):
        curr=self.head
        prev=None
        while(curr!=None):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev

def printlist(head):
    if(head):
        print(head.data)
        printlist(head.next)

t=linkedlist()
while(True):
    print("Select option from below:")
    print("""1.append
2.insertatbegi
3.insertatmid
4.pop
5.deletehead
6.deleteatloc
7.reverse
8.length
9.printlist
10.Break""")
    s=int(input())
    if(s==1):
        t.append(input())
    elif(s==2):
        t.insertatbegi(input("Enter name"))
    elif(s==3):
        t.insertatmid(input("Enter name"),int(input("Enter location")))
    elif(s==4):
        t.pop()
    elif(s==5):
        t.deletehead()
    elif(s==6):
        t.deleteat(int(input("Enter location")))
    elif(s==7):
        t.reverse()
    elif(s==8):
        print(t.length())
    elif(s==9):
        printlist(t.head)
    elif(s==10):
        break