'''Project 5 - Program 3
by Solmaz Gharagozloo
11/27/18
'''
miles=[]
def weekdays():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:

      x=int(input("Enter the number of miles for "+ day +": "))
      miles.append(x)
    return miles  
      
 
    
def main():
 weekdays()    
    
 counter1=0
 counter2=0
 counter3=0
 for i in range(7):
    if miles[i]<5:
        counter1+=1
    elif miles[i]>=5 and miles[i]<=10:
        counter2+=1
    elif miles[i]>10:
        counter3+=1
         
 print("the number of days you ran less than 5 miles are: ", counter1)  
 print("the number of days you ran between 5 and 10 miles are: ", counter2) 
 print("the number of days you ran more than 10 are: ", counter3) 

main() 