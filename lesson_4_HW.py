class Node:
        
        def __init__(self, data):
             self.data = data
             self.next = None


class Kitchen:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_order(self, data):
        new_order = Node(data)
        if self.head == None:
            self.head = new_order
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order

    def cook_order(self):
        if self.head == None:
            return "No Orders"
        else:
            cooked = self.head
            self.head = cooked.next
            return cooked.data
    
    def view_orders(self):
        orders = self.head
        while orders:
            print(orders.data)
            orders = orders.next


order = Kitchen()

order.add_order("Hamburger")
order.add_order("Hotdog")
order.add_order("Sandwich")

order.view_orders() 

print("-" * 25)

print("Cooking Order:", order.cook_order())

print("-" * 25)

order.view_orders()