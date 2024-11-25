#Decorador que comprueba rol
def check_access(required_rol):
    def decorator(func):
        def wrapper(employee):
            #Comprobar si el rol del empleado coincide con el rol requerido
            if employee.get('role') == required_rol:
                return func(employee)
            else:
                print(f'Acceso denegado.')
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Registrando accion para el empleado {employee['name']}')
        return func(employee)
    return wrapper

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado.')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

#delete_employee(admin)
delete_employee(employee)