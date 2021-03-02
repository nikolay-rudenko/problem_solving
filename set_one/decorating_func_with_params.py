import functools


user = {'username': 'Jose', 'access_level': 'admin'}


def make_secure(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f"No permissions for {user['username']}."

    return secure_func


@make_secure
def get_admin_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'super_secure password'


print(get_admin_password('billing'))
