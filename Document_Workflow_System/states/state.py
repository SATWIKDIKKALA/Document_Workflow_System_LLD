from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self,document):
        self.document = document

    @abstractmethod
    def edit(self,new_content):
        pass

    @abstractmethod
    def submit(self):
        pass
    
    @abstractmethod
    def approve(self):
        pass

    @abstractmethod
    def reject(self):
        pass