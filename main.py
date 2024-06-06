import json

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
    @staticmethod
    def load(file_name: str = CONFIG_FILE_PATH) -> Options:
        with open(file_name, 'r') as f:
            option = json.load(f)
        return option

    @staticmethod
    def save(option: Options, file_name: str = CONFIG_FILE_PATH) -> None:
        with open(file_name, 'w') as f:
            json.dump(option, f)

    @staticmethod
    def create_empty(file_name: str = CONFIG_FILE_PATH) -> None:
        OptionsController.save(Options(), file_name)


def main() -> None:
    pass


if __name__ == '__main__':
    main()
