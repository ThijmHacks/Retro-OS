import pickle

def create_user_file():
    file = open("retroos/users/user_list.ul", "w")
    file.close()

def create_user(username, password):
    users[username] = password

    with open('retroos/users/user_list.ul', 'wb') as f:
        pickle.dump(users, f)