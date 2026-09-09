class EmailNotification:

    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Email: {self.message}"


class SMSNotification:

    def __init__(self, message):
        self.message = message

    def send(self):
        return f"SMS: {self.message}"


class PushNotification:

    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Push: {self.message}"


def send_notifications(notifications):
    # Process every object using send()
    for i in notifications:
        print(i.send())


if __name__ == "__main__":
    message = input()

    # Create objects, store them in a list, and call send_notifications()
    obj1 = EmailNotification(message)
    obj2 = SMSNotification(message)
    obj3 = PushNotification(message)

    notifications = [obj1, obj2, obj3]

    send_notifications(notifications)