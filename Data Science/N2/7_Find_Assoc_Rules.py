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


# Function from this exercise

def find_assoc_rules(receipts, threshold):
    pair_counts = defaultdict(int)
    item_counts = defaultdict(int)

    for i in receipts:
        update_pair_counts(pair_counts, i)
        update_item_counts(item_counts, i)
    rules = filter_rules_by_conf(pair_counts, item_counts, threshold)
    return rules


# `find_assoc_rules_test`: Test cell

receipts = [set('abbc'), set('ac'), set('a')]
rules = find_assoc_rules(receipts, 0.6)

print("Original receipts as itemsets:", receipts)
print("Resulting rules:")
print(print_rules(rules))


assert ('a', 'b') not in rules
assert ('b', 'a') in rules
assert ('a', 'c') in rules
assert ('c', 'a') in rules
assert ('b', 'c') in rules
assert ('c', 'b') not in rules

print("\n(Passed!)")
