#Example of Facade Design Pattern in Python
class CPU:
    def run(self):
        return "CPU is running"

class RAM:
    def load(selfself):
        return "RAM is loading data"

class HDD:
    def read(self):
        return "HDD is reading data"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.hdd = HDD()

    def start_computer(self):
        results = []
        results.append(self.cpu.run())
        results.append(self.ram.load())
        results.append(self.hdd.read())
        return results
if __name__ == "__main__":
    computer = ComputerFacade()
    boot_processes = computer.start_computer()
    print(boot_processes)