from abc import ABCMeta, abstractmethod


class IOperatingSystem(metaclass=ABCMeta):
    """A OS Class Interface (Product)"""

    @staticmethod
    @abstractmethod
    def getOSInfo():
        """An abstract interface method"""
