# 27.9.13
# Per Starke
# works

class Binary(object):                       # defines the class binary

    def __init__(self, teiler_, zahl_):     # defines the _init_ which is needed for classes
        self.Zahl_ = zahl_
        self.Teiler_ = teiler_
        
    def ausrechnen(self):                   # defines the function which gives you the
        teiler = self.Teiler_               # number in the wished system back
        zahl = self.Zahl_                   # and here's the number
        bina = ""                           # and the empty bina (look in binary.py for
                                            # more information
        while zahl > 0:                             
            bina = str(zahl%teiler) + str(bina)
            zahl = int(zahl/teiler)
        return(bina)
        

        


