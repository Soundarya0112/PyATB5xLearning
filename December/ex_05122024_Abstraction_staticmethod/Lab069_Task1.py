from abc import ABC,abstractmethod
class PC:
    def pc_init(self):
        print("pc intialized")
class Motherboard():
    def start(self):
        print("motherboard started")
class RAM(ABC):
    @abstractmethod
    def start_ram(self):
        pass
class Processor(ABC):
    @abstractmethod
    def start_processor(self):
        pass
class Storage(ABC):
    @abstractmethod
    def store_data(self):
        pass
    @staticmethod
    def loadOs():
        print("loading os")
    def startMouse(self):
        print("start mouse")
    def UseHeadPhone(self):
        print("use headphone")

#subclass for abstract class RAM
class SubRam(RAM):
    def start_ram(self):
      print("start RAM")
#subclass for abstract Processor
class SubProcessor(Processor):
    def start_processor(self):
       print("start Processor")
#subclass for abstract Storage
class SubStorage(Storage):
    def store_data(self):
       print("start storing data")
Storage.loadOs()  #calling static method without oj=bject creation-- storage
pc_obj=PC()
pc_obj.pc_init()
mother_obj=Motherboard()
mother_obj.start()
ram_obj=SubRam()
ram_obj.start_ram()
processor_obj=SubProcessor()
processor_obj.start_processor()
storage_obj=SubStorage()
storage_obj.store_data()
storage_obj.startMouse()
storage_obj.UseHeadPhone()
