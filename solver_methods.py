__author__ = 'Marko Prelevikj'
import boolean

def find_unit_clauses(formula):
    '''
    supposes that the formula is of type And()
    '''
    if not isinstance(formula, boolean.And):
        raise Exception('Invalid formula.')
    for clause in formula.terms:
        if len(clause.terms) == 1:
            return next(iter(clause.terms))
    return None

def dpll_simplify(formula, unit):
    if not isinstance(formula, boolean.And):
        raise Exception('Invalid formula')
    new_terms = []
    for clause in formula.terms:
        new_clause = clause
        if unit in clause.terms:
            continue
        if boolean.Not(unit).simplify() in clause.terms:
            new_clause = boolean.Or([[x for x in clause.terms.difference(set([boolean.Not(unit).simplify()]))], len(clause.terms) - 1])
        new_terms.append(new_clause)
    return boolean.And([new_terms, len(new_terms)])

def dpll_aux(formula, validation):
    '''
    An auxilary method for the solver, which is the de facto solver
    '''

    return True

def dpll(formula):
    '''
    A DPLL solver for the SAT problem
    '''
    valuations = {}
    print('original:  ', formula)
    unit_clause = find_unit_clauses(formula)
    print(unit_clause)
    while unit_clause != None:
        formula = dpll_simplify(formula, unit_clause)
        print(formula)
        valuations[unit_clause] = True
        unit_clause = find_unit_clauses(formula)
        print(unit_clause)
    # valuations[unit_clause] = True
    # formula = formula.evaluate(valuations)
    print('evaluated:', formula)
    print([(str(k), valuations[k]) for k in valuations])
    return formula
