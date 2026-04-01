import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login.login import LoginPage
from utils.config import Config

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
