from collections import defaultdict
import itertools  # Hint!

# My solution


def update_pair_counts(pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type(pair_counts) is defaultdict

    c = list(itertools.permutations(itemset, 2))
    #pair_counts = defaultdict(int)
    for i in c:
        pair_counts[i] += 1

    return pair_counts

# GA Tech solution


def update_pair_counts(pair_counts2, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type(pair_counts2) is defaultdict

    for a, b in itertools.combinations(itemset, 2):
        pair_counts2[(a, b)] += 1
        pair_counts2[(b, a)] += 1

    return pair_counts2


# `update_pair_counts_test`: Test cell

itemset_1 = set("error")
itemset_2 = set("dolor")

pair_counts = defaultdict(int)
pair_counts2 = defaultdict(int)

print(update_pair_counts(pair_counts, itemset_1))

assert len(pair_counts) == 6
print(update_pair_counts(pair_counts, itemset_2))
assert len(pair_counts) == 16

print('"{}" + "{}"\n==> {}'.format(itemset_1, itemset_2, pair_counts))
for a, b in pair_counts:
    assert (b, a) in pair_counts
    assert pair_counts[(a, b)] == pair_counts[(b, a)]

print("\n(Passed!)")

print(update_pair_counts(pair_counts2, itemset_1))

assert len(pair_counts2) == 6
print(update_pair_counts(pair_counts2, itemset_2))
assert len(pair_counts2) == 16

print('"{}" + "{}"\n==> {}'.format(itemset_1, itemset_2, pair_counts2))
for a, b in pair_counts2:
    assert (b, a) in pair_counts2
    assert pair_counts2[(a, b)] == pair_counts2[(b, a)]

print("\n(Passed!)")
