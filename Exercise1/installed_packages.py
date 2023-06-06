import sys
import pkg_resources

# print python version
print(f"\nPython version: {sys.version}")


# print installed packages
print("\nInstalled Packages:")

installed_packages= pkg_resources.working_set

for package in installed_packages:
    print(package.key,  package.version)


