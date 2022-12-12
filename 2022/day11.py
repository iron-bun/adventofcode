import operator
import functools

operators = {"+":operator.add, "*":operator.mul}

moduland = 1

class Operation:
    def __init__(self, operation):
        tmp = operation.split(" ")
        self.operand = [tmp[0], tmp[2]]
        self.operator = tmp[1]
    
    def apply(self, old):
        ans = 0
        
        if self.operand[0] == "old":
            ans += old
        else:
            ans += operators[self.operator](ans, int(self.operand[0]))
            
        if self.operand[1] == "old":
            ans = operators[self.operator](ans, ans)
        else:
            ans = operators[self.operator](ans, int(self.operand[1]))
        
        return ans
        
class Monkey:
    
    def __init__(self, id, items, operation, test, true_monkey, false_monkey, monkey_dict):
        self.id = id
        self.items = items
        self.operation = Operation(operation)
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.monkey_dict = monkey_dict
        self.inspections = 0
    
    def inspect(self, reducemethod):
        while len(self.items) > 0:
            self.inspections += 1
            item = self.items.pop()
            item = self.operation.apply(item)
            
            item = reducemethod(item)
            
            if item == 0:
                exit(1)
            if item % self.test == 0:
                self.monkey_dict[self.true_monkey].give(item)
            else:
                self.monkey_dict[self.false_monkey].give(item)
    
    def give(self, item):
        self.items.append(item)

def get_monkeys():
    monkeys = {}
    global moduland 
    moduland = 1
    
    with open("day11.txt") as f:
        line = f.readline().strip()
        while line:
            id = int(line.split(" ")[1][:-1])
            
            line = f.readline().strip()
            items = [int(v.strip(" ")) for v in line[16:].split(",")]
            
            line = f.readline().strip()
            operation = line[17:]
            
            line = f.readline().strip()
            test = int(line[19:])
            moduland *= test
            
            line = f.readline().strip()
            true_monkey = int(line[25:])
            
            line = f.readline().strip()
            false_monkey = int(line[26:])
            
            m = Monkey(id, items, operation, test, true_monkey, false_monkey, monkeys)
            monkeys[id] = m
            
            f.readline()
            line = f.readline().strip()
    return monkeys

def get_monkey_business(monkeys):
    
    ans = [0, 0]
    for m in monkeys:
            tmp = monkeys[m].inspections
            if tmp > ans[0]:
                ans[1] = ans[0]
                ans[0] = tmp
            elif tmp > ans[1]:
                ans[1] = tmp
                
    return (ans[0] * ans[1])
    
if __name__ == "__main__":
    monkeys = get_monkeys()
    for _ in range(20):
        for k in monkeys:
            monkeys[k].inspect(lambda x: x // 3)    
    print(get_monkey_business(monkeys))
   
    monkeys = get_monkeys()
    for i in range(10000):
            for k in monkeys:
                monkeys[k].inspect(lambda x: x % moduland)
    print(get_monkey_business(monkeys))
            