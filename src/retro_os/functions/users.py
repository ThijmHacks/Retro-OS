import pickle
import os

def create_user_file():
    savedir = "retroos/users/"
    if not os.path.exists(savedir):
        os.makedirs(savedir)


    file = open("retroos/users/user_list.ul", "w")
    file.close()



def create_user(username, password):
    try:
        with open('retroos/users/user_list.ul', 'rb') as f:
            users = pickle.load(f)
    except (EOFError):
        users = {}


    users[username] = password

    with open('retroos/users/user_list.ul', 'wb') as f:
        pickle.dump(users, f)

def load_users():
    try:
        with open('retroos/users/user_list.ul', 'rb') as f:
            users = pickle.load(f)
            return users
    except EOFError:
        return {}
    except FileNotFoundError:
        return {}