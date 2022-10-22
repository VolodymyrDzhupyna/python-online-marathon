class Employee:

    def __init__(self, full_name, **kwargs):
        self.full_name = full_name
        self.name = full_name.split()[0]
        self.lastname = full_name.split()[1]
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
    

john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")


print(john.name)
print(john.lastname)
print(giancarlo.nationality)
