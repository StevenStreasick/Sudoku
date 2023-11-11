class Cell:
    defaultCellValue = 1
    
    def __init__(self, n : int = defaultCellValue):
        self.setCellValue(n)
        
    def getCellValue(self) -> int:
        return self.__val
    
    def setCellValue(self, n : int = defaultCellValue) -> int:
        if not type(n) == int:
            raise TypeError("A cell can only hold an int value")
        if n <= 0 or n > 9:
            raise ValueError("A cell's value can only be between 1 and 9.")
        self.__val = n
        return self.__val
    
    def __repr__(self):
        return str(self.getCellValue())
