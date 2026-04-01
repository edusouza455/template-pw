import allure
from playwright.sync_api import Page, Locator, expect
from utils.config import Config

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = Config.BASE_URL
        
        # Locators
        self.username_input: Locator = page.get_by_role("textbox", name="Username")
        self.password_input: Locator = page.get_by_role("textbox", name="Password")
        self.login_button: Locator = page.get_by_role("button", name="Login")
        self.dashboard_heading: Locator = page.get_by_role("heading", name="Dashboard")
        self.required_message: Locator = page.get_by_text("Required")
        self.invalid_credentials_message: Locator = page.get_by_text("Invalid credentials")

    @allure.step("Navegar até a página de login")
    def navigate(self):
       # Navega até a página de login
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

    @allure.step("Realizar o login com usuário: {username}")
    def login(self, username: str, password: str):
        # Realiza o login com usuário e senha
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    @allure.step("Validar que o login foi bem-sucedido")
    def validate_login_successful(self):
        # Valida se o login foi bem-sucedido verificando o cabeçalho do Dashboard
        expect(self.dashboard_heading).to_be_visible()

    @allure.step("Validar mensagem de campo obrigatório")
    def validate_required_message(self, expected_count: int = 1):
        # Valida se a mensagem "Required" aparece a quantidade de vezes esperada
        expect(self.required_message).to_have_count(expected_count)

    @allure.step("Validar mensagem de credenciais inválidas")
    def validate_invalid_credentials_message(self):
        # Valida se a mensagem de "Invalid credentials" é exibida
        expect(self.invalid_credentials_message).to_be_visible()
