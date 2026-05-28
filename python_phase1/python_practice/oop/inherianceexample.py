class teammember:
    def __init__(self,name,uid):
        self.name = name
        self.uid = uid
class worker:
    def __init__(self,pay,pos):
        self.pay = pay
        self.pos = pos
class tl(teammember,worker):
    def __init__(self, name, uid,pay,pos,exp):
        self.exp = exp
        teammember

class teamleader(teammember,worker):
    def __init__(self,name,uid,pay,pos,exp):
        self.exp=exp
        teammember.__init__(self,name,uid)
        worker.__init__(self,pay,pos)
        print("name: {}, pay:{}, exp:{}".format(self.name,self.pay,self.exp))
tl =teamleader("jake",10001,250000,"scrummaster",5)        
 