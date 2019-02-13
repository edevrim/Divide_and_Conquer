#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:13:22 2019

@author: salihemredevrim
"""

#divide and conquer for finding majority element!

import numpy as np
import pandas as pd

#%%%
def majority(a): #take subarray
    a[1] = 1; #trick .s.s
    len1 = len(a); 
    
    gb = a.groupby(a[0]).sum().reset_index(drop=False); #find frequency per color
    
    temp = 'n/a'; #default is n/a
    
    for i in range(len(gb)):
        
        if (gb[1].loc[i]) / len1 > 0.5: #could be only one majority or none
            temp = gb[0].loc[i];
            
    print('checking majority!');       
    
    return temp;

#%%
def divide_conquer(a): #take subarray 
   
    n = len(a); #find the length of the array

    m = int(np.floor(n/2)); #find the first part, it could be an odd number
    
    left = a.head(m); #take the left side
    right = a.tail(n-m); #take the right side
    
    if len(left) == 1: 
        left_m = majority(left); #if it is in the last level, assign the majority (cell value in most cases)
        print('left length is:', len(left), 'majority is:', left_m); 
    else:
        left_m = divide_conquer(left); #recursive
        print('left length is:', len(left), 'majority is:', left_m);
        
    if len(right) == 1:
        right_m = majority(right); 
        print('right length is:', len(right), 'majority is:', right_m); 
    else:
        right_m = divide_conquer(right); #recursive
        print('right length is:', len(right), 'majority is:', right_m);
    
   # left_m = majority(left); #find the left majority
    # right_m = majority(right); #find the right majority
    
    if left_m == right_m and left_m != 'n/a':  #Case 1 
        major = left_m; 
    elif left_m != 'n/a' and right_m == 'n/a': #Case 3
        major = majority(a);
    elif right_m != 'n/a' and left_m == 'n/a': #Case 3 again
        major = majority(a);  
    else: 
        major = 'n/a'; #Case 2 and 4 
        
    return major; 

#%%
A = pd.DataFrame(['Red','Yellow','Red','Green','Red','Blue','Red','Red','Yellow']);
B = pd.DataFrame(['Red','Yellow','Red','Green']);
C = pd.DataFrame(['Green','Green','Green','Red','Red','Blue','Red']);
D = pd.DataFrame(['Red','Green','Red', 'Yellow','Red', 'Blue','Red']);
E = pd.DataFrame(['Green', 'Yellow', 'Green']);
    
major_last1 = divide_conquer(A); 
major_last2 = divide_conquer(B); 
major_last3 = divide_conquer(C); 
major_last4 = divide_conquer(D); 
major_last5 = divide_conquer(E); 

 

    
    

