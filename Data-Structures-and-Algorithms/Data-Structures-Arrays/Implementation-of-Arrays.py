class MyArray:
  def __init__(self):
    self.length =0
    self.data ={}

  def __str__(self):
    return str(self.__dict__)

  def get(self, index):
    return self.data[index]

  def push(self, item):
    self.data[self.length]=item
    self.length+=1

  def pop(self):
    lastitem = self.data[self.length-1]
    del self.data[self.length-1]
    self.length = self.length-1
    return lastitem

  def delete(self,index):
    deleteditem = self.data[index]
    for i in range(index,self.length-1):
      self.data[i]=self.data[i+1]

    del self.data[self.length-1]
    self.length = self.length-1
    
    return deleteditem
    

newArray = MyArray()
newArray.push(3)
newArray.push('hi')
newArray.push(34)
newArray.push(20)
newArray.push('hey')
newArray.delete(3)
print(newArray)
  
  
