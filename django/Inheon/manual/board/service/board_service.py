from abc import ABC, abstractmethod


class BoardService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createBoard(self, boardData):
        pass

    @abstractmethod
    def readBoard(self, boardId):
        pass

    @abstractmethod
    def deleteBoard(self, boardId):
        pass