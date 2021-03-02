import functools

user = {'username': 'Jose', 'access_level': 'guest'}


def make_secure(func):
    @functools.wraps(func)
    def secure_func():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f"No permissions for {user['username']}."

    return secure_func


@make_secure
def get_admin_password():
    return '1234'


print(get_admin_password())
