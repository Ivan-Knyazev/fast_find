def find_user(required_user: str, users):
    # users objects to strings
    users_str = {}
    for i in range(len(users)):
        user = users[i]
        user_str = f'{user.name} {user.surname} {user.patronymic} {user.email}'.lower()
        users_str[i] = user_str

    # split required find string
    find = required_user.lower().split()

    keys = [i for i in users_str.keys()]
    keys_new = []
    for word in find:
        for i in keys:
            if word in users_str[i]:
                keys_new += [i]
        keys = keys_new
        keys_new = []

    # return result
    result = [users[i] for i in keys]
    return result
