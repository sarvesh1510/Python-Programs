import functools

# Simulated function to get current user permissions
def get_current_user_permissions():
    # For demonstration, let's assume the user has 'admin' permission
    return ['admin', 'edit', 'view']

def requires_permission(permission):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_permissions = get_current_user_permissions()
            if permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have permission to access this resource.")
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user_id):
    print(f"User {user_id} deleted")

# Attempt to delete a user
try:
    delete_user(123)
except PermissionError as e:
    print(e)

print("THIS PROGRAM IS WRITTEN BY SARVESH BHARDWAJ ERP :- 0221BCA062")
