from interface_os import IOperatingSystem


class Solaris(IOperatingSystem):
    """A Concrete Class that implements the IOperatingSystem interface"""

    def __init__(self):
        self.name = "Solaris"

    def getOSInfo(self):
        return self