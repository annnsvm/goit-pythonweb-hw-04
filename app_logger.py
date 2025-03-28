import logging
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": Fore.CYAN,
        "INFO": Fore.BLUE,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.MAGENTA,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, Fore.WHITE)
        log_message = super().format(record)
        return f"{log_color}{log_message}{Style.RESET_ALL}"

logger = logging.getLogger('log_cat')
logger.setLevel(logging.DEBUG)

# Creating a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Formatter with colors
formatter = ColoredFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

# Handler without colors (for writting in to file)
fh = logging.FileHandler("app.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(fh)