class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,data):
        make_node=node(data)
        if not self.head:
            self.head=make_node
            self.tail=make_node
        else:
            self.tail.next=make_node
            self.tail=make_node

    def show(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

    def delete(self,item):
        temp=self.head
        previous_node=None
        while temp.data!=item:
            previous_node=temp
            temp=temp.next
        next_node=temp.next
        if previous_node==None:
            self.head=next_node
        else:
            previous_node.next=next_node

if __name__ == "__main__":
    llist=linkedlist()
    for i in range(2):
        n=input()
        llist.insert(n)
    llist.show()
    llist.delete(str(1))
    llist.show()