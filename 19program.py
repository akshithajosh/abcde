class queue:
  def _init_(self):
    self.items = []
  def enqueue(self,item):
     self.items.append(item)
  def dequeue(self):
    if self.isEmpty():
       print("queue is Empty cannot delete")
    else:
      item=self.items.pop(0)
      print("deleted item is:",item)
  def display(self):
    if self.isEmpty():
       print("queue is Empty")
    else:
      print(self.items)
  def length(self):
    return len(self.items)
  def isEmpty(self):
    return len(self.items)==0
q=queue()
while (True):
 print("1:enqueue 2:dequeue 3:display 4:length 5:exit")
 choice=int(input("enter your choice:"))
 if choice==1:
    item=input("enter the element:")
    q.enqueue(item)
 elif choice==2:
    q.dequeue()
 elif choice==3:
    q.display()
 elif choice==4:
    n=q.length()
    print("lenght of the queue is",n)
 elif choice==5:
    break