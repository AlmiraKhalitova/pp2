def power_of_two(word_len):
    pwr = 0
    while pwr <= 100:
        if 2 ** pwr == word_len:
            return True
        pwr += 1
    return False

n = int(input())
ch_s = "!@#$%^&*()_+~`'<>/?.,/:;’1234567890"
while n > 0:
    v = list(map(str, input().split()))
    new_v = []
    for word in v:
        x = ''
        for ch in word:
            if ch not in ch_s:
                x += ch
        new_v.append(x)
    for word in new_v:
        if power_of_two(len(word)):
            print('H', end=' ')
        else:
            print('C', end=' ')
    print()
    n -= 1