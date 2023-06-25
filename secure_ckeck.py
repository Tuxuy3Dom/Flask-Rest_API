from user import User

users = [User(1, 'Ihor', 'ihor_pass'),
         User(2, 'Dawid', 'dawid_pass')]

username_table = {u.username: u for u in users}
user_id_table = {u.id: u for u in users}

def authenticate(username, password):
    user = user_id_table.get(username, None)
    if user and password == user.password:
        return user
    
def identity(payload):
    user_id = payload['identity']
    return user_id_table.get(user_id, None)