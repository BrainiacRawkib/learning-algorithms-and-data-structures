from collections import deque


s = deque()

print(s)

new_queue = deque([1, 2, 'Name'])

print(new_queue)


if __name__ == '__main__':
    new_queue.append('age_right')
    print(new_queue)
    new_queue.appendleft('age_left')
    print(new_queue)
    print(new_queue.pop())
    print(new_queue.popleft())
