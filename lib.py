import sys, os


# get the dir of the executable file
def get_exdir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable) + os.sep
    else:
        return os.path.dirname(__file__) + os.sep


def abs_path(path: str) -> str:
    return path if os.path.isabs(path) else get_exdir() + path
