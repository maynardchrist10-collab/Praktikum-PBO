# induk
class hero:
    def __init__(self, nama, hp, attack):
        self.nama = nama
        self.hp = hp
        self.attack = attack

    def hitung_damage(self):
        return 0

    def ultimate(self):
        return f"{self.nama} belum punya ultimate"
#anak
class tank(hero):
    def hitung_damage(self):
        return self.attack * 1.2
    
    def ultimate(self):
        return f"{self.nama} mengeluarkan implusion"

class mage(hero):
    def hitung_damage(self):
        return self.attack * 1.5
    
    def ultimate(self):
        return f"{self.nama} mengeluarkan magis"

tim = [
    hero('Badeng', 1000, 100),
    tank('Asoy Merah', 1500, 50),
    mage('Meilonie', 1500, 100) 
]

for hero in tim:
    dmg = hero.hitung_damage()
    print(f"{hero.nama}: {dmg:,.0f} damage")
    print(f'{hero.ultimate()}')

class Penyihir: 
    def __init__(self, nama): 
        self.nama = nama 
    def serang(self): 
        print(f'{self.nama} melempar bola api!') 

class Menara: 
    def serang(self):  
        print('Menara menembakkan laser!') 
        
class Creep: 
    def serang(self): 
        print('Creep memukul pelan.') 
        
class Batu: 
    pass 

def mulai_pertempuran(penyerang_list): 
    for p in penyerang_list: 
        p.serang() 


mulai_pertempuran([ 
    Penyihir('Eudora'), Menara(), Creep(), ]) 

try: 
    mulai_pertempuran([Batu()]) 
except AttributeError as e: 
    print(f'Error: {e}')

from abc import ABC, abstractmethod
class HeroBase(ABC):
    @abstractmethod
    def serangdasar(self):
        pass

    @abstractmethod
    def gunakanultumate(self):
        pass

class layla(HeroBase):
    def __init__(self, level):
        self.level = level

def serangdasar(self):
    print ("layla menembak melefic gun")

def gunakanultimate(self):
    print(f"layla level {self.level}menggunakan skill ultimate nya")

class herobug(HeroBase):
    def serangdasar(self):
        pass

    def gunakanultumate(self):
        pass
hero_1 = layla(15)
hero_1 = gunakanultimate()

class statushero:
    def __init__(self, nama, hp , attack):
        self.nama =nama
        self.hp=hp
        self.attack=attack

    def __add__(self, itemstats):
        hp_baru = self.hp + itemstats.hp
        attack_baru = self.attack + itemstats.attack
        return statushero(self.nama, hp_baru, attack_baru )

    def __gt__ (self, hero_lain):
        return self.hp > hero_lain.hp

    def __str__(self):
        return f"{self.nama}, {self.hp}, {self.attack}"

chou_awal = statushero ("chou", 3000, 150)
bon = statushero ("item1",0, 150 )
nod = statushero ("item1",150, 0 )

chou_jadi = chou_awal + bon+ nod
aldos = statushero ("aldos", 4000 , 300)
print(aldos)
print (f"apakah chou lebih tebal dari aldos {chou_jadi > aldos}")