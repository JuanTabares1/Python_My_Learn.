def print_exceptions_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exceptions_hierarchy(subclass, indent + 4)

print_exceptions_hierarchy(Exception)