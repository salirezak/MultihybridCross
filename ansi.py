def LEFT_CURSOR(x): return f'\033[{x}D'
def UP_CURSOR(x): return f'\033[{x}F'


RESET_C = '\033[0m'
BLUE_C = '\033[94m'
GREEN_C = '\033[92m'
YELLOW_C = '\033[93m'
RED_C = '\033[91m'
MAGENTA_C = '\033[95m'
CLEAR_TO_END = '\033[0J'
SAVE_CURSOR = '\0337'
LOAD_CURSOR = '\0338'
CYAN_C = '\033[96m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'