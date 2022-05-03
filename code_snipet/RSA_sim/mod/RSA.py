class rsa:
    def __init__(self, p = None, q = None, e = None, d = None):
        self.p = p
        self.q = q
        self.n = self.cal_n(self.p, self.q) 
        self.ph = self.cal_ph(self.p, self.q)
        self.e = e
        self.d = self.cal_d(self.e)

    def cal_n(self, p, q):
        if p and q:
            return p * q
        return None
    
    def cal_ph(self, p, q):
        if p and q:
            return (p-1) * (q-1)
        return None

    #d x e mod Φ =1
    def cal_d(self,e):
        d = 1
        if e and self.ph:
            while (d * e) % self.ph != 1:
                print(f"d is now: {d}, (d * e) mod self.ph = {(d * e) % self.ph}")
                d += 1
            print(f"d is now: {d}, (d * e) mod self.ph = {(d * e) % self.ph}")
            return d
        return None

    def display(self):
        print(f"Public key:\n\te = {self.e}, n = {self.n}")
        print(f"Private key:\n\td = {self.d}, Φ = {self.ph}")