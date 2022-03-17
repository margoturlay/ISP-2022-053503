import re
import os

path = 'text.txt'


def is_empty() -> bool:
    return os.path.getsize(path) == 0

def read_file(path: str) -> str:
    if is_empty():
        raise EOFError("File is empty.")
    else:
        with open(path) as open_file:
            s = open_file.read()
    return s

def check_variables(N: int, K: int):
    if N == 0 or K == 0:
        raise ValueError("Incorrect input")

def frequency_list(s: str) -> list:
    cnt = {}
    for i in re.sub('[^\w\s]', ' ', s.lower().replace('\n', ' ')).split(' '):
        if len(i) > 0:
            cnt.setdefault(i, 0)
            cnt[i] += 1
    return sorted(cnt.items(), key=lambda item: item[1])

def words_counts(s: str) -> list:
    cnt = []
    for p in re.sub('[!?]', '.', s).split('.'):
        words = 0
        for i in p.split(' '):
            if len(i) > 0:
                words += 1
        if words > 0:
            cnt += [words]
    return cnt

def average(cnt: list) -> int:
    return sum(cnt) / len(cnt)

def median(cnt: list) -> int:
    cnt = sorted(cnt)
    return (cnt[len(cnt) // 2] + cnt[(len(cnt) - 1) // 2]) / 2

def Ngramms(s: str, K: int) -> str:
    cnt = {}
    s = re.sub('[^a-z]', '', s.lower())
    for i in range(len(s) - K + 1):
        subs = s[i:i + K]
        cnt.setdefault(subs, 0)
        cnt[subs] += 1
    return sorted(cnt.items(), key=lambda item: item[1], reverse=True)
