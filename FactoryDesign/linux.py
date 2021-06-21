from interface_os import IOperatingSystem


class Linux(IOperatingSystem):
    """A Concrete Class that implements the IOperatingSystem interface"""

    def __init__(self):
        self.name = "Linux"

    def getOSInfo(self):
        return self