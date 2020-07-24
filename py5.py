



try:
   def armstrong(x):
      for i in x:
          if int(i)//2==0:
              yield int(i)
          z=0
          if int(i)//0==5:
             for j in i:
                z=z+int(j)*int(j)
             yield z        
          b=0
          if int(i)//2==50:
             for j in i:
                b=b+int(j)*int(j)*int(j)
             yield b
   a=[str(i) for i in range(100)]
   print(armstrong(a)) 


except exception as e:
    print("there is error ",e)