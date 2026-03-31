from faker import Faker

# Inicializa o Faker com a localização para o Brasil (pt_BR)
fake = Faker('pt_BR')

class FakerData:
    
    @staticmethod
    def get_name() -> str:
        #Gera um nome completo aleatório
        return fake.name()

    @staticmethod
    def get_email() -> str:
        #Gera um endereço de e-mail aleatório
        return fake.email()

    @staticmethod
    def get_phone_number() -> str:
        #Gera um número de telefone aleatório
        return fake.phone_number()

    @staticmethod
    def get_cpf() -> str:
        #Gera um número de CPF válido aleatório
        return fake.cpf()

    @staticmethod
    def get_random_text(max_nb_chars: int = 200) -> str:
        #Gera um texto aleatório
        return fake.text(max_nb_chars=max_nb_chars)