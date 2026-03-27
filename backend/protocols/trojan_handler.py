# Trojan Protocol Handler

class TrojanHandler:
    def __init__(self):
        self.users = {}
        self.traffic_stats = {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = {'enabled': True}
            self.traffic_stats[username] = 0
            print(f"User {username} added.")
        else:
            print(f"User {username} already exists.")

    def enable_user(self, username):
        if username in self.users:
            self.users[username]['enabled'] = True
            print(f"User {username} enabled.")
        else:
            print(f"User {username} does not exist.")

    def disable_user(self, username):
        if username in self.users:
            self.users[username]['enabled'] = False
            print(f"User {username} disabled.")
        else:
            print(f"User {username} does not exist.")

    def log_traffic(self, username, bytes_transferred):
        if username in self.traffic_stats:
            self.traffic_stats[username] += bytes_transferred
            print(f"Traffic logged for user {username}: {bytes_transferred} bytes.")
        else:
            print(f"User {username} does not exist.")

    def get_traffic_stats(self, username):
        if username in self.traffic_stats:
            return self.traffic_stats[username]
        else:
            print(f"User {username} does not exist.")
            return None
