from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def notify(self):
        pass


class EmailNotificationService(NotificationService):

    def __init__(self, message):
        self.message = message

    def notify(self):
        return f"Email: {self.message}"


class SMSNotificationService(NotificationService):

    def __init__(self, message):
        self.message = message

    def notify(self):
        return f"SMS: {self.message}"


def run_notifications(services):
    for service in services:
        print(service.notify())


if __name__ == "__main__":
    message = input()

    services = [
        EmailNotificationService(message),
        SMSNotificationService(message),
    ]

    run_notifications(services)