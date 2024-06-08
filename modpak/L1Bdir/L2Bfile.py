"""This script relies intended to be invoked directly: python L2Bfile.py and does not use relative imports.
    It ONLY works if the PYTHONPATH environmental variable contains L1Adir and L2Adir - so those directories are searched
    when looking for L2Adir and L3Afile modules.
"""
print("L2Bfile entered")

from pathlib import PurePath
print("L2Bfile run for ",PurePath(__file__).parent.name)
print("package:",__package__)
print("name:",__name__)



print("attempting import of cousin L2Adir\n")
import L2Adir
print("successful import of L2Adir")

print("\nattempting import of printme from L3Afile")
from L3Afile import printme
print("import successful, calling printme")

printme("L2Bfile")