from ios import IOS
from linux import Linux
from solaris import Solaris
from windows import Windows


class OSFactory:
    """The Factory Class"""

    @staticmethod
    def create_object(osName):
        """A static method to get a concrete product"""
        if osName == 'Windows':
            return Windows()
        if osName == 'Linux':
            return Linux()
        if osName == 'Solaris':
            return Solaris()
        if osName == 'IOS':
            return IOS()
        return None
