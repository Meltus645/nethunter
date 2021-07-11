import os

class RenameFiles:
    default_dir ='/Users/wajuma/Downloads/Video'
    def __init__(self, path =default_dir):
        self.path =path
        self.rename()
    def rename(self):
        os.chdir(self.path)
        for f in os.listdir():
            f_name,f_ext =os.path.splitext(f)
            n_name =f_name.lower().strip()
            kwindex =n_name.find('y2mate.com');
            if kwindex >=0:
                tail =f_name[:kwindex]
                head =f_name[kwindex+len('y2mate.com'):]
                print(tail+head)

if __name__ =='__main__':
    RenameFiles()