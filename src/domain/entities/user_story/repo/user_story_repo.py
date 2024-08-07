from abc import abstractmethod
from typing import List

from src.domain.entities.user_story.user_story import UserStory


class UserStoryRepo:
    """Interface for a User Story Repository"""

    @abstractmethod
    def get_all_user_stories(self) -> List[UserStory]:
        """Get all user stories"""
        pass