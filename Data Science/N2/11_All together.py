from collections import defaultdict
from collections import Counter
import itertools
import math


# Code snippet to import dataset 

def on_vocareum():
    import os
    return os.path.exists('.voc')


def download(file, local_dir="", url_base=None, checksum=None):
    import os
    import requests
    import hashlib
    import io
    local_file = "{}{}".format(local_dir, file)
    if not os.path.exists(local_file):
        if url_base is None:
            url_base = "https://cse6040.gatech.edu/datasets/"
        url = "{}{}".format(url_base, file)
        print("Downloading: {} ...".format(url))
        r = requests.get(url)
        with open(local_file, 'wb') as f:
            f.write(r.content)
    if checksum is not None:
        with io.open(local_file, 'rb') as f:
            body = f.read()
            body_checksum = hashlib.md5(body).hexdigest()
            assert body_checksum == checksum, \
                "Downloaded file '{}' has incorrect checksum: '{}' instead of '{}'".format(local_file,body_checksum,checksum)
    print("'{}' is ready!".format(file))


if on_vocareum():
    DATA_PATH = "./resource/asnlib/publicdata/"
else:
    DATA_PATH = ""
datasets = {'groceries.csv': '0a3d21c692be5c8ce55c93e59543dcbe'}

for filename, checksum in datasets.items():
    download(filename, local_dir=DATA_PATH, checksum=checksum)

with open('{}{}'.format(DATA_PATH, 'groceries.csv')) as fp:
    groceries_file = fp.read()
# Prints the first 250 characters only
print(groceries_file[0:250] + "...\n... (etc.) ...")
print("\n(All data appears to be ready.)")


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


def make_itemsets(words):
    return [set(w) for w in words]


def update_pair_counts2(pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type(pair_counts) is defaultdict

    for i in itemset:
        c = list(itertools.permutations(i, 2))
        for j in c:
            pair_counts[j] += 1

    return pair_counts


def update_item_counts2(item_counts, itemset, min_count):
    for i in itemset:
        for j in i:
            item_counts[j] += 1
    delete = {k: v for (k, v) in item_counts.items() if v < min_count}
    #print(delete)
    for k in delete.keys():
        del item_counts[k]
    #for k in delete.keys(): itemset.remove(k)
    assert [v for v in item_counts.values() if v >= min_count]
    #  print(item_counts)
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


data_cl = groceries_file.split("\n")
new_data_cl = []
for i in data_cl:
    x = i.split(",")
    new_data_cl.append(x)

test = new_data_cl
#print(test)

itemset = make_itemsets(test)
#print(itemset)

item_counts = defaultdict(int)
pair_counts = defaultdict(int)
update_item_counts2(item_counts, itemset, 10)
update_pair_counts2(pair_counts, itemset)
basket_rules = filter_rules_by_conf(pair_counts, item_counts, 0.5)

print_rules(basket_rules)

# Confidence threshold
THRESHOLD = 0.5

# Only consider rules for items appearing at least `MIN_COUNT` times.
MIN_COUNT = 10

### `basket_rules_test`: TEST CODE ###

print("Found {} rules whose confidence exceeds {}.".format(len(basket_rules), THRESHOLD))
print("Here they are:\n")
print_rules(basket_rules)

assert len(basket_rules) == 19
assert all([THRESHOLD <= v < 1.0 for v in basket_rules.values()])
ans_keys = [("pudding powder", "whole milk"),
            ("tidbits", "rolls/buns"),
            ("cocoa drinks", "whole milk"),
            ("cream", "sausage"),
            ("rubbing alcohol", "whole milk"),
            ("honey", "whole milk"),
            ("frozen fruits", "other vegetables"),
            ("cream", "other vegetables"),
            ("ready soups", "rolls/buns"),
            ("cooking chocolate","whole milk"),
            ("cereals", "whole milk"),
            ("rice", "whole milk"),
            ("specialty cheese", "other vegetables"),
            ("baking powder", "whole milk"),
            ("rubbing alcohol", "butter"),
            ("rubbing alcohol", "citrus fruit"),
            ("jam", "whole milk"),
            ("frozen fruits", "whipped/sour cream"),
            ("rice", "other vegetables")]

for k in ans_keys:
    assert k in basket_rules

print("\n(Passed!)")
