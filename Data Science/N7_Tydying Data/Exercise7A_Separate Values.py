import pandas as pd
import numpy as np
from io import StringIO
from IPython.display import display
from pandas.testing import assert_frame_equal
import re

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


table3 = pd.read_csv("N7_Tydying Data/table3.csv")
display(table3)
table1 = pd.read_csv("N7_Tydying Data/table1.csv")


def default_splitter(text):
    """Searches the given string for all integer and floating-point
    values, returning them as a list _of strings_.

    E.g., the call

      default_splitter('Give me $10.52 in exchange for 91 kitten stickers.')

    will return ['10.52', '91'].
    """
    fields = re.findall("(\d+\.?\d+)", text)
    return fields


# CODE FOR THIS EXERCISE - MY CODE


def separate(df, key, into, splitter=default_splitter):
    """Given a data frame, separates one of its columns, the key,
    into new variables.
    """
    assert type(df) is pd.DataFrame
    assert key in df.columns

    # Hint: http://stackoverflow.com/questions/16236684/apply-pandas-function-to-column-to-create-multiple-new-columns
    #     display(df)

    key_to_list = df[
        key
    ].tolist()  # take the column with the data to be separated and transform into a list
    #     print(key_to_list, '\n')
    list_to_string = ",".join(
        key_to_list
    )  # convert the list to string separated by comma
    #     print(list_to_string, '\n')
    separated_values = splitter(
        list_to_string
    )  # call REGEX function to split the values passed as strings.
    #     print(separated_values, '\n')

    dic = (
        {}
    )  # create a dictionary with new variables(columns as keys) and its values from existing variable in df
    for i in into:
        if i not in dic:
            dic.update({i: 0})
    #     print(dic,'\n')

    sep_values = [
        int(x) for x in separated_values
    ]  # transform every number into an integer
    #     print(sep_values, type(sep_values), '\n')

    num_of_new_var = len(into)  # number of new columns/variables

    for i in range(num_of_new_var):
        dic[into[i]] = sep_values[
            i::num_of_new_var
        ]  # populate the dictionary using slicing (the slice step == number of new variables)
    #     print(dic)

    new_df = pd.DataFrame(dic)  # transform the dictionay into a new DataFrame object
    #     display(new_df)
    final_df = pd.concat(
        [df, new_df], axis=1
    )  # concatenate the new DataFrame object with original DataFrame passed as argument
    del final_df[
        key
    ]  # delete the variable/column which was separated into new variables/columns
    #     display(final_df)

    return final_df


# CODE FOR THIS EXERCISE - GT CODE


def separate(df, key, into, splitter=default_splitter):
    """Given a data frame, separates one of its columns, the key,
    into new variables.
    """
    assert type(df) is pd.DataFrame
    assert key in df.columns

    # Hint: http://stackoverflow.com/questions/16236684/apply-pandas-function-to-column-to-create-multiple-new-columns

    def apply_splitter(text):
        fields = splitter(text)
        # print(fields)
        new_fields = pd.Series({into[i]: f for i, f in enumerate(fields)})
        print(new_fields)
        return new_fields

    fixed_vars = df.columns.difference([key])
    # print(fixed_vars)
    tibble = df[fixed_vars].copy()
    tibble_extra = df[key].apply(apply_splitter)
    print(tibble_extra)
    tibble = pd.concat([tibble_extra, tibble], axis=1)

    return tibble


# Test: `separate_test`

print("=== Recall: table3 ===")
display(table3)

tibble3 = separate(table3, key="rate", into=["cases", "population"])
print("\n=== tibble3 = separate (table3, ...) ===")
display(tibble3)
tibble3.to_csv(r"N7_Tydying Data/Tibble3.csv", index=False)

assert "cases" in tibble3.columns
assert "population" in tibble3.columns
assert "rate" not in tibble3.columns

tibble3["cases"] = tibble3["cases"].apply(int)
tibble3["population"] = tibble3["population"].apply(int)

assert tibbles_are_equivalent(tibble3, table1)
print("\n(Passed.)")
