#Acts as a placeholder for a value between 1 and 9.
#Also stores a value which locks the int value.
class Cell:
    defaultCellValue = 1

    #Creates a modifiable cell
    def __init__(self, n : int = defaultCellValue):
        self.__modifiable = True

        self.setCellValue(n)
    #Returns the current cell value.     
    def getCellValue(self) -> int:
        return self.__val
    
    #Attempts to set the cell value.
    #NOTE: Raises an exception if the value is not between 1 and 9, or if the cell is lockd.
    def setCellValue(self, n : int = defaultCellValue) -> int:
        if not self.__modifiable:
            raise Exception("Unable to modify cell value. Cell is locked.")
        if not type(n) == int:
            raise TypeError("A cell can only hold an int value")
        if n <= 0 or n > 9:
            raise ValueError("A cell's value can only be between 1 and 9.")
        
        self.__val = n
        return self.__val
    #Locks the current cell, preventing changes to be made to the cell value.
    def lock(self):
        self.__modifiable = False
    
    #Unlocks the current cell, allowing changes to be made to the cell value.    
    def unlock(self):
        self.__modifiable = True
    
    #Determines if the cell is currently locked
    def isLocked(self):
        return not self.__modifiable
    #Acts sorta like a toString method, but with some intricacies
    #I believe this method is solely for debugging purposes 
    def __repr__(self):
        return str(self.getCellValue())
