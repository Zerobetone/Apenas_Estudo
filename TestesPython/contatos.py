class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)  # Implementar a obtenção do nome completo

    # Implementar outros métodos necessários

    def __str__(self):
        return "Nome: {}, Phone: {}, E-mail: {}".format(self.get_full_name(), self.phone_number, self.email )
    
    