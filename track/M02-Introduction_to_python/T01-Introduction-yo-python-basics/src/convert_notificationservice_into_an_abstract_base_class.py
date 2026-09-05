from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def notify(self):
        pass


class EmailNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def send_email(self):
        return f"Email: {self.message}"

    def notify(self):
        return self.send_email()


class SMSNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def send_sms(self):
        return f"SMS: {self.message}"

    # Implement notify()
    def notify(self):
        return self.send_sms()


message = input()

# Create both objects and call notify()
obj1 = EmailNotificationService(message)
obj2 = SMSNotificationService(message)

print(obj1.notify())
print(obj2.notify())