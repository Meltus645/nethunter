import os

class RenameFiles:
    default_dir ='/Users/wajuma/Downloads/Video'
    def __init__(self, path =default_dir):
        self.path =path
        self.rename()
    def rename(self):
        os.chdir(self.path)
        for file in os.listdir():
            name,extension =os.path.splitext(file)
            print(name)

if __name__ =='__main__':
    RenameFiles()