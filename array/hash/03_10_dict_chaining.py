dict = {"fast" : "Quic" }

# put(key,value) -> dic에 key 에 해당하는 곳에 value 를 저장한다
# get(key) -> dictionary 에 key 해당한는 value를 반환해라

# 체이닝, 개방 주소법을 통해 해시를 일반 구조에서 넣었을때의 충돌 문제를 해결할 수 있다.
# 충돌 : 같은 배열의 인덱스로 매핑되어서 데이터를 덮어써버리는 결과
# 체이닝 : 내부구조를 링크드리스트로 변경해서 들어오는 데이터를 연결하는 방법
# 개방 주소법 : 해시값을 나누어 찾은 인덱스값으로 배열에 저장시키려했으나 꽉찬경우 다음 주소에 저장시키는 방법
class LinkedTuple:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def add(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].append((key,value)) # ["333",7] -> ["77" ,6]

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

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

linked_tuple = LinkedTuple()
linked_tuple.add("test", 4)
linked_tuple.add("test2", 5)
print(linked_tuple.items)
print(linked_tuple.get("test"))
print(linked_tuple.get("test2"))