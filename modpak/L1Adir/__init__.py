from pathlib import PurePath
print("init run for ",PurePath(__file__).parent.name)
print("package:",__package__)
print("name:",__name__)
print("exiting init\n")