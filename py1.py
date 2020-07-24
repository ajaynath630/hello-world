class animal:
    def __init__ (self,color,typeof,legs):
         self.color=color
         self.type=typeof
         self.legs=legs
    def get_animal(self):
        print(self.color) 
        print(self.type)    
        print(self.legs)
    def action(self):
        print(self.color+" "+"animal is"+" "+self.type+" having"+" "+self.legs+" "+"legs")    

        
elphant=animal("black","not wild","four")
elphant.get_animal()
elphant.action()





lion=animal("red","wild","four")        
lion.get_animal()
def abc(a):
    for i in range(len(a)):
        a[i]="bat"
        print(a[i])
    return a     
a=[8,"dog","pig","rabbit"]       
print(abc(a))

y="yes" 
while y=="yes":
    y=input("yes or no")  
else:
    print("dh")       




line="From an india ro usa \n \n widhd djksjkd hdhdj hdjdj hdhjd \n hdhsjhs hdjdjd\n hdjdkslsjk."
line=line.split()
print(line)

