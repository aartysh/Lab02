import random
from datetime import datetime

class TSensor:
    def tdata(self):
        self.data = random.randint(-30, 30)

class dataSave:
    def __init__(self, tem, time):
        self.tem = tem
        self.time = time

class loger:
    def __init__(self, numberOfData):
        self.numberOfData = numberOfData
        self.TSensor = TSensor()
        self.allData = []

    def collectData(self):
        for i in range(self.numberOfData):
            self.TSensor.tdata()
            temperature = self.TSensor.data
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.allData.append(dataSave(temperature, time))



    def DataToTxt(self, filename):
        with open(filename, 'w') as file:
            for entry in self.allData:
                file.write(f"{entry.time} - {entry.tem}C\n")

lg = loger(10)
lg.collectData()
lg.DataToTxt("data.txt")