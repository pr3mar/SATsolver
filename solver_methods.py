__author__ = 'Marko Prelevikj'
import boolean

def dpll_aux(formula, validation):
    '''
    An auxilary method for the solver, which is the de facto solver
    '''

    return True

def dpll(formula):
    '''
    A DPLL solver for the SAT problem
    '''
    print('original:  ', formula)
    formula = formula.simplify()
    print('simplified:', formula)
    return formula
