import pandas as pd
import numpy as np
from io import StringIO
from IPython.display import display
from pandas.testing import assert_frame_equal
import re
from math import isnan


who_raw = pd.read_csv("N7_Tydying Data/who.csv")

print(
    "=== WHO TB data set: {} rows x {} columns ===".format(
        who_raw.shape[0], who_raw.shape[1]
    )
)
print("Column names:", who_raw.columns)

print("\n=== A few randomly selected rows ===")
import random


# CODE FROM PREVIOUS EXERCISES

row_sample = sorted(random.sample(range(len(who_raw)), 5))
display(who_raw.iloc[row_sample])


def canonicalize_tibble(X):
    # Enforce Property 1:
    var_names = sorted(X.columns)
    # print(var_names)
    # print(X[var_names])
    Y = X[var_names].copy()
    # print(Y)

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


def melt(df, col_vals, key, value):
    assert type(df) is pd.DataFrame
    keepVars = df.columns.difference(col_vals)
    melted_sec = []
    for c in col_vals:  # loop through the list given as an argument
        melted_c = df[keepVars].copy()
        # print(melted_c)
        melted_c[key] = c
        melted_c[value] = df[c]
        melted_sec.append(melted_c)
    # print(melted_sec)
    melted = pd.concat(melted_sec)
    return melted


# CODE FOR THIS EXERCISE


col_vals = who_raw.columns.difference(["country", "iso2", "iso3", "year"])
# print(col_vals)
who2 = melt(who_raw, col_vals, "case_type", "count")

del who2["iso2"]
del who2["iso3"]
# print(who2.head(), "\n")
who2 = who2[who2["count"].apply(lambda x: not isnan(x))]
# print(who2.head(10))
who2["count"] = who2["count"].apply(lambda x: int(x))
who2.to_csv(r"N7_Tydying Data/who2AS.csv", index=False)

# Test: `who2_test`

print("=== First few rows of your solution ===")
display(who2.head())

print("=== First few rows of the instructor's solution ===")
who2_soln = pd.read_csv("N7_Tydying Data/who2_soln.csv")
display(who2_soln.head())

# Check it
assert tibbles_are_equivalent(who2, who2_soln)
print("\n(Passed.)")
