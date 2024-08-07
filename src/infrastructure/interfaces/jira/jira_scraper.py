class JiraScaper:
    """Web scraper for a Jira board"""
    
    def __init__(self, jira_url: str):
        self.__jira_url = jira_url