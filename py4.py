x=12345
y=input("ente password")
while True:
    try:

      if int(y)==x:
        print("u r in")
        break
      elif y=="done":
          print("u r in")
          break



    except:
        print("invalid")
        y=input("enter corect password  :")
