import os

class RenameFiles:
    default_dir ='/Users/wajuma/Downloads'
    def __init__(self, path =default_dir):
        self.path =path
        self.rename()
    def rename(self):
        os.chdir(self.path)
        print(os.getcwd())

if __name__ =='__main__':
    RenameFiles()