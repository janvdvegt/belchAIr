class Test:
    def __init__(self, my_list=list()):
        self.my_list = my_list

    def add_item(self, item):
        self.my_list.append(item)

test1 = Test()
test1.add_item(3)
test2 = Test()
test2.add_item(4)
print(test2.my_list)