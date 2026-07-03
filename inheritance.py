class users:
    def __init__(self, name , age , id):
        self.name = name
        self.id = id
        self.age = age
    
class worker(users):
    def __init__(self,name,age,id, salary):
        super().__init__(name,age,id)
        self.salary = salary

class costumer(users):
    def __init__(self,name,age,id):
        super().__init__(name,age,id)

james = costumer("james" , 25 , 1)
ray = worker("ray",18,2, 2555)

print(isinstance(ray,costumer))
