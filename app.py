import os

class RenameFiles:
    default_dir ='/Users/wajuma/Downloads/Video'
    def __init__(self, path =default_dir):
        self.path =path
        self.rename(self.check_keyword)
    def rename(self, filename):
        os.chdir(self.path)
        for f in os.listdir():
            f_name,f_ext =os.path.splitext(f)
            n_name =f_name.lower().split('y2mate.com')[1].strip()
            if n_name[0] =='-':
                n_name =f_name.split('-')[1].strip()
            n_name =n_name+f_ext
            print(n_name.find('y2mate'))
    def check_keyword(self):
        return filename
        
if __name__ =='__main__':
    RenameFiles()