import math


def filter_rules_by_conf(pair_counts, item_counts, threshold):
    rules = {}  # (item_a, item_b) -> conf (item_a => item_b)
    for k, v in pair_counts.items():
        for i, j in item_counts.items():
            assert i in item_counts
            if k[0] == i in item_counts:
                if v/j >= threshold:
                    rules[k] = v/j
    return rules


# `filter_rules_by_conf_test`: Test cell
pair_counts = {('man', 'woman'): 5,
               ('bird', 'bee'): 3,
               ('red fish', 'blue fish'): 7}
item_counts = {'man': 7,
               'bird': 9,
               'red fish': 11}
rules = filter_rules_by_conf(pair_counts, item_counts, 0.5)
print("Found these rules:", rules)
assert ('man', 'woman') in rules
assert ('bird', 'bee') not in rules
assert ('red fish', 'blue fish') in rules
print("\n(Passed first test -- your code seems to find the right rules.)")

for a, b, c in [('man', 'woman', 0.7142857142857143), ('red fish', 'blue fish', 0.6363636363636364)]:
    assert math.isclose(rules[(a, b)], c, rel_tol=1e-3), \
        f"conf('{a}' => '{b}') should be about {c:.4f}, but you computed {rules[(a, b)]}."
print("\n(Passed second test -- your code also seems to get the right confidence values.)")
