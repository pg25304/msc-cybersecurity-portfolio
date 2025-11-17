#DIP (Dependency Inversion Principal) flips the traditional dependency structure on its head: instead of high-level modules relying directly on
# low-level details, both should depend on shared abstractions. This makes systems more flexible and
# easier to extend or modify.
from abc import ABC, abstractmethod
# Step 1: Define an abstraction
class MessageService:
    @abstractmethod
    def send(self, message):
        pass
# Step 2: Create concrete implementations of the abstraction - Low-level modules
class EmailService(MessageService):
    def send(self, message):
        print(f"sending email: {message}")
class SMSService(MessageService):
    def send(self, message):
        print(f"sending SMS: {message}")
# Step 3: High-level module depends on the abstraction, not the concrete implementations
class NotificationSender:
    def __init__(self, service: MessageService):
        self.service = service
    def notify(self, message):
        self.service.send(message)

# Step 4: Client code/test
email_service = EmailService()
smsservice = SMSService()
email_notifier = NotificationSender(email_service)
sms_notifier = NotificationSender(smsservice)
email_notifier.notify("Hello Payman! via email")
sms_notifier.notify("Hello Payman! via SMS")
# Output:
# sending email: Hello Payman! via email
# sending SMS: Hello Payman! via SMS


