import math

def hello(a_name):
  print("Hello! "+a_name)


def hello2(a_name,b_name):
  print("Hello!" +a_name+"and"+b_name+"!")


def sum_two(x,y):
  z=x+y
  return z


def circle_area(radius):
    a = math.pi*radius**2
    return a

import datetime

def today():
  now=datetime.datetime.now()
  return now.day


def my_sum(a_list):
  total=0
  for n in a_list:
    total = total + n 
  return total 


import code

def my_prod(a_list):
  total = 1
  for n in a_list: #important to put double point
    total=total*n
  return total


#how many items in a list 
def my_count(a_list):
  count = 0
  for n in a_list:
    count = 1 + count #not necessary to use n/n here, 1 goes as well 
  return count 


 #how many numbers<5 
def my_count_less_5(a_list):
  count = 0
  for n in a_list:
    if n < 5:
      count = count + 1
  return count #return on this level to get return 


#how many times number 1 appears in list 
def my_count_ones(a_list):
  count = 0
  for n in a_list:
    if n==1:
      count = count + 1
  return count 

  
#define the maximum value in the list
def my_max(a_list):
  b = 0 #b is the maximum
  for n in a_list:
    if n>b:
      b=n
  return b 


#is the list empty? approach 1
def is_the_list_empty(a_list):
  if my_count(a_list)==0:
    return True
  else:
    return False 


#is the list empty? approach 2
def my_max(a_list):
  return None
  b=a_list[0]
  for n in a_list:
    if n>b:
      b=n
  return b



import os

#get_filenames("c:\\users\\sback")
#--> list of file names 
# [code.py  imageprocessor.py  loops.py  start.py]


def get_filenames(a_dirnames): #this gives the full path of all files in directory
  list_of_files = os.listdir(a_dirnames)#listdir gives you all the files within the folder (also other files)
  print ("list of file names:") #this gives you the file names 
  print (list_of_files)
  all_files = [] #prepare an empty list
  for filename in list_of_files: #n is the name of the file
    full_path = os.path.join(a_dirnames,filename)#os.list.join-> converts the slash(mac) or backslash(windows) in right way. Also a_dirname is connected to the filename
    if not os.path.isdir(full_path):#if it is not a directory (another file within a file)
      all_files.append(full_path) #append the paths to the files
  return all_files
   


#[12,34,[56,67],78] -> [12,34,56,67,78] 
def flatten(a_list_with_lists):
  new_list = []
  for n in a_list_with_lists:
    if isinstance(n,list):
      for i in n:
        new_list.append(1)
    else:
      new_list.append(n)
  return new_list

#[12,34,[56,67],78] -> #hint: use print(..,end=' ')
#12
#34
#5667
#78

def print_right(a_list_with_lists):
  for n in a_list_with_lists:
    if isinstance(n,list):
      for i in n:
        print(i,end='')
      print('')
    else:
      print(n)


#single_row_stars(4) --> ****
def single_row_stars(number):
  for n in range(number):
    print('*', end='')

def single_row_of(number,string):
  for n in range(number):
    print(string, end='')


# square_of_stars(4)
# -> a square of four rows and four columns

def square_of_stars(number):
  for m in range(number):
    for m in range(number):
      print('*', end='')
  print('')


#list_by_2([1,2,3]) -> [2,4,6]
def list_by_2(a_list):
  new_list_by_2=[]
  for b in a_list:
    new_list_by_2.append(b * 2)
  return new_list_by_2

#create_grid(4)
# -> 4 rows and 4 columns of '-'
# 2 for loups 
# in the inner list (size)
def create_grid(size):
  new_grid=[]
  for row in range(size):
    new_sublist=[]
    for column in range(size):
      new_sublist.append('-')
    new_grid.append(new_sublist)
  return new_sublist









