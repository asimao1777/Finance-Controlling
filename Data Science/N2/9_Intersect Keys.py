from random import sample
from collections import defaultdict
import itertools
import math


# Funtions from previous exercises


def gen_rule_str(a, b, val=None, val_fmt='{:.3f}', sep=" = "):
    text = "{} => {}".format(a, b)
    if val:
        text = "conf(" + text + ")"
        text += sep + val_fmt.format(val)
    return text


def print_rules(rules):
    if type(rules) is dict or type(rules) is defaultdict:
        from operator import itemgetter
        ordered_rules = sorted(rules.items(), key=itemgetter(1), reverse=True)
    else:  # Assume rules is iterable
        ordered_rules = [((a, b), None) for a, b in rules]
    for (a, b), conf_ab in ordered_rules:
        print(gen_rule_str(a, b, conf_ab))


def update_pair_counts(pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type(pair_counts) is defaultdict

    c = list(itertools.permutations(itemset, 2))
    for i in c:
        pair_counts[i] += 1

    return pair_counts


def update_item_counts(item_counts, itemset):
    for i in itemset:
        item_counts[i] += 1

    return item_counts


def filter_rules_by_conf(pair_counts, item_counts, threshold):
    rules = {}  # (item_a, item_b) -> conf (item_a => item_b)
    for k, v in pair_counts.items():
        for i, j in item_counts.items():
            if k[0] == i in item_counts:
                assert i in item_counts
                if v/j >= threshold:
                    rules[k] = v/j
    return rules


def find_assoc_rules(receipts, threshold):
    pair_counts = defaultdict(int)
    item_counts = defaultdict(int)

    for i in receipts:
        update_pair_counts(pair_counts, i)
        update_item_counts(item_counts, i)
    rules = filter_rules_by_conf(pair_counts, item_counts, threshold)
    return rules


def get_normalized_words(s):
    sl = s.lower()
    nl = ''.join([i for i in sl if i.isalpha() or i.isspace()])
    nl2 = nl.replace("\n", " ")
    nl3 = nl2.split(" ")
    nl4 = [i for i in nl3 if i != ""]

    return nl4


def make_itemsets(words):
    return [set(w) for w in words]


# Function from this exercise


def intersect_keys(d1, d2):
    assert type(d1) is dict or type(d1) is defaultdict
    assert type(d2) is dict or type(d2) is defaultdict

    intersection = []
    for k, v in d1.items():
        if k in d2.keys():
            intersection.append(k)

    return intersection

#  `intersect_keys_test`: Test cell


key_space = {'ape', 'baboon', 'bonobo',
             'chimp', 'gorilla', 'monkey', 'orangutan'}
val_space = range(100)

for trial in range(10):  # Try 10 random tests
    d1 = {k: v for k, v in zip(sample(key_space, 4), sample(val_space, 4))}
    d2 = {k: v for k, v in zip(sample(key_space, 3), sample(val_space, 3))}
    k_common = intersect_keys(d1, d2)
    for k in key_space:
        is_common = (k in k_common) and (k in d1) and (k in d2)
        is_not_common = (k not in k_common) and (
            (k not in d1) or (k not in d2))
        assert is_common or is_not_common

print("\n(Passed!)")
