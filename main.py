class Users:
    IDs = []
    USERNAMES = []
    Logs = []

    def __init__(self, username: str) -> None:
        self.username = username
        self.id = len(Users.IDs) + 1

    def create_user(self) -> None:
        if self.username not in Users.USERNAMES:
            Users.USERNAMES.append(self.username)
            Users.IDs.append(self.id)
            Users.Logs.append(f'User successfully created: {self.username} with ID: {self.id}')

    def delete_user(self) -> None:
        if self.username in Users.USERNAMES:
            index = Users.USERNAMES.index(self.username)
            Users.USERNAMES.pop(index)
            Users.IDs.pop(index)
            self.id = 0
            self.username = 'None'
            Users.Logs.append(f'User successfully deleted: {self.username}')

    def edit_user(self, new_username: str, new_id: int) -> None:
        if self.username in Users.USERNAMES:
            index = Users.USERNAMES.index(self.username)
            Users.USERNAMES[index] = new_username
            Users.IDs[index] = new_id
            self.username = new_username
            self.id = new_id
            Users.Logs.append(f'User successfully edited: {self.username} with ID: {self.id}')