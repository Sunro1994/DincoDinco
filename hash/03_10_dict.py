dict = {"fast" : "Quic" }

# put(key,value) -> dic에 key 에 해당하는 곳에 value 를 저장한다
# get(key) -> dictionary 에 key 해당한는 value를 반환해라

class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value


    def get(self, key):
        index = hash(key) %len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))