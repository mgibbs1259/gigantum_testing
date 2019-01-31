

class UiElement(object):
    def __init__(self, driver):
        self.driver = driver


class Auth0LoginElements(UiElement):
    @property
    def login_green_button(self):
        return self.driver.find_element_by_css_selector(".Login__button")

    @property
    def username_input(self):
        return self.driver.find_element_by_css_selector(".auth0-lock-input[name = username]")

    @property
    def password_input(self):
        return self.driver.find_element_by_css_selector(".auth0-lock-input[name = password]")

    @property
    def login_grey_button(self):
        return self.driver.find_element_by_css_selector(".auth0-lock-submit")


class GuideElements(UiElement):
    @property
    def got_it_button(self):
        return self.driver.find_element_by_css_selector(".button--green")

    @property
    def guide_button(self):
        return self.driver.find_element_by_css_selector(".Helper-guide-slider")

    @property
    def helper_button(self):
        return self.driver.find_element_by_css_selector(".Helper__button--side-view")


class AddProjectElements(UiElement):
    @property
    def create_new_button(self):
        return self.driver.find_element_by_css_selector(".btn--import")

    @property
    def project_title_input(self):
        return self.driver.find_element_by_css_selector(".CreateLabbook input")

    @property
    def project_description_input(self):
        return self.driver.find_element_by_css_selector(".CreateLabbook__description-input")

    @property
    def project_continue_button(self):
        return self.driver.find_element_by_xpath("//button[contains(text(), 'Continue')]")


class AddProjectBaseElements(UiElement):
    @property
    def arrow_button(self):
        return self.driver.find_element_by_css_selector(".slick-arrow slick-next")

    @property
    def create_project_button(self):
        return self.driver.find_element_by_css_selector(".ButtonLoader ")

    @property
    def projects_page_button(self):
        return self.driver.find_element_by_css_selector(".SideBar__icon")

    @property
    def py2_tab_button(self):
        return self.driver.find_element_by_xpath("//li[contains(text(), 'python2')]")

    @property
    def py2_minimal_base_button(self):
        return self.driver.find_element_by_xpath("//h6[contains(text(), 'Python2 Minimal')]")

    @property
    def py3_tab_button(self):
        return self.driver.find_element_by_xpath("//li[contains(text(), 'python3')]")

    @property
    def py3_minimal_base_button(self):
        return self.driver.find_element_by_xpath("//h6[contains(text(), 'Python3 Minimal')]")

    @property
    def py3_data_science_base_button(self):
        return self.driver.find_element_by_xpath("//h6[contains(text(), 'Python3 Data Science Quick-Start')]")

    @property
    def r_tab_button(self):
        return self.driver.find_element_by_xpath("//li[contains(text(), 'R')]")

    @property
    def r_tidyverse_base_button(self):
        return self.driver.find_element_by_xpath(
            "//h6[contains(text(), 'R Tidyverse (+ Python3) in Jupyter Quickstart')]")


class EnvironmentElements(UiElement):
    @property
    def environment_tab_button(self):
        return self.driver.find_element_by_css_selector("#environment")

    @property
    def add_packages_button(self):
        return self.driver.find_element_by_css_selector(".PackageDependencies__addPackage")

    @property
    def package_name_input(self):
        return self.driver.find_element_by_css_selector(".PackageDependencies__input")

    @property
    def version_name_input(self):
        return self.driver.find_element_by_css_selector(".PackageDependencies__input--version")

    @property
    def add_button(self):
        return self.driver.find_element_by_css_selector(".PackageDependencies__btn--round")

    @property
    def install_packages_button(self):
        return self.driver.find_element_by_css_selector(".PackageDependencies__btn--absolute")

    @property
    def pip_tab_button(self):
        return self.driver.find_element_by_css_selector(".PackageDependencies__btn--absolute")

    @property
    def apt_tab_button(self):
        return self.driver.find_element_by_css_selector(".PackageDependencies__tab:nth-child(3)")

    @property
    def conda3_tab_button(self):
        return self.driver.find_element_by_css_selector(".PackageDependencies__tab:nth-child(2)")

    @property
    def custom_docker_edit_button(self):
        return self.driver.find_element_by_css_selector(".CustomDockerfile__btn--edit")

    @property
    def custom_docker_text_input(self):
        return self.driver.find_element_by_css_selector(".CustomDockerfile__textarea")

    @property
    def custom_docker_save_button(self):
        return self.driver.find_element_by_css_selector(".CustomDockerfile__content-save-button")


class ContainerStatus(UiElement):
    @property
    def container_status_stop(self):
        return self.driver.find_element_by_css_selector(".flex>.Stopped")

