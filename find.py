def find_user(required_user: str, users):
    # users objects to strings
    users_str = []
    for user in users:
        user_str = f'{user.name} {user.surname} {user.patronymic} {user.email}'.lower()
        users_str += [user_str]

    # split required find string
    find = required_user.lower().split()

    indexes = [i for i in range(len(users_str))]
    indexes_new = []
    for word in find:
        for i in indexes:
            if word in users_str[i]:
                indexes_new += [i]
        indexes = indexes_new
        indexes_new = []

    # return result
    result = [users_str[i] for i in indexes]
    return result
