import pandas as pd
import numpy as np
from io import StringIO
from IPython.display import display

# Test: `canonicalize_tibble_test`

# Test input
canonical_in_csv = """,c,a,b
2,hat,x,1
0,rat,y,4
3,cat,x,2
1,bat,x,2"""

with StringIO(canonical_in_csv) as fp:
    canonical_in = pd.read_csv(fp, index_col=0)
print("=== Input ===")
display(canonical_in)
print("")


def canonicalize_tibble(X):
    # Enforce Property 1:
    var_names = sorted(X.columns)
    # print(var_names)
    print(X[var_names])
    Y = X[var_names].copy()
    print(Y)

    # Enforce Property 2 & 3:
    Y.sort_values(by=var_names, inplace=True)
    Y.set_index([list(range(0, len(Y)))], inplace=True)

    return Y


# Test output solution
canonical_soln_csv = """,a,b,c
0,x,1,hat
1,x,2,bat
2,x,2,cat
3,y,4,rat"""

with StringIO(canonical_soln_csv) as fp:
    canonical_soln = pd.read_csv(fp, index_col=0)
print("=== True solution ===")
display(canonical_soln)
print("")

canonical_out = canonicalize_tibble(canonical_in)
print("=== Your computed solution ===")
display(canonical_out)
print("")

canonical_matches = canonical_out == canonical_soln
print("=== Matches? (Should be all True) ===")
display(canonical_matches)
assert canonical_matches.all().all()

print("\n(Passed.)")
