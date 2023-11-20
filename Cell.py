class Cell:
    defaultCellValue = 1
    
    def __init__(self, n : int = defaultCellValue):
        self.__modifiable = True

        self.setCellValue(n)
        
    def getCellValue(self) -> int:
        return self.__val
    
    def setCellValue(self, n : int = defaultCellValue) -> int:
        if not self.__modifiable:
            raise Exception("Unable to modify cell value. Cell is locked.")
        if not type(n) == int:
            raise TypeError("A cell can only hold an int value")
        if n <= 0 or n > 9:
            raise ValueError("A cell's value can only be between 1 and 9.")
        self.__val = n
        return self.__val
    
    def lock(self):
        self.__modifiable = False
        
    def unlock(self):
        self.__modifiable = True
    def isLocked(self):
        return not self.__modifiable
    
    def __repr__(self):
        return str(self.getCellValue())
