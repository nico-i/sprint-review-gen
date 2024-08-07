import logging

from src.infrastructure.interfaces.jira.jira_scraper import JiraScaper
from src.infrastructure.logging.logger import get_logger

logger = get_logger(logging.INFO)
scraper = JiraScaper(jira_login_url="https://service-desk.1nce.com/login.jsp?os_destination=%2Fsecure%2FRapidBoard.jspa%3FprojectKey%3DFE%26rapidView%3D247", board_url="https://service-desk.1nce.com/secure/RapidBoard.jspa?projectKey=FE&rapidView=247", logger=logger)

