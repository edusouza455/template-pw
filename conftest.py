import pytest
import allure
from playwright.sync_api import Page

# Hook do Pytest executado após cada fase do teste
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # Verifica se o teste falhou durante a execução (fase "call")
    if report.when == "call" and report.failed:
        page: Page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )