from collections import defaultdict
import itertools
import math


# Latin Text

latin_text = """
Sed ut perspiciatis, unde omnis iste natus error sit
voluptatem accusantium doloremque laudantium, totam
rem aperiam eaque ipsa, quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta
sunt, explicabo. Nemo enim ipsam voluptatem, quia
voluptas sit, aspernatur aut odit aut fugit, sed
quia consequuntur magni dolores eos, qui ratione
voluptatem sequi nesciunt, neque porro quisquam est,
qui dolorem ipsum, quia dolor sit amet consectetur
adipisci[ng] velit, sed quia non numquam [do] eius
modi tempora inci[di]dunt, ut labore et dolore
magnam aliquam quaerat voluptatem. Ut enim ad minima
veniam, quis nostrum exercitationem ullam corporis
suscipit laboriosam, nisi ut aliquid ex ea commodi
consequatur? Quis autem vel eum iure reprehenderit,
qui in ea voluptate velit esse, quam nihil molestiae
consequatur, vel illum, qui dolorem eum fugiat, quo
voluptas nulla pariatur?

At vero eos et accusamus et iusto odio dignissimos
ducimus, qui blanditiis praesentium voluptatum
deleniti atque corrupti, quos dolores et quas
molestias excepturi sint, obcaecati cupiditate non
provident, similique sunt in culpa, qui officia
deserunt mollitia animi, id est laborum et dolorum
fuga. Et harum quidem rerum facilis est et expedita
distinctio. Nam libero tempore, cum soluta nobis est
eligendi optio, cumque nihil impedit, quo minus id,
quod maxime placeat, facere possimus, omnis voluptas
assumenda est, omnis dolor repellendus. Temporibus
autem quibusdam et aut officiis debitis aut rerum
necessitatibus saepe eveniet, ut et voluptates
repudiandae sint et molestiae non recusandae. Itaque
earum rerum hic tenetur a sapiente delectus, ut aut
reiciendis voluptatibus maiores alias consequatur
aut perferendis doloribus asperiores repellat.
"""

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


y = get_normalized_words(latin_text)
print(y)
x = make_itemsets(y)
print(x)
threshold = 0.75
latin_rules = find_assoc_rules(x, threshold)
print_rules(latin_rules)


# `latin_rules_test`: Test cell

assert len(latin_rules) == 10
assert all([0.75 <= v <= 1.0 for v in latin_rules.values()])
for ab in ['xe', 'qu', 'hi', 'xi', 'vt', 're', 've', 'fi', 'gi', 'bi']:
    assert (ab[0], ab[1]) in latin_rules
print("\n(Passed!)")
