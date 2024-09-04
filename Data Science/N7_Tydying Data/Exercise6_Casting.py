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


def cast(df, key, value, join_how="outer"):
    """Casts the input data frame into a tibble,
    given the key column and value column.
    """
    assert type(df) is pd.DataFrame
    assert key in df.columns and value in df.columns
    assert join_how in ["outer", "inner"]

    fixed_vars = df.columns.difference([key, value])
    tibble = pd.DataFrame(columns=fixed_vars)  # empty frame
    # display(tibble)
    new_vars = df[key].unique()
    # ñprint(new_vars)
    for v in new_vars:
        df_v = df[df[key] == v]
        print(df_v)
        del df_v[key]
        df_v = df_v.rename(columns={value: v})
        tibble = tibble.merge(df_v, on=list(fixed_vars), how=join_how)
    # return tibble


# Test: `cast_test`
table1 = pd.read_csv("N7_Tydying Data/table1.csv")
table2 = pd.read_csv("N7_Tydying Data/table2.csv")
print("=== table2 ===")
display(table2, "\n")

print('\n=== tibble2 = cast (table2, "type", "count") ===')
tibble2 = cast(table2, "type", "count")
display(tibble2)

assert tibbles_are_equivalent(table1, tibble2)

print("\n(Passed.)")
