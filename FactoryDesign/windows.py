from interface_os import IOperatingSystem


class Windows(IOperatingSystem):
    """A Concrete Class that implements the IOperatingSystem interface"""

    def __init__(self):
        self.name = "Windows"

    def getOSInfo(self):
        return self