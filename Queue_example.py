from collections import deque
bank = deque(['A', 'X', 'Y'])
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
if not bank:
    print('No person left')