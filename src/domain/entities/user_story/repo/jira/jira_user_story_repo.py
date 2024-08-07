from src.domain.entities.user_story.repo.user_story_repo import UserStoryRepo
from src.infrastructure.interfaces.jira.jira_scraper import JiraScaper


class JiraUserStoryRepo(UserStoryRepo):
    """Jira User Story Repository"""

    def __init__(self, jira_scraper: JiraScaper):
        self.__jira_scraper = jira_scraper

    def get_all_user_stories(self):
        raise NotImplementedError