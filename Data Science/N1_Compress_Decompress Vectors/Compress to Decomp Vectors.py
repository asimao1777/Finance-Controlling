# Create a Vector from a Dict (Compressed Vectors) containing a list of indexes and a list of values

# Decompress vector function


def decompress_vector(d, n=None):
    i_max = max(d["inds"]) if d["inds"] else -1
    if n == None:
        n = i_max + 1
    else:
        assert n > i_max, "Bad value for full vector length"

    final = [float(0)] * n
    # print(final)

    for a, b in zip(d["inds"], d["vals"]):
        final[a] += b

    return final


# Tests to check if function works

# `decompress_vector_test`: Test cell
def check_decompress_vector(d_orig, x_true):
    print("Testing `decompress_vector(d, n)`:")
    print("\tx_true: {}".format(x_true))
    print("\td: {}".format(d_orig))
    d = d_orig.copy()
    n_true = len(x_true)
    if d["inds"] and max(d["inds"]) + 1 == n_true:
        n = None
    else:
        n = n_true
    print("\tn: {}".format(n))
    x = decompress_vector(d, n)
    print("\t=> x[:{}]: {}".format(len(x), x))
    assert type(x) is list and len(x) == n_true, "Output vector has the wrong length."
    assert all(
        [abs(x_i - x_true_i) < n_true * 1e-15 for x_i, x_true_i in zip(x, x_true)]
    )
    assert d == d_orig


# Test 1: Example
d = {}
d["inds"] = [0, 3, 7, 3, 3, 5, 1]
d["vals"] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
x_true = [1.0, 7.0, 0.0, 11.0, 0.0, 6.0, 0.0, 3.0]
check_decompress_vector(d, x_true)

# Test 2: Random vectors
def gen_cvec_reps(p_nz, n_max):
    from random import random, randrange, sample

    x_true = [0.0] * n_max
    d = {"inds": [], "vals": []}
    for i in range(n_max):
        if random() <= p_nz:  # Create non-zero
            n_rep = randrange(1, 5)
            d["inds"].extend([i] * n_rep)
            v_i = [float("{:.2f}".format(random())) for _ in range(n_rep)]
            d["vals"].extend(v_i)
            x_true[i] = sum(v_i)
    perm = sample(range(len(d["inds"])), k=len(d["inds"]))
    d["inds"] = [d["inds"][k] for k in perm]
    d["vals"] = [d["vals"][k] for k in perm]
    return (d, x_true)


p_nz = 0.2  # probability of a non-zero
n_max = 10  # maximum full-vector length
for _ in range(5):  # 5 trials
    print("")
    (d, x_true) = gen_cvec_reps(p_nz, n_max)
    check_decompress_vector(d, x_true)

# Test 3: Empty vector of length 5
print("")
check_decompress_vector({"inds": [], "vals": []}, [0.0] * 5)

print("\n(Passed!)")
