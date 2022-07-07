vechiles = 200
wheels = 540
if (wheels&1)==1 or wheels<1 or wheels<=vechiles:
    print("Invalid")
else:
    x = ((4*vechiles) - wheels)//2  # 130
    print("two whelleres = {0} four wheeler = {1}".format(x,vechiles-x))# two whelleres = 130 four wheeler = 170