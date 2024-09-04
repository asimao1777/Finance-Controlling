import pandas as pd
import numpy as np
from io import StringIO
from IPython.display import display

A_csv = """country,year,cases
Afghanistan,1999,745
Brazil,1999,37737
China,1999,212258
Afghanistan,2000,2666
Brazil,2000,80488
China,2000,213766"""

with StringIO(A_csv) as fp:
    A = pd.read_csv(fp)
print("=== A ===")
# display(A)

B_csv = """country,year,population
Afghanistan,1999,19987071
Brazil,1999,172006362
China,1999,1272915272
Afghanistan,2000,20595360
Brazil,2000,174504898
China,2000,1280428583"""

with StringIO(B_csv) as fp:
    B = pd.read_csv(fp)
print("\n=== B ===")
#display(B)

C = A.merge(B, on=["country", "year"])
print("\n=== C = merge(A, B) ===")
# display(C, "\n")

G = C.copy()  # If you do not use copy function the original data frame is modified
G["year"] = G["year"].apply(lambda x: "'{:02d}".format(x % 100))
# display(G)


def calc_prevalence(G):
    assert "cases" in G.columns and "population" in G.columns
    G_copy = G.copy()
    G_copy["prevalence"] = G_copy.apply(lambda row: row.cases / row.population, axis=1)
    return G_copy


display(calc_prevalence(G))
