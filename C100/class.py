class Car (object):
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.mode = model

    def start(self) :
        print('started')
    
    def stop(self) :
        print('stoped')
    
    def accelerate(self) :
        print('accelarting...')

audi = Car('A6','red','audi',80)

audi.start()