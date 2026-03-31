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

    def navigate(self):
       # Navega até a página de login
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

    def login(self, username: str, password: str):
        # Realiza o login com usuário e senha
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def validate_login_successful(self):
        # Valida se o login foi bem-sucedido verificando o cabeçalho do Dashboard
        expect(self.dashboard_heading).to_be_visible()
