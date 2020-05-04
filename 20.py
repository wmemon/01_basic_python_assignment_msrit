from collections import defaultdict


def get_day(num):
    num = int ( num )
    d = defaultdict ( lambda: "[!]Enter a value between 0 and 6 (both included)",
                      {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
                       6: 'Saturday'}
                      )
    return d[num]

print(get_day(3))
print(get_day(99))