if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
from slot.a import *

def module():
    return Lily

class Lily(adv.Adv):
    a1 = ('a',0.15,'hp100')
    a3 = ('prep','100%')

    conf = {}
    conf['slot.a'] = CC()+Seaside_Princess()
    conf['acl'] = """
        #prep=0
        #if pin=='prep': prep=1
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5 and cancel
        `s3, s
        `s2, pin='prep'
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)



