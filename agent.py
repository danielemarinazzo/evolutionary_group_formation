# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="marcoj"
__date__ ="$11-ott-2016 12.20.07$"

class agent:

    def __init__(self,name,strategy):
        self.name = name
        self.strategy = strategy
        self.neigh_list = []
        self.group_name = 0
        
    
    def SetStrategy(self,new_strategy):
        self.strategy = new_strategy
    
    def SetGroupName(self,group):
        self.group_name = group
    
    def FreeAgent(self):
        self.group_name = 0


    def SetNewNeigh(self,new_neigh):
        self.neigh_list.append(new_neigh)

    def RemoveNeigh(self,neigh):
        w=0
        new_list = []
        while w < len(self.neigh_list):
            if self.neigh_list[w] != neigh:
                new_list.append(self.neigh_list[w])
            w+=1
        self.neigh_list = []
        self.neigh_list = list(new_list)


