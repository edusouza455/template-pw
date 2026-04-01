import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login.login import LoginPage
from utils.config import Config
from utils.faker_data import FakerData

@allure.epic("Autenticação")
@allure.feature("Login")
class TestLogin:
    
    @allure.story("Login com credenciais válidas")
    @allure.title("Validar login com sucesso no OrangeHRM")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_login(self, page: Page):
        # Dado que o usuário acessa a página de login do OrangeHRM
        # E preenche o usuário e senha com dados válidos
        # Quando clica no botão Login
        # Então deve ser redirecionado para o dashboard
        
        login_page = LoginPage(page)
        login_page.navigate()
        
        # Utiliza as credenciais  
        login_page.login(Config.USER_NAME, Config.USER_PASSWORD)
        
        # Verifica se o login foi bem-sucedido
        login_page.validate_login_successful()

    @allure.story("Login com campos incompletos")
    @allure.title("Validar mensagem Required ao preencher apenas a senha")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_username(self, page: Page):
        # Dado que o usuário acessa a página de login 
        # E preenche apenas a senha
        # Quando clica no botão Login
        # Então deve exibir a mensagem Required sob o campo username
        
        login_page = LoginPage(page)
        login_page.navigate()
        
        # Deixa o usuário vazio e preenche a senha
        login_page.login("", Config.USER_PASSWORD)
        
        # Verifica se a mensagem de campo obrigatório aparece 1 vez
        login_page.validate_required_message(expected_count=1)

    @allure.story("Login com campos incompletos")
    @allure.title("Validar mensagem Required ao preencher apenas o usuário")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_password(self, page: Page):
        # Dado que o usuário acessa a página de login 
        # E preenche apenas o usuário
        # Quando clica no botão Login
        # Então deve exibir a mensagem Required sob o campo password
        
        login_page = LoginPage(page)
        login_page.navigate()
        
        # Preenche o usuário e deixa a senha vazia
        login_page.login(Config.USER_NAME, "")
        
        # Verifica se a mensagem de campo obrigatório aparece 1 vez
        login_page.validate_required_message(expected_count=1)

    @allure.story("Login com campos vazios")
    @allure.title("Validar mensagens Required ao tentar login sem preencher os campos")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_fields(self, page: Page):
        # Dado que o usuário acessa a página de login
        # Quando clica no botão Login com ambos os campos vazios
        # Então deve exibir a mensagem Required em ambos os campos
        
        login_page = LoginPage(page)
        login_page.navigate()
        
        login_page.login("", "")
        
        # Verifica se a mensagem de campo obrigatório aparece 2 vezes (usuário e senha)
        login_page.validate_required_message(expected_count=2)

    @allure.story("Login com credenciais inválidas")
    @allure.title("Validar mensagem Invalid credentials ao usar dados incorretos")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_credentials(self, page: Page):
        # Dado que o usuário acessa a página de login
        # Quando tenta logar com credenciais inválidas aleatórias
        # Então deve exibir a mensagem Invalid credentials
        
        login_page = LoginPage(page)
        login_page.navigate()
        
        # Utiliza o Faker para gerar dados que não existem no banco
        fake_username = FakerData.get_name()
        fake_password = FakerData.get_email() 
        
        login_page.login(fake_username, fake_password)
        
        # Verifica se a mensagem de erro é apresentada
        login_page.validate_invalid_credentials_message()
