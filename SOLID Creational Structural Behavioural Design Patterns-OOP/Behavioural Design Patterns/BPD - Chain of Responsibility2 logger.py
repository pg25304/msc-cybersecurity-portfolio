#Handler
from abc import ABC, abstractmethod
class Logger(ABC):
    def __init__(self, successor = None):
        self.successor = successor #next logger in the chain

    @abstractmethod
    def handle(self, message, level):
        pass
    #pass to next handler
    def pass_to_next(self, message, level):
        if self.successor:
            return self.successor.handle(message, level)
        return None

#Concrete loggers
class InfoLogger(Logger):
    def handle(self, message, level):
        if level == "INFO":
            print(f"[INFO] {message}")
        else:
            return self.pass_to_next(message, level)

class ErrorLogger(Logger):
    def handle(self, message, level):
        if level == "ERROR":
            print(f"[ERROR] {message}")
        else:
            return self.pass_to_next(message, level)
class WarningLogger(Logger):
    def handle(self, message, level):
        if level == "WARNING":
            print(f"[WARNING] {message}")
        else:
            return self.pass_to_next(message, level)

#Example usage
if __name__ == "__main__":
    #create chain of loggers: Info -> Error ->Warning
    logger_chain = InfoLogger(ErrorLogger(WarningLogger()))
    #log messages at different levels
    logger_chain.handle("System started successfully.","INFO" )
    logger_chain.handle("Low disk space warning.","WARNING" )