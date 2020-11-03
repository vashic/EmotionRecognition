# -*- coding: utf-8 -*-
"""AI_Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wvni8ozKX7ioMcl6t97A0uORd_FMK7oQ

Hi guys! Create Cells and add your codes!

Fitness
"""

from Fitness_Function import Fitness

####################### TOURNAMENT ############################################
import random
def tournament_selection(pop, k):
    best = 0
    for i in range (1, k):
        randi = random.randint(0, len(pop)-1)
        #print("lenght of pop "+str(len(pop)))
        #print(randi)
        #print(best)
        #ind = pop[randi]
        #print(type(randi), type(best))
        if (best == 0) or (fitnesslist[randi] > fitnesslist[best]):
            best = randi
    return pop[best]

################### ROULETTE ##################################################
'''
def weighted_random_choice(chromosomes):
    max = sum(fitnesslist[chromosomes.index(chromosome)] for chromosome in chromosomes)
    pick = random.uniform(0, max)
    current = 0
    for chromosome in chromosomes:
        current += chromosome.fitness
        if current > pick:
            return chromosome
'''        
def weighted_random_choice(chromosomes):
    max = sum(fitnesslist[chromosomes.index(chromosome)] for chromosome in chromosomes)
    pick = random.uniform(0, max)
    current = 0
    for chromosome in chromosomes:
        current += fitnesslist[chromosomes.index(chromosome)]
        if current > pick:
            return chromosome

####### CROSSOVER #############################################################

############## single-point #########################

#p1= parent 1, p2= parent 2, n=number of bits
#import random
def single_point_crossover(p1,p2,n):
  p1=list(p1) #string to array
  p2=list(p2)

  k= random.randint(0,n-1)

  #print("k: ",k)

  for i in range (k, n-1):
    p1[i],p2[i] =p2[i],p1[i]

  p1 = ''.join(p1) #array to string
  p2 = ''.join(p2)
  return p1,p2
'''
#code to test the crossover function
p1 = '1010000101'
p2 = '1111111111'
n = len(p1)
p1,p2=single_point_crossover(p1,p2,n)
print("p1: ", p1,"\n") 
print("p2: ", p2,"\n")
'''
############# multi-point #################################
#This will automatically include two point crossover
#but not single point so a separate method is defined for it

#p1= parent 1, p2= parent 2, n=number of bits
#import random
def multi_point_crossover(p1,p2,n):
  p1=list(p1)
  p2=list(p2)

  k= random.randint(0,n-1) # number of points for crossover

  arr = []
  for i in range (1,k):
    q=random.randint(0,n-1)
    if q not in arr:#to eliminate duplicates
      arr.append(q) # stores set of points that divide the array into segments

  arr.sort()

  m=len(arr)
  #print("Array of points: ",arr)
  for x in range(0,m-1,2): #crossover for every alternate segment is done
    for i in range (arr[x], arr[x+1]): 
      p1[i],p2[i] =p2[i],p1[i]
      
  p1 = ''.join(p1)
  p2 = ''.join(p2)
  return p1,p2
'''
#code to test the crossover function
p1 = '0000000000'
p2 = '1111111111'
n = len(p1)
p1,p2=multi_point_crossover(p1,p2,n)
print("p1: ", p1,"\n")
print("p2: ", p2,"\n")
'''
################## uniform cross-over ##########################

#p1= parent 1, p2= parent 2, n=number of bits

def uniform_crossover(p1,p2,n):
  p1=list(p1)
  p2=list(p2)
  k= random.randint(0,n-1) # number of flips to be done

  arr = []

  for i in range (1,k): # for position of flips
    q=random.randint(0,n-1)
    if q not in arr: #to eliminate duplicates
      arr.append(q)  #array stores the position where flips are to be done

  arr.sort()

  print("Array of points: ",arr)
  for x in arr:
    p1[x],p2[x] =p2[x],p1[x]
    
  p1 = ''.join(p1)
  p2 = ''.join(p2)
  return p1,p2
'''
#code to test the crossover function
p1 = '0000000000'
p2 = '1111111111'
n = len(p1)
p1,p2=uniform_crossover(p1,p2,n)
print("p1: ", p1,"\n")
print("p2: ", p2,"\n")
'''

############### MUTATION #####################################################
#p is gene to be mutated, n is number of bits 
#import random
def mutation_single_point(p,n) :
  p=list(p) #string to array 
  index=random.randint(0,n-1) #index to be mutated
  #print("index: ",index)
  p[index]=str(1-int(p[index]))
  p = ''.join(p) #array to string
  return p
'''
#code to test the mutation function
  p = '0001110'
  n=len(p)
  p=mutation_single_point(p,n)
  print(p)
'''
#p is gene to be mutated, n is number of bits , h is the number of bits to be reversed
#import random
def mutation_inversion(p,n,h):
  p=list(p) #string to array 
  index=random.randint(0,n-h+1) #index from where inversion has to be started
  print(index)
  p[index:h+index]=reversed(p[index:h+index]) #inversion from index for h bits
  p=''.join(p) #array to string
  return p
'''
#code to test the mutation function
  p='00011101'
  n=len(p)
  h=4
  p=mutation_inversion(p,n,h)
  print(p)
'''

################ GA ##########################################################

pop = ['111111','111110','111101','111011','110111','101111','111100','111000','110000','100111']
pop_size = len(pop)
#acc=0
iter=0
num_pairs=4
iter=0

while (1):
  #Evaluate fitness of every chromosome
  fitnesslist=[]
  for i in range(pop_size):              
    fitnesslist.append(Fitness(pop[i]))

  #Termination Condition
  if ((max(fitnesslist)>70)or(iter==5)):
    max_index=fitnesslist.index(max(fitnesslist))
    break;

  else :
  #Reproduction phase  
    next_generation=[]
    for i in range(num_pairs):
      #generate parents
      mom = tournament_selection(pop, 7)
      #print(pop.index(mom))
      dad = tournament_selection(pop, 7)
      #print(pop.index(mom))
      #produce kids through crossover
      kid1, kid2 = multi_point_crossover(dad,mom,len(dad))

      #mutate kids
      mutation_single_point(kid1,len(kid1))
      mutation_single_point(kid2,len(kid2))

      #construct the new generation by adding new kids
      next_generation.extend([kid1, kid2])

  #Elitism 
    max_index = fitnesslist.index(max(fitnesslist)) #index of most fit chromosome obtained
    #print(max_index)

    copy_fitnesslist = fitnesslist                  #process to get index of chromosome with 2nd highest fitness
    copy_fitnesslist.remove(max(copy_fitnesslist))
    second_max_value = max(copy_fitnesslist)
    second_max_index = fitnesslist.index(second_max_value) #index of 2nd most fit chromosome obtained
    #print(second_max_index)

    next_generation.extend([pop[max_index],pop[second_max_index]]) #new generation completed, with 8 kids and 2 best people from the older generation

  #Replace older generation with the next generation
    pop = next_generation
  
  #Update counter
    iter=iter+1 

#print('Test!')
#print(max_index)
print(pop[max_index])