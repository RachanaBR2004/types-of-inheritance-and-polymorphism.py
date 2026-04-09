'''class father:
    def height(self):
        print("child gets height from father")
class mother:
    def color(self):
        print("child gets color from mother")
class child(mother,father):
    def weight(self):
        print("child weight is 3kg")
c=child()
c.height()
c.color()
c.weight()

class onlinepayment:
    def pay_online(self):
        print("paid using online")
class cashpayment:
    def pay_cash(self):
        print("paid using cash")
class paymentsystem(onlinepayment,cashpayment):
    def make_payment(self,mode):
        self.mode=mode
        if mode=='online':
            self.pay_online()
        elif mode=='cash':
            self.pay_cash()
        else:
            print("paid using other method")
p=paymentsystem()
p.make_payment("barter")'''

'''class person:
    def person_info(self,name='rach',age ='20'):
        self.name=name
        self.age=age
        print(f"name={self.name},age={self.age}")
class salary:
    def show_salary(self,basic_sal=50000):
        self.basic_sal=basic_sal
        print(f"basic_sal={self.basic_sal}")

class shift:
    def shift_timings(self,time=6):
        self.time=time
        print(f"shift_time={self.time}")

class emp(person,salary,shift):
    pass
e=emp()
e.person_info()
e.show_salary()
e.shift_timings'''
    

#doubt

class person:
    def __init__(self,name='rach',age ='20'):
        self.name=name
        self.age=age
    def display1(self):
        print(f"name={self.name},age={self.age}")
        #print(f"name={self.name},age={self.age}")
class salary:
    def __init__(self,basic_sal=50000):
        self.basic_sal=basic_sal
    def display2(self):
        print(f"basic_sal={self.basic_sal}")

class shift:
    def __init__(self,time=6):
        self.time=time
    def display3(self):
        print(f"shift_time={self.time}")

class emp(person,salary,shift):
    person().__init__()
    person().display1()
    salary().__init__()
    salary().display2()
    shift().__init__()
    shift().display3()
    
e=emp()




# muti level inheritance

"""class animal:
    def speak(self):
        print("animal speak...")
class dog(animal):
    def bark(Self):
        print("animal bark...")

class puppy(dog):
    def cat(self):
        print("animal yy...")
p=puppy()
p.speak()
p.bark()
p.cat()"""


""""class hospital:
    def hospital_info(self,name='sanjo',loc='mandya'):
        self.name=name
        self.loc=loc
        print(f" hname={name},hloc={loc}")
class doctor(hospital):
    def doctor_info(self,dept='dermtologist'):
        self.dept=dept
        print(f" dept of doctor={dept}")
class staff(doctor):
    def nurse(self,work='OT'):
        self.work=work
        print(f" work={self.work}")
class patient(staff):
    def ward(self,ward_no=123):
        self.ward_no=ward_no
        print(f" ward_no={self.ward_no}")
class family_mem(patient):
    pass
f=family_mem()
f.hospital_info()
f.doctor_info()
f.nurse()
f.ward()"""

"""class hospital:
    def __init__(self,name='sanjo',loc='mandya'):
        self.name=name
        self.loc=loc
    def hospital_info(self):
        print(f" hname={name},hloc={loc}")
class doctor(hospital):
    def __init__(self,dept='dermtologist'):
        super().__init_()
        super().hospital_info()
        self.dept=dept

    def doctor_info(self):
        print(f" dept of doctor={dept}")
class staff(doctor):
    def __init__(self,work='OT'):
        super().__init_()
        super().doctor_info()
        self.work=work
    def nurse(self):
        print(f" work={self.work}")
class patient(staff):
    def __init__(elf,ward_no=123):
        super().__init_()
        super().nurse()
        self.ward_no=ward_no
    def ward(self):
        print(f" ward_no={self.ward_no}")
class family_mem(patient):
    def __init__(self):
        super().__init__()
        super().ward()

f=family_mem()"""

#hierarchial inhr

'''class grand_father:
    prop_1=1000
    def total_assets(self):
        print("grand father's prop=",self.prop_1)
class father(grand_father):
    prop_2=2000
    def total_assets(self):
        print("grand father's prop=",self.prop_2)
class grand_son(grand_father):
    prop_3=3000
    def total_assets(self):
        print("grand father's prop=",self.prop_3)
f=father()
s=grand_son()
f.total_assets()
s.total_assets()'''

"""class bank:
    cash=1000
    
    @classmethod
    def total_cash(cls):
        print(cls.cash)

class hdfc(bank):
    pass

class statebank(bank):
    cash=2000

    @classmethod
    def total_cash(cls):
        print(cls.cash+bank.cash)
h=hdfc()
s=statebank()
h.total_cash()
s.total_cash()"""


#hybrid inheritance

"""class singer:
    def passion(self):
        print("singing is a passion")
class painter:
    def passion(Self):
        print("painting is my passion")
class artist(painter,singer,):
    pass
    #def passion(self):
        #print("artist passion involves singing and painter ")
a=artist()
a.passion()
print(artist.mro())"""

"""class robo:
    def talk(self):
        print("robo can talk......")
    def walk(self):
        print("robo can walk....")
    def charge(self):
        print("robo can charge....")
class fighter_robo(robo):
    pass
class teacher_robo(robo):#(obj)->u can give object name what ever
    pass
class driver_robo(robo):
    pass
def access_robo(r):
    r.talk()
    r.walk()
    r.charge()
r=robo()
access_robo(r)
print("--------------")
t=teacher_robo()
access_robo(t)
print("-------------")
d=driver_robo()
access_robo(d)
print("------------")
f=fighter_robo()
access_robo(f)"""


"""class bookx:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages
    def __sub__(self,other):
        return self.pages-other.pages

class booky:
    def __init__(self,pages):
        self.pages=pages
b1=bookx(200)
b2=booky(150)
print("total pages=",b1+b2)

print("total pages=",b1-b2)"""

#metod overloading

"""class demo:
    def add(Self,a=10,b=20):
        self.a=a
        self.b=b
        print(self.a+self.b)
    def add(self,a=10,b=30,c=30):
        self a=a
        self b=b
        self.c=c
        print(self.a+self.b+self.c)
d=demo()
d.add()

class addition:
    def add(Self,*args):
        print("sum=",sum(args))
        print(type(args))
a=addition()
a.add(1,2,3,4)"""

#method over riding

'''class father:
    def property(self,phone="iphone",car="tata nano"):
        self.phone=phone
        self.car=car
        print("father phone=",self.phone)
        print("father car=",self.car)
class son(father):
    def property(self,phone="samsung",car="bmw"):
        super().property()
        self.phone=phone
        self.car=car
        print("father phone=",self.phone)
        print("father car=",self.car)
s=son()
s.property()'''
    

        












9














        
        
        






    


        


    
        

        


    

        


        


        
    





















        































            

