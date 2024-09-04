import pandas as pd
import numpy as np
from io import StringIO
from IPython.display import display
from pandas.testing import assert_frame_equal
import re
from math import isnan


who2 = pd.read_csv("N7_Tydying Data/who2AS.csv")
display(who2.head(5))


# CODE FROM PREVIOUS EXERCISES
def canonicalize_tibble(X):
    # Enforce Property 1:
    var_names = sorted(X.columns)
    # print(var_names, type(var_names))
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

    # print(AA.equals(BB))
    return AA.equals(BB)


def default_splitter(text):
    fields = re.findall("(\d+\.?\d+)", text)
    return fields


import re


def who_splitter(text):
    m = re.match(r"^new_?(rel|ep|sn|sp)_(f|m)(\d{2,4})$", text)
    if m is None or len(m.groups()) != 3:
        return ["", "", ""]

    fields = list(m.groups())
    print(fields, "\n")

    # rename fields after splitting them

    if fields[1] == "f":
        fields[1] = "female"
    elif fields[1] == "m":
        fields[1] = "male"

    if fields[2] == "014":
        fields[2] = "0-14"
    elif fields[2] == "65":
        fields[2] = "65+"
    elif len(fields[2]) == 4 and fields[2].isdigit():
        fields[2] = fields[2][0:2] + "-" + fields[2][2:4]

    return fields


def separate(df, key, into, splitter=default_splitter):
    assert type(df) is pd.DataFrame
    assert key in df.columns

    def apply_splitter(text):
        fields = splitter(text)
        # print(fields)
        new_fields = pd.Series({into[i]: f for i, f in enumerate(fields)})
        # print(new_fields)
        return new_fields

    fixed_vars = df.columns.difference([key])
    # print(fixed_vars)
    tibble = df[fixed_vars].copy()
    tibble_extra = df[key].apply(apply_splitter)
    # print(tibble_extra)
    tibble = pd.concat([tibble_extra, tibble], axis=1)

    return tibble


who3 = separate(who2, "case_type", ["type", "gender", "age_group"], who_splitter)
who3.to_csv("N7_Tydying Data/who3AS.csv")

# display(who3.head(10))

# Test: `who3_test`

print("=== First few rows of your solution ===")
display(who3.head())

who3_soln = pd.read_csv("N7_Tydying Data/who3_soln.csv")
print("\n=== First few rows of the instructor's solution ===")
display(who3_soln.head())

assert tibbles_are_equivalent(who3, who3_soln)
print("\n(Passed.)")
