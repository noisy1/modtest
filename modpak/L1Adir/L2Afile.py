def printme(caller):
    print("\nprintme called from ",caller, "\nfile is: ", __file__, "\nname is: ",__name__,"\npackage is:",__package__)

printme("L2Afile.py")

print("\nL2Afile attempting cousin import")
from .. import L1Bdir

