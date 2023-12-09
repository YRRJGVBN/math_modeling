import sys, os
 
print(os.getcwd())
 
os.system("echo hi!")

print("Python version is:", sys.version)
print(sys.path)
print(sys.platform)
	
print(dir(sys))