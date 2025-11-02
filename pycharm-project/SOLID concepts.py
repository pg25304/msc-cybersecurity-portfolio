#This is a code to explor the concepts of SOLID
#1-Define Abstraction/interface;  any subclass must implement a send(message) method

class NotificationChannel:
    def send(self, message):
        pass
#Create two implementation
#- EmailChannel is a real implementation — it simulates sending an email.
class EmailChannel(NotificationChannel):
    def send(self, message):
        print("Email Sending:",message)


#- MockChannel is a fake one — useful for testing or demos.
class MockChannel(NotificationChannel):
    def send(self, message):
        print("Mock Sending:",message)


#Define the high levelModule - - NotificationService is the high-level logic.
#- It doesn’t care how the message is sent — it just calls self.channel.send(message).
class NotificationService:  #--init-- method which is a constructor that initializes an instance of the NotificationService class.
    #The method takes two parameters: self (a reference to the instance being created) and channel
    # (an instance of the NotificationChannel class, which is used to send notifications).
    def __init__(self, channel: NotificationChannel):
        """# channel parameter is assigned to the self.channel attribute, making the channel object an instance
         variable of the NotificationService class. This allows the channel to be used across different methods within the class"""
        self.channel = channel
        """defining a method called send, which is responsible for sending a notification. It takes two parameters:
        # self (the instance of the NotificationService class) and message 
        (the content of the notification to be sent)."""

    def send_notification(self, message):
            self.channel.send(message)
            """This line calls the send method of the channel object (which was assigned in the __init__ method).
            It passes the message parameter to the send method, effectively sending the notification through the
            specified NotificationChannel."""




""" - We create two versions of NotificationService, each with a different channel.
- The service code stays the same — only the injected channel changes.
- This is constructor injection and DIP in action.
"""
#email_service = NotificationService(EmailChannel())
#email_service.send_notification("Welcome to SOLID Notifications!")

#Using the real email channel
email = EmailChannel()
service1 = NotificationService(email)
service1.send_notification("Welcome Jack")

#using Mock channel
mock = MockChannel()
service2 = NotificationService(mock)
service2.send_notification("Testing notification system...")

