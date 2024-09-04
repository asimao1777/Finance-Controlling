import pandas as pd
import numpy as np
from io import StringIO
from IPython.display import display
from pandas.testing import assert_frame_equal

# CODE FROM PREVIOUS EXERCISES


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


# CODE FOR THIS EXERCISE


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


# Test: `melt_test`

table4a = pd.read_csv("N7_Tydying Data/table4a.csv")
print("\n=== table4a ===")
display(table4a)

m_4a = melt(table4a, col_vals=["1999", "2000"], key="year", value="cases")
print("=== melt(table4a) ===")
display(m_4a)

table4b = pd.read_csv("N7_Tydying Data/table4b.csv")
print("\n=== table4b ===")
display(table4b)

m_4b = melt(table4b, col_vals=["1999", "2000"], key="year", value="population")
print("=== melt(table4b) ===")
display(m_4b)

m_4 = pd.merge(m_4a, m_4b, on=["country", "year"])
print("\n=== inner-join(melt(table4a), melt (table4b)) ===")
display(m_4)

m_4["year"] = m_4["year"].apply(int)

table1 = pd.read_csv("N7_Tydying Data/table1.csv")
print("=== table1 (target solution) ===")
display(table1)
assert tibbles_are_equivalent(table1, m_4)
print("\n(Passed.)")
