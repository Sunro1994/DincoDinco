class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 1. 원소를 맨 뒤 에 추가
        self.items.append(value)
        # 2. 해당 원소의 인덱스가 루트 노드일때까지 (현재 노드의 인덱스가 1이라면 멈춤)
        cur_index = len(self.items) - 1

        while cur_index != 1: # 부모노드와 비교해서 내가 더 크다면 위치를 바꾼다.
            parent_idx = cur_index // 2

            if self.items[parent_idx] < self.items[cur_index]:
                self.items[parent_idx], self.items[cur_index] = self.items[cur_index], self.items[parent_idx]
                cur_index = parent_idx
            else:
                break

        return self.items


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!