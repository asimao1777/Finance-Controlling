from collections import defaultdict


def update_item_counts(item_counts, itemset):
    for i in itemset:
        item_counts[i] += 1

    return item_counts


# `update_item_counts_test`: Test cell
itemset_1 = set("error")
itemset_2 = set("dolor")

item_counts = defaultdict(int)
print(update_item_counts(item_counts, itemset_1))
assert len(item_counts) == 3
print(update_item_counts(item_counts, itemset_2))
assert len(item_counts) == 5

assert item_counts['d'] == 1
assert item_counts['e'] == 1
assert item_counts['l'] == 1
assert item_counts['o'] == 2
assert item_counts['r'] == 2

print("\n(Passed!)")
