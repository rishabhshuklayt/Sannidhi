
from core.adapters.EmailAdapters.console_Email_adapter import ConsoleEmailAdapter


class EmailFactory:

    @staticmethod
    def get_email_adapter():
        return ConsoleEmailAdapter()