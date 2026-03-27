import subprocess
class ZiVPNHandler:
    def __init__(self):
        self.users = {}
    def download_binary(self):
        url = "https://github.com/fauzanihanipah/ziv-udp/releases/download/udp-zivpn/udp-zivpn-linux-amd64"
        result = subprocess.run(["wget", url, "-O", "/usr/local/bin/udp-zivpn"], capture_output=True)
        return {"status": "success" if result.returncode == 0 else "error"}
    def create_user(self, username, port):
        self.users[username] = {"port": port, "enabled": True}
        return {"status": "success", "username": username, "port": port}
    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            return {"status": "success"}
        return {"status": "error"}
    def get_users(self):
        return self.users
