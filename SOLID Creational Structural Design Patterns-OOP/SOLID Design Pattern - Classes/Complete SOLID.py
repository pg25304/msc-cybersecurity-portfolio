class NotificationChannel:
    def send(self, message):
        pass


# Implementations
class EmailChannel(NotificationChannel):
    def send(self, message):
        print("This is sent by Email Channel:", message)


class SMSChannel(NotificationChannel):
    def send(self, message):
        print("Sent by SMS:", message)


class PushChannel(NotificationChannel):
    def send(self, message):
        print("Push channel sent:", message)


# Wrapper / High level module
class NotificationService:
    """Define and initiate constructor method which takes a channel argument of type NotificationChannel
    and assign it to self.channel"""

    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    def send_notification(self, message):
        # Call the send method of provided channel
        self.channel.send(message)


# Example usage:
email_channel = EmailChannel()
email_service = NotificationService(email_channel)
email_service.send_notification("Welcome to SOLID Notification")

SMS_channel = SMSChannel()
SMS_service = NotificationService(SMS_channel)
SMS_service.send_notification("Welcome to SMS notification")

Push_channel = PushChannel()
push_service = NotificationService(Push_channel)
push_service.send_notification("Welcome to push notification system")