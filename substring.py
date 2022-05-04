def substring(s: str(), k: int) -> int:
    result = set()
    for i in range(len(s)):
        equal_in_seq = 0
        sequence = str()
        for j in range(i, len(s)):
            if s[i] == s[j] or s[j] == s[j-1]:
                sequence += s[i]
            elif equal_in_seq < (k-1):
                equal_in_seq += 1
                sequence += s[j]
            else:
                break
        result.add(sequence)
    num = list(result)
    return (len(max(num, key=len)))


if __name__ == '__main__':
    print(substring('aaaaa', 2))