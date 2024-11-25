def check_access(func):
    def wrapper(employee):
        #Comprobar rol
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('Acceso denegado. Sin permisos de administrador')
    return wrapper

#Funcion que elimina empleados
@check_access
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

#delete_employee(admin)
delete_employee(employee)