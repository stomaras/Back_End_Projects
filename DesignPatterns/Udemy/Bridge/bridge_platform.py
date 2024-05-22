# Let's say you have a software called FileApp that works on Windows, Linux and MacOs operating system.
# The FileApp carries out file Operations that open, closes and rename files without minding which operating system you install on it.

class FileApp:
    def __init__(self, os_impl):
        self.os_impl = os_impl
        
    # bridge methods
    def open_file(self, path):
        self.os_impl.open_file(path)
    
    def close_file(self, path):
        self.os_impl.close_file(path)
    
    def rename_file(self, old_path, new_path):
        self.os_impl.rename_file(old_path, new_path)
    
#===================IMPLEMENTATION============================
class OperatingSystemImplementation:
    def open_file(self, path):
        pass
    
    def close_file(self, path):
        pass
    
    def rename_file(self, old_path, new_path):
        pass
    
class WindowsImplementation(OperatingSystemImplementation):
    def open_file(self, path):
        print(f'Opening file {path} in Windows')
    
    def close_file(self, path):
        print(f'Closing file {path} in Windows')
    
    def rename_file(self, old_path, new_path):
        print(f'Renaming file {old_path} to {new_path} in Windows')
        
class LinuxImplementation(OperatingSystemImplementation):
    def open_file(self, path):  
        print(f'Opening file {path} in Linux')
        
    def close_file(self, path):
        print(f'Closing file {path} in Linux')
        
    def rename_file(self, old_path, new_path):
        print(f'Renaming file {old_path} to {new_path} in Linux')
        
        
windows = WindowsImplementation()
linux = LinuxImplementation()

file = FileApp(windows)
file.open_file('example.txt')
file.close_file('example.txt')
file.rename_file('example.txt', 'exampleNew.txt')

fileLinux = FileApp(linux)
fileLinux.open_file('example.txt')
fileLinux.close_file('example.txt')
fileLinux.rename_file('example.txt', 'exampleNew.txt')
        
        