import pandas as pd
import numpy as np
from io import StringIO
from IPython.display import display
from pandas.testing import assert_frame_equal
import re


# CALLING DATA FOR TESTING CODE

tibble3 = pd.read_csv("N7_Tydying Data/Tibble3.csv")
print("\n=== tibble3 = separate (table3, ...) ===\n")
display(tibble3)

tibble3_copy = tibble3.copy()
fixed_var = tibble3.columns.difference(["cases", "population"])
# print(fixed_var)
int_to_str = lambda x: str(x)
tibble3_copy["cases_str"] = tibble3.cases.apply(int_to_str)
tibble3_copy["population_str"] = tibble3.population.apply(int_to_str)
del tibble3_copy["cases"]
del tibble3_copy["population"]
# print(tibble3_copy)
tibble3_copy["rate"] = tibble3_copy["cases_str"] + "/" + tibble3_copy["population_str"]
del tibble3_copy["cases_str"]
del tibble3_copy["population_str"]
# print(tibble3_copy)

table3 = pd.read_csv("N7_Tydying Data/table3.csv")

# FUNCTION GIVEN BY EXERCISE


def str_join_elements(x, sep=""):
    assert type(sep) is str
    return sep.join([str(xi) for xi in x])


# CODE FOR THIS EXERCISE - MY CODE


def unite(df, cols, new_var, combine=str_join_elements):
    # Hint: http://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe

    df_copy = df.copy()
    #     display(df_copy)

    str_ = lambda x: str(x)
    for i in range(len(cols)):
        df_copy[cols[i]] = df_copy[cols[i]].apply(str_)

    size_df = len(df_copy)
    size_cols = len(cols)

    beg = cols.index(cols[0])
    end = cols.index(cols[-1])
    #     print(beg, end, '\n')

    list_ = []

    for i in range(size_df):
        x = df_copy.loc[i, cols[beg] : cols[end]]
        #       print(x, '\n')
        list_.append(combine(x))
    #     print(list_, ' \n')

    df_copy[new_var] = pd.Series(list_)
    #     display(df_copy)
    for i in range(size_cols):
        del df_copy[cols[i]]
    #     display(df_copy)

    return df_copy


# Test Code - Function Call

t = unite(
    tibble3,
    ["cases", "population"],
    "rate",
    combine=lambda x: str_join_elements(x, "/"),
)

print(t, "\n")

# CODE FOR THIS EXERCISE - GT CODE
# ALTERNATIVE W/ PARAMETER "COMBINE" AND W/ SEPARATE FUNCTION STR_JOIN_ELEMENTS


def unite(df, cols, new_var, combine=str_join_elements):
    df_copy = df.copy()

    df_copy[new_var] = df_copy[cols].apply(combine, axis=1)
    # print(df_copy)

    for var in cols:
        del df_copy[var]

    return df_copy


# Test Code - Function Call

z = unite(
    tibble3,
    ["cases", "population"],
    "rate",
    combine=lambda x: str_join_elements(x, "/"),
)

print(z, "\n")

# ALTERNATIVE W/O PARAMETER "COMBINE" AND W/O SEPARATE FUNCTION STR_JOIN_ELEMENTS


def unite2(df, cols, new_var, sep=""):
    df_copy = df.copy()

    comb_as_str = lambda row: sep.join(row.values.astype(str))
    df_copy[new_var] = df_copy[cols].apply(comb_as_str, axis=1)

    for var in cols:
        del df_copy[var]

    return df_copy


# TEST CODE

w = unite2(tibble3, ["cases", "population"], "rate", sep="/")
print(w)
