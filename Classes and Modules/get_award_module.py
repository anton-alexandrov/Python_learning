#finction with unknown number of input parameters
def award (award, *names):
    for name in names:
        print (name.title()+" got the "+award + " award! Congrats!")

