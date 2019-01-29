import os
class basework:
    def basework(self):
        return self
    def opendir(self, dir):
        cmd = "open %s" % (dir)
        print(cmd)
        os.system(cmd)
