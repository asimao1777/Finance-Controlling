from collections import defaultdict
from collections import Counter
import itertools
import math

english_text = """
But I must explain to you how all this mistaken idea
of denouncing of a pleasure and praising pain was
born and I will give you a complete account of the
system, and expound the actual teachings of the great
explorer of the truth, the master-builder of human
happiness. No one rejects, dislikes, or avoids
pleasure itself, because it is pleasure, but because
those who do not know how to pursue pleasure
rationally encounter consequences that are extremely
painful. Nor again is there anyone who loves or
pursues or desires to obtain pain of itself, because
it is pain, but occasionally circumstances occur in
which toil and pain can procure him some great
pleasure. To take a trivial example, which of us
ever undertakes laborious physical exercise, except
to obtain some advantage from it? But who has any
right to find fault with a man who chooses to enjoy
a pleasure that has no annoying consequences, or
one who avoids a pain that produces no resultant
pleasure?

On the other hand, we denounce with righteous
indignation and dislike men who are so beguiled and
demoralized by the charms of pleasure of the moment,
so blinded by desire, that they cannot foresee the
pain and trouble that are bound to ensue; and equal
blame belongs to those who fail in their duty
through weakness of will, which is the same as
saying through shrinking from toil and pain. These
cases are perfectly simple and easy to distinguish.
In a free hour, when our power of choice is
untrammeled and when nothing prevents our being
able to do what we like best, every pleasure is to
be welcomed and every pain avoided. But in certain
circumstances and owing to the claims of duty or
the obligations of business it will frequently
occur that pleasures have to be repudiated and
annoyances accepted. The wise man therefore always
holds in these matters to this principle of
selection: he rejects pleasures to secure other
greater pleasures, or else he endures pains to
avoid worse pains.
"""

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

# Functions from previous exercises


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


def get_normalized_words(s):
    sl = s.lower()
    nl = ''.join([i for i in sl if i.isalpha() or i.isspace()])
    nl2 = nl.replace("\n", " ")
    nl3 = nl2.split(" ")
    nl4 = [i for i in nl3 if i != ""]

    return nl4


def make_itemsets(words):
    return [set(w) for w in words]


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


def intersect_keys(d1, d2):
    assert type(d1) is dict or type(d1) is defaultdict
    assert type(d2) is dict or type(d2) is defaultdict

    intersection = {}
    for k, v in d1.items():
        if k in d2.keys():
            intersection[k] = v

    return intersection


# Function from this exercise


def get_high_conf_rules(string1, string2, threshold):

    final_list = []

    normwords1 = get_normalized_words(string1)
    # print(normwords1)
    itemset1 = make_itemsets(normwords1)
    # print(itemset1)
    rules1 = find_assoc_rules(itemset1, threshold)
    # print(print_rules(rules1))

    normwords2 = get_normalized_words(string2)
    # print(normwords2)
    itemset2 = make_itemsets(normwords1)
    # print(itemset2)
    rules2 = find_assoc_rules(itemset1, threshold)
    # print(print_rules(rules2))

    high_conf_rules = (intersect_keys(rules1, rules2))
    just_values = high_conf_rules.values()
    max_key = max(just_values)
    # print(max_key)

    for k, v in high_conf_rules.items():
        if v == max_key:
            final_list.append(k)

    # print(final_list)

    return final_list


threshold = 0.75
common_high_conf_rules = (get_high_conf_rules(
    latin_text, english_text, threshold))

print_rules(common_high_conf_rules)

# `common_high_conf_rules_test`: Test cell

assert len(common_high_conf_rules) == 2
assert ('x', 'e') in common_high_conf_rules
assert ('q', 'u') in common_high_conf_rules
print("\n(Passed!)")
