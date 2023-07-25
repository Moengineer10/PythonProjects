

import math

# Pearson Correlation between two vectors
def pearsonD(UserPRatings, UserQRatings): 

# (1)     
    sumpq= 0
    sump = 0
    sumq = 0
    sump2 = 0
    sumq2= 0


UserPRatings = {'Apple':1, 'Samsung':5, 'Nokia':7, 'Motorola':8, 'LG':5, 'Sony':1, 'Blackberry':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}



for k in sorted(UserPRatings.keys()):
       if (k in UserQRatings.keys() ):
   
        print(k, UserPRatings[k], UserQRatings[k]) 
       


# ((2))    

P = [1, 5, 7, 5, 1, 7]
Q= [7, 1, 4, 4, 6, 3]
n=len(P)

sumpq= 0
sump = 0
sumq = 0
sump2 = 0
sumq2= 0

#Pearson correlation using computationally efficient form    
for p, q in zip(P, Q):
    sumpq += p * q
    sump +=  p
    sumq += q
    sump2 += pow(p, 2)
    sumq2 += pow(q, 2)   



#Pearson correlation coefficient
nr= (sumpq-(sump * sumq)/n)
dr= (math.sqrt(sump2 - pow(sump, 2)/ n) *
        math.sqrt(sumq2 - pow(sumq, 2)/ n))    

r = nr/dr

     
print(k, UserPRatings[k], UserQRatings[k]) 
print( "Pearson Correlation:", round(r,4))







    
    

    
    
    
