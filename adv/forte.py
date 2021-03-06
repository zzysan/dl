from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Forte

class Forte(Adv):
    a3 = ('k_poison', 0.30)

    conf = {}
    conf['slots.a'] = The_Red_Impulse()+Heralds_of_Hinomoto()
    conf['slots.d'] = Epimetheus()
    conf['slots.poison.d'] = Shinobi()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s3, not self.s3_buff
        `s2
        `s1
        `fs, x=5
        """
    coab = ['Ieyasu','Cleo','Bow']

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Ieyasu','Cleo','Wand']

    def s1_proc(self, e):
        self.dragonform.charge_gauge(4, dhaste=False)
        with KillerModifier('s1_killer', 'hit', 0.3, ['poison']):
            self.dmg_make('s1', 11.34)

    def s2_proc(self, e):
        self.dragonform.charge_gauge(4, dhaste=False)
        Selfbuff('s2', 0.20, 15, 'att', 'buff')

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)