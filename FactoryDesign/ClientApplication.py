# The Client
from osfactory import OSFactory

osObj = OSFactory().create_object('Windows')
print(osObj.name + " selected as current OS")