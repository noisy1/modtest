import sys
print (sys.path,"\n\n\n")

#from modpak import *

#import modpak.L1Adir, modpak.L1Adir.L2Adir, modpak.L1Adir.L2Adir.L3Afile

from modpak.L1Adir.L2Adir.L3Afile import printme

print("main: import of printme complete")
printme("called from main")