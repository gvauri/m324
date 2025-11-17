class File:
    def __init__(self):
        pass

    def create_file(self, filename: str):
        open(filename, "w").close()

    def write_to_file(self, filename: str, text: str):
        with open(filename, "w") as f:
            f.write(text)

    def read_from_file(self, filename: str) -> str:
        with open(filename, "r") as f:
            return f.read()
