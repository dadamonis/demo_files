from datetime import datetime

class Tr:
    def __init__(self, amt, t_type):
        self.a = amt
        self.t = t_type
        self.d = datetime.now()

class BnkAcc:
    def __init__(self, acc_num, init_bal=0):
        self.acc_num = acc_num
        self.b = init_bal
        self.t = []

    def dep(self, amt):
        self.b += amt
        self.t.append(Tr(amt, 'Dep'))
    
    def wdraw(self, amt):
        if amt <= self.b:
            self.b -= amt
            self.t.append(Tr(amt, 'Wdraw'))
        else:
            print("No money")

    def od(self):
        return self.b < 0

class SAcc(BnkAcc):
    def __init__(self, acc_num, init_bal=0, ir=0.01):
        super().__init__(acc_num, init_bal)
        self.ir = ir

    def ai(self):
        int_amt = self.b * self.ir
        self.dep(int_amt)

class Cust:
    def __init__(self, nm, cid):
        self.nm = nm
        self.cid = cid
        self.accts = {}

    def add_acc(self, acc):
        self.accts[acc.acc_num] = acc

    def get_acc(self, acc_num):
        return self.accts.get(acc_num)

    def get_tot_bal(self):
        return sum(acc.b for acc in self.accts.values())