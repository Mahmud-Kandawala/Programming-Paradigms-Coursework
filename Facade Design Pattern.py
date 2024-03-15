class VenueBooking:
    """
    Creating a subsystem responsible for
    Handling venue bookings.
    """
    def book_venue(self, date: str) -> str:
        return f"Venue booked for {date}"
 
 
class CateringService:
    """
    Subsystem for handling catering orders.
    """
    def arrange_catering(self, menu: str) -> str:
        return f"Catering order for {menu}"
 

class PeopleCount:
    """
    Subsystem for counting amount of people.
    """
    def people_catering(self, people: int) -> int:
        return f"People Attending: {people}"


class NotificationSystem:
    """
    Subsystem for handling notifications
    """
    def send_invitation(self) -> str:
        return "Invitation Sent"
 
 
class EventManager:
    """
    Facade class which simplifies the interaction with the
    various management systems.
    """
    def __init__(self) -> None:
        self.venue_booking = VenueBooking()
        self.catering_service = CateringService()
        self.notification_system = NotificationSystem()
        self.people_system = PeopleCount()
 
    def organize_event(self, date: str, menu: str, people: int) -> str:
        """
        A method to organize the entire event by coordinating
        between different services.
        :param date:
        :param menu:
        :param people:
        :return:
        """
        results = []
        results.append(self.venue_booking.book_venue(date))
        results.append(self.catering_service.arrange_catering(menu))
        results.append(self.notification_system.send_invitation())
        results.append(self.people_system.people_catering(people))
        return "\n".join(results)
 
 
def client_code(event_manager: EventManager) -> None:
    """
    The client code that uses the facade to simplify the process
    of organizing our event.
    :param event_manager:
    :return:
    """
    print(event_manager.organize_event("2024-03-15", "Carivore Gluten-Free", 25))
  
 
 
if __name__ == "__main__":
    event_manager = EventManager()
    client_code(event_manager)