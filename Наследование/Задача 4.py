class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        print(f"Sending message '{message}' to {user.name}")

    def post(self, message):
        print(f"Posting message '{message}' on own wall")

    def info(self):
        return ""

    def describe(self):
        print(f"User: {self.name} {self.info()}")

class Person(User):
    def __init__(self, name, birthday):
        super().__init__(name)
        self.birthday = birthday

    def info(self):
        return f"Date of Birth: {self.birthday}"

    def subscribe(self, user):
        print(f"{self.name} subscribed to {user.name}")

class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f"Description: {self.description}"