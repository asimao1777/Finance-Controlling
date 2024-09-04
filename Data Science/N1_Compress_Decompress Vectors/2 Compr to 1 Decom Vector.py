# 2 Compressed Vectors into 1 Decompressed Vector

d1 = {'inds': [9, 9, 1, 9, 8, 1], 'vals': [
    0.28, 0.84, 0.71, 0.03, 0.04, 0.75]}
d2 = {'inds': [0, 9, 9, 1, 3, 3, 9], 'vals': [
    0.26, 0.06, 0.46, 0.58, 0.42, 0.21, 0.53, 0.76]}


def find_common_indexes(d1, d2):
    new = []
    for i in d1['inds'] and d2['inds']:
        if i in d1['inds'] and d2['inds']:
            if i not in new:
                new.append(i)
    return new


a = find_common_indexes(d1, d2)

print(a)
