class Notification:
    def send(self, message):
        print(f"General Notification: {message}")


class EmailNotification(Notification):
    # Override send()
    def send(self, message):
        print(f"Email Notification: {message}")


message = input().strip()

# Create both objects and call send()
obj1 = Notification()
obj1.send(message)

obj2 = EmailNotification()
obj2.send(message)