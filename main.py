# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="MTJ"
__date__ ="$12-ott-2016 10.32.27$"
#!/usr/bin/env python
#import matplotlib
#Force matplotlib to not use any Xwindows backend.
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
from agent import agent
from group import group
from numpy import *
from numpy.core.numeric import zeros
import random
import simulation


#import community
#import networkx as nx

#import csv
from time import clock

font1 = {'family'     : 'serif',
        'color'      : 'k',
        'weight' : 'normal',
        'size'   : 18,
        }

start = clock()

print "Settings..."

nr_agent = 1000

nr_simulation = 30

max_steps_sim = 1000000

opt_asyn = 1

len_strategy = 5

print "Nr Agents: ",nr_agent," nr bit strategy",len_strategy," for ",max_steps_sim," time steps"


lista_divisori = []
for i in range(2,nr_agent):
    if nr_agent%i==0:
        primo=False
	lista_divisori.append(i)

lista_divisori.append(nr_agent)
payoff_list = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
div = 0

res_matrix = zeros((len(lista_divisori),len(payoff_list)),float)
res_matrix_b = zeros((len(lista_divisori),len(payoff_list)),float)

while div < len(lista_divisori):
    group_size = lista_divisori[div]
    pay_ind = 0
    while pay_ind < len(payoff_list):
	payoff = payoff_list[pay_ind]

	result = 0.0
	res_b = 0.0
	result,res_b = simulation.perform_sim(nr_agent, group_size, payoff,nr_simulation,len_strategy,max_steps_sim)
	print "Nr agents ",nr_agent," group size ",group_size," payoff ",payoff," RESULT: ",result," breaking ",res_b
	res_matrix[div][pay_ind] = result
	res_matrix_b[div][pay_ind] = res_b


	pay_ind+=1

    print "Time: ",clock()-start," seconds!"
    div+=1

name_group = 'result_agent_%i_string_len_%i.txt' % (nr_agent,len_strategy)
name_break = 'result_break_agent_%i_string_len_%i.txt' % (nr_agent,len_strategy)

savetxt(name_group, res_matrix)
savetxt(name_break, res_matrix_b)
