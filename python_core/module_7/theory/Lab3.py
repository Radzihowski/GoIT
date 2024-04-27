class FileOps:
    def __init__(self, path) -> None:
        self.file = open(path, "r")

    def readWords(self):
        pass

    def __del__(self):
        self.file.close()
