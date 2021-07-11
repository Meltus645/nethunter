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
            kwindex =f_name.lower().find('y2mate.com');
            n_name =''
            if kwindex >=0:
                tail =f_name[:kwindex].strip()
                head =f_name[kwindex+len('y2mate.com'):].strip()
                n_name =tail+head
                if n_name[0] =='-':
                    n_name =n_name[1:].strip()
                print(n_name+f_ext)

if __name__ =='__main__':
    RenameFiles()