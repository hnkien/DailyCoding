class Queue:
    def __init__(self):
        self.list = []

    def add(self,item):
        if item:
            self.list.append(item)

    def pop(self):
        if len(self.list) == 0: return None
        last_item = self.list[0]
        del(self.list[0])
        return last_item

    def is_empty(self):
        return len(self.list) == 0