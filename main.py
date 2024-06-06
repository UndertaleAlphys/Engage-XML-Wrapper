import json
from typing import Optional

MOD_DIRECTORY = 'mod_directory'
MOD_NAME = 'mod_name'
CONFIG_FILE_PATH = 'Config/options.json'


class Options:
    # The options of the program
    # Defines the basic mod path
    mod_directory: str
    mod_name: str

    def __init__(self, mod_directory: str = '', mod_name: str = '') -> None:
        self.mod_directory = mod_directory
        self.mod_name = mod_name


class OptionsController:

    # Return None if failed
    @staticmethod
    def load(file_name: str = CONFIG_FILE_PATH) -> Optional[Options]:
        try:
            with open(file_name, 'r') as f:
                option = json.load(f)
        except IOError:
            return None
        return option

    # Return False if failed
    @staticmethod
    def save(options: Options, file_name: str = CONFIG_FILE_PATH) -> bool:
        try:
            with open(file_name, 'w') as f:
                json.dump(options, f)
        except IOError:
            return False
        return True

    @staticmethod
    def is_invalid(options: Optional[Options]) -> bool:
        return options is None or options.mod_directory == '' or options.mod_name == ''


def main() -> None:
    # load options
    options = OptionsController.load()

    # new user
    if OptionsController.is_invalid(options):
        if options is None:
            options = Options()
        while not options.mod_directory:
            options.mod_directory = input('请输入模拟器模组文件夹路径:')
        while not options.mod_name:
            options.mod_name = input('请输入模组名称:')
        # save the options
        OptionsController.save(options)
    print(f'当前模组文件夹路径: {options.mod_directory}')
    print(f'当前模组名: {options.mod_name}')


if __name__ == '__main__':
    main()
