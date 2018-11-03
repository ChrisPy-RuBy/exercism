import cPickle as pickle

"""
This is very slow. Could spend it up 
"""

class Robot(object):

    def __init__(self):
            self.name = self.getName()


    def getName(self):
        
        try:     
            with open('./allcodes', 'rb') as fp:
                codes = pickle.load(fp)
                name = codes.pop()
        except Exception:
            self.generateNameList()
            self.getName()

        with open('./allcodes', 'wb') as fp:
            pickle.dump(codes, fp)
        return name
    

    def reset(self):

        newName = self.getName()
        self.name = newName


    @staticmethod
    def generateNameList():

        allcodes = []        
        alphabet = [chr(letter).upper() for letter in range(97, 123)]
        for letter in alphabet:       
            codestr = letter
            for letter in alphabet:
                secondletter = codestr
                secondletter += letter
                for x in range(0, 10):
                    thirdletter = secondletter
                    thirdletter += str(x)     
                    for x in range(0, 10):
                        forthletter = thirdletter
                        forthletter += str(x)    
                        for x in range(0,10):
                            fifthletter = forthletter
                            fifthletter += str(x)    
                            (fifthletter)
        try:
            import cPickle as pickle
            with open('./allcodes', 'wb') as fb:
                pickle.dump(set(allcodes), fb)
        except Exception as err:
            raise(err)

