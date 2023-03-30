class Acount:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.acount = []
        

    def check(self,id):
        print(id)
        if id != self.id :
            self.acount.append(id)
            
            return True
        return False



class Register(Acount):
    def __init__(self, id, password) :
        super().__init__(id, password)
        self.acount = ""
    
        
    def geta(self):
        self.acount = Acount() 


    def add_(self):
        # ตรวจสอบ ID PASSWORD
        self.acount.check(self.id)







# class check(Register):
#     def __init__(self, id, password):
#         super().__init__(id, password)
#         self.acount = ""

#     def geta(self):
#         self.acount = Acount() 


# class add_ac(Register):
#     def __init__(self, id, password):
#         super().__init__(id, password)

#         def



# class Login(Acount):
    
        
#     def check_l(self, id, password):
        

        








s1 = Register("001", "brawny")
s2 = Register("002", "brawny")

s2.add_
s1.add_


