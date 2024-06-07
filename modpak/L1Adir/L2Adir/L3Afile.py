def printme(caller):
    print("\nprintme called from ",caller, "\nfile is: ", __file__, "\nname is: ",__name__,"\npackage is:",__package__)

printme("L3Afile.py")

print("\nL3Afile attempting cousin import")
from ... import L1Bdir