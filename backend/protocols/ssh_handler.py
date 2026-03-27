class SSHUserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        if username in self.users:
            raise ValueError('User already exists.')
        self.users[username] = password

    def delete_user(self, username):
        if username not in self.users:
            raise ValueError('User does not exist.')
        del self.users[username]

    def change_password(self, username, new_password):
        if username not in self.users:
            raise ValueError('User does not exist.')
        self.users[username] = new_password

    def get_users(self):
        return list(self.users.keys())
