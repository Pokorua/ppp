from codecs import namereplace_errors
from ctypes.wintypes import HPALETTE
from xml.dom import domreg


class Enemy:

    def __init__(self, hp, dmg, name) -> None:
        self.hp = hp 
        self.dmg = dmg
        self.name = name

    def spawn(self):
        print(f'Появляется враг - {self.name}')    

zb = Enemy(100, 10, 'Horr')    
zb.spawn()

class Enemy_1(Enemy):

    def damage(self):
        print(f'Вам нанесено {self.dmg * 10} урона')

zzb = Enemy_1(10000, 45363, 'Boss' )
zzb.spawn()
zzb.damage()            