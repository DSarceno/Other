import yaml

class Others:
    def __init__(self) -> None:
        pass

    def load_config(self, file_path : str):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config