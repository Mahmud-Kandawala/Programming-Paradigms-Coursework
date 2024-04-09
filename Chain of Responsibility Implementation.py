from abc import ABC, abstractmethod

class AccessHandler(ABC):
    @abstractmethod
    def handle_request(self, user):
        pass

class BasicAccessHandler(AccessHandler):
    def __init__(self, successor = None):
        self.succsessor = successor

    def handle_request(self, user):
        if user.role == "basic":
            print("Basic access granted.")
        elif self.succsessor:
            self.succsessor.handle_request(user)
        else:
            print("Access denied.")

class PremiumAccessHandler(AccessHandler):
    def __init__(self, successor = None):
        self.successor = successor

    def handle_request(self, user):
        if user.role == "premium":
            print("Premium access granted.")
        elif self.successor:
            self.successor.handle_request(user)
        else:
            print("Access denied.")
        
class User:
    def __init__(self, role):
        self.role = role

class OrderingSystem:
    def __init__(self):
        # Build the chain of responsibility
        self.access_handler = BasicAccessHandler(PremiumAccessHandler())

    def process_order(self, user):
        print("Processing order...")
        self.access_handler.handle_request(user)

def main():
    order_system = OrderingSystem()

    user1 = User("basic")
    user2 = User("premium")

    order_system.process_order(user1)
    order_system.process_order(user2)


if __name__ == "__main__":
    main()   