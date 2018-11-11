import platform
import sys

class Colour:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    GRAY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    DARKGRAY = '\033[30m'
    DARKRED = '\033[31m'
    DARKGREEN = '\033[32m'
    DARKYELLOW = '\033[33m'
    DARKBLUE = '\033[34m'
    DARKPURPLE = '\033[35m'
    DARKCYAN = '\033[36m'
    DARKWHITE = '\033[37m'

    FULLDARKGRAY = '\033[40m'
    FULLDARKRED = '\033[41m'
    FULLDARKGREEN = '\033[42m'
    FULLDARKYELLOW = '\033[43m'
    FULLDARKBLUE = '\033[44m'
    FULLDARKPURPLE = '\033[45m'
    FULLDARKCYAN = '\033[46m'
    FULLDARKWHITE = '\033[47m'

    FULLGRAY = '\033[100m'
    FULLRED = '\033[101m'
    FULLGREEN = '\033[102m'
    FULLYELLOW = '\033[103m'
    FULLBLUE = '\033[104m'
    FULLPURPLE = '\033[105m'
    FULLCYAN = '\033[106m'
    FULLWHITE = '\033[107m'

    def print(message,colour='',end='\n'):
        os_name = Colour.__get_os_name()
        end_colour = Colour.END
        if(os_name == 'windows'):
            colour = ''
            end_colour = ''
        # print(colour + message + end_colour,end=end)
        sys.stderr.write(colour + message + end_colour + end)

    @staticmethod
    def __get_os_name():
        os_name = platform.system().lower()
        if 'window' in os_name:
            return 'windows'
        if 'darwin' in os_name:
            return 'mac'
        if 'linux' in os_name:
            return 'linux'
        return None

