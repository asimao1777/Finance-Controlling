import pandas as pd
import numpy as np
from io import StringIO
from IPython.display import display
from pandas.util.testing import assert_frame_equal


def canonicalize_tibble(X):
    # Enforce Property 1:
    var_names = sorted(X.columns)
    print(var_names, type(var_names))
    Y = X[var_names].copy()
    print(Y)

    # Enforce Property 2 & 3:
    Y.sort_values(by=var_names, inplace=True)
    Y.set_index([list(range(0, len(Y)))], inplace=True)

    return Y


def tibbles_are_equivalent(A, B):
    """Given two tidy tables ('tibbles'), returns True iff they are
    equivalent.
    """
    # A_var_names = sorted(A.columns)
    # AA = A[A_var_names].copy()  # COLUMN ORDER
    # AA.sort_values(by=A_var_names, inplace=True)  # VALUE ORDER

    # B_var_names = sorted(B.columns)
    # BB = B[B_var_names].copy()
    # BB.sort_values(by=B_var_names, inplace=True)
    AA = canonicalize_tibble(A)
    BB = canonicalize_tibble(B)

    print(AA.equals(BB))
    return AA.equals(BB)


# Test: `tibble_are_equivalent_test`

A = pd.DataFrame(
    columns=["a", "b", "c"],
    data=list(zip(["x", "y", "z", "w"], [1, 2, 3, 4], ["hat", "cat", "bat", "rat"])),
)
print("=== Tibble A ===")
display(A)

# Permute rows and columns, preserving equivalence
import random

obs_ind_orig = list(range(A.shape[0]))
var_names = list(A.columns)

obs_ind = obs_ind_orig.copy()
while obs_ind == obs_ind_orig:
    random.shuffle(obs_ind)

while var_names == list(A.columns):
    random.shuffle(var_names)

B = A[var_names].copy()
B = B.iloc[obs_ind]

print("=== Tibble B == A ===")
display(B)

print("=== Tibble C != A ===")
C = A.copy()
C.columns = var_names
display(C)

assert tibbles_are_equivalent(A, B)
assert not tibbles_are_equivalent(A, C)
assert not tibbles_are_equivalent(B, C)

print("\n(Passed.)")
