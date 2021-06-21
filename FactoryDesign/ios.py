from interface_os import IOperatingSystem


class IOS(IOperatingSystem):
    """A Concrete Class that implements the IOperatingSystem interface"""

    def __init__(self):
        self.name = "iOS"

    def getOSInfo(self):
        return self