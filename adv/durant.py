if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *
from slot.d import *

def module():
    return Durant

class Durant(Adv):
    a1 = ('a',0.13,'hp100')
    a3 = ('cd',0.17,'hp100')

    conf = {}
    conf['slot.a'] = Seaside_Princess()+FWHC()
    conf['slot.d'] = Marishiten()

    conf['acl'] = """
        `s1
        `s2
        `s3, seq=5
        """

if __name__ == '__main__':
    adv_test.test(module(), conf, verbose=-2)

