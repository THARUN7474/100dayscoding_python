import os
n = int(input())
sequences = []
for _ in range(n):
    m, *values = input().split()
    sequences.append(set(values))

p = int(input())
for _ in range(p):
    old_password, new_password = input().split()
    found = False
    for seq in sequences:
        common_prefix = os.path.commonprefix([old_password, new_password])
        common_suffix = os.path.commonprefix([old_password[::-1], new_password[::-1]])[::-1]
        if common_prefix in seq and common_suffix in seq and len(common_prefix) + len(common_suffix) <= len(old_password):
            found = True
            break
    if found:
        print("REJECT")
    else:
        print("OK")
