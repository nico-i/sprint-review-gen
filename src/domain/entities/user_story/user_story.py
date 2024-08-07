
from attr import dataclass


@dataclass
class UserStory:
    """Model of a Jira User Story"""
    title: str
    url: str
    assignee: str
    is_only_mentionable: bool

    def to_presentable_story_md(self):
        return f"""## {self.title}
    
        **Story:** {self.url}
        **Presenter:** {self.assignee}
        **Comments:** -"""
        
    def to_mentionable_md(self):
        return f"""- ${self.url}"""