from abc import ABC, abstractmethod


class BacklogMapNumberRepository(ABC):
    @abstractmethod
    def create(self, backlog, status):
        pass

    @abstractmethod
    def modify(self, backlog, domain):
        pass