from logging import Logger

from selenium import webdriver


class JiraScaper:
    """Web scraper for a Jira board"""

    def __init__(self, jira_login_url: str, board_url: str, logger: Logger):
        self.__cookies = None
        self.__jira_login_url = jira_login_url
        self.__board_url = board_url
        self.__logger = logger

        self.__prompt_login()

    def __prompt_login(self):
        """Prompt the user to log in to Jira and retrieve the cookies"""
        print("In the next step a browser window will open. Please log in to Jira and return to the terminal.")
        input("\nPress Enter to open the login page...")

        driver = webdriver.Chrome()

        driver.get(self.__jira_login_url)
        input("Please confirm you have logged in by pressing Enter...")

        self.__cookies = driver.get_cookies()
        self.__logger.info(f"Retrieved cookies: {self.__cookies}")
