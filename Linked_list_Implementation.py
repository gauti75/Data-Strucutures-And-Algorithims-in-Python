class Node:
        def __init__(self,data=None,next=None):
            self.data=data
            self.next=None

class linked_list():
    
    def __init__(self):
        self.head=Node()

    def insert(self,data):
        new_node=Node(data)
        current_element=self.head

        while current_element.next!=None:
            current_element=current_element.next
        current_element.next=new_node

    def display(self):
        elem=[]
        count=0
        current_element=self.head
        while current_element.next!=None:
            current_element=current_element.next
            elem.append(current_element.data)
            count+=1
        for i in range(0,len(elem)):
            if(elem[i]==elem[-1]):
                print(f"{elem[i]}")
            else:
                print(f"{elem[i]}",end="=>")

    def find_length(self):
        current_Node=self.head
        total=0
        count=0
        while current_Node.next!=None:
            current_Node=current_Node.next
            count+=1
        total+=count
        return total
        #print(f"The length of the linked list {total}")

    def value_at_Index(self,index):
        current_Node=self.head
        current_index=0

        if index<0 or index>=self.find_length():
            print("error")
        
        while True:
            if current_index==index:
                return current_Node.data
            current_index+=1
            current_Node=current_Node.next

    def remove_at_Index(self,index):
        current_node=self.head
        current_index=0

        if index<0 or index>=self.find_length():
            print("error")

        
        
            
        while current_node:
            if current_index==index-1:
                current_node.next=current_node.next.next
                
            current_node=current_node.next
            current_index+=1
            
        
  

    


    
example=linked_list()

example.insert(23)
example.insert(355)
example.insert(325)
example.insert(55)

example.display()
example.find_length()

print(example.value_at_Index(1))

example.remove_at_Index(2)

example.display()
