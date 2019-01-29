
from workhelper.src.main.project.basework import basework

ICBC_ROOT = '/Users/liuqi/Documents/SVN/SmartSVN/EsSoftware/Products/eBankMidwareV2/Branches/Icbc_Develop/Tags/EsSlotApiM-7629'
ICBC_ANDROID_AS_PROJECT = '%s/ASProject' % ICBC_ROOT
ICBC_IOS_PROJECT =  '%s/iOSProject' % ICBC_ROOT

class icbcwork(basework):
    def test(self):
        print()
    def openandroidas(self):
        self.opendir(ICBC_ANDROID_AS_PROJECT)
    def openios(self):
        self.opendir(ICBC_IOS_PROJECT)
    def openroot(self):
        self.opendir(ICBC_ROOT)