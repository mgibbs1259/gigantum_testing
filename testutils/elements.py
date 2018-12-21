
class UiElement(object):
    def __init__(self, driver):
        self.driver = driver

class Auth0LoginElements(UiElement):
    @property
    def username_input(self):
        return self.driver.find_element_by_css_selector("input[name='username']")

    @property
    def password_input(self):
        return self.driver.find_element_by_css_selector("input[name='password']")


class CreateProjectElements(UiElement):
    pass
