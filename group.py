# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="marcoj"
__date__ ="$11-ott-2016 12.20.07$"

class group:

    def __init__(self,name,agents,payoff):
        self.name = name
        self.agents = agents
        self.payoff = payoff
        
    
    def AddAgent(self,new_agent):
        self.agents.append(new_agent)

    def RemoveAgent(self,agent):
        w=0
        new_group = []
        while w < len(self.agents):
            if self.agents[w] != agent:
                new_group.append(self.agents[w])
            w+=1
        self.agents = []
        self.agents = list(new_group)

    def FreeGroup(self):
        self.agents = []
        self.payoff = 0