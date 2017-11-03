def substitute(formula, valuation):
    substituted = []
    for clause in formula:
        new_clause = []
        for literal in clause:
            val = valuation[abs(literal)]
            new_clause.append(False if val is None else val)
        substituted.append(new_clause)
    return substituted

def eval(formula, valuation):
    formula_w_vals = substitute(formula, valuation)
    valuated = []
    for clauses in formula:
        valuated.append(any(clauses))
    return all(valuated)
