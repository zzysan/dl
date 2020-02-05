import adv.adv_test
from adv import now
from slot.d import Dreadking_Rathalos
from slot.a import Amulet, The_Lurker_in_the_Woods
import adv.chelsea

def module():
    return Chelsea

class Dear_Diary(Amulet):
    att = 65
    a = [('cc',0.14)]

class Chelsea(adv.chelsea.Chelsea):
    comment = 'roll fs; only use s1 3 times to proc RO at'

    def d_slots(this):
        this.slots.d = Dreadking_Rathalos()
        this.slots.a = The_Lurker_in_the_Woods()+Dear_Diary()

    def d_acl(this):
        this.conf['acl'] = """
            `s3,not this.s3_buff_on
            `s2,fsc
            `s1,fsc and this.hp < 30 and this.ro_charges > 0
            `dodge, fsc
            `fs
        """

    def prerun(this):
        super().prerun()
        this.ro_charges = 3
        # adv.Buff('resilient_offense',0.10, -1).on()
        # this.comment += ' 0s'
        # this.hp = 20

    def dmg_before(this, name):
        hpold = this.hp
        super().dmg_before(name)
        if this.ro_charges > 0 and hpold > 30 and this.hp < 30:
            adv.Buff('resilient_offense',0.10, -1).on()
            this.comment += ' {}s'.format(round(now()))
            this.ro_charges -= 1

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)