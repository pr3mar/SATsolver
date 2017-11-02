from random import shuffle
from operator import itemgetter
import re, sys

# parse CNF files
def parse_inst(input_file):
    with open(input_file) as f: s = f.read()
    clauses = s.split("\n")
    fs = 0
    nvars = 0
    parsed = []
    vars = set()
    for f in clauses:
        if f.startswith("c"):
            continue
        elif f.startswith("p"):
            prob = re.split("\s+", f)
            nvars = int(prob[2])
            fs = int(prob[3])
        elif f.strip() == '':
            continue
        else:
            cl = list(map(lambda x: int(x), f.strip().split(" ")))
            cl.pop()
            vars = vars.union(set([abs(x) for x in cl]))
            parsed.append(cl)
    return parsed, dict.fromkeys(vars, None)

def simplify(formula, valuations, add=None):
    if not (add is None):
        formula.insert(0, add)
    id = 0
    print(formula)
    while id < len(formula): # identify all the unit clauses
        if len(formula[id]) == 1:
            val = formula[id][0]
            valuations[abs(val)] = val > 0 # value needed to be true
            iid = 0
            while iid < len(formula): # remove all clauses where the unit literal appears
                if val in formula[iid]:
                    formula.remove(formula[iid])
                    iid -= 1
                    print(formula)
                elif -val in formula[iid]:
                    formula[iid].remove(-val)
                    print(formula)
                iid += 1
            id = 0
        else:
            id += 1
    print(formula)
    print " "
    return formula, valuations

# def selective_simplify(formula, valuations, add):
#     if = 0
#     while id < len(formula): # identify all the unit clauses
#         if len(formula[id]) == 1:
#             val = formula[id][0]
#             valuations[abs(val)] = val > 0 # value needed to be true
#             iid = 0
#             while iid < len(formula): # remove all clauses where the unit literal appears
#                 if val in formula[iid]:
#                     formula.remove(formula[iid])
#                     iid = 0
#                     continue
#                 # formula[iid] = [e for e in formula[iid] if e not in (literalToRemove & set(formula[iid]))]
#                 if -val in formula[iid]:
#                     formula[iid].remove(-val)
#                 iid += 1
#             id = 0
#         else:
#             id += 1
#     return formula, valuations

# def SATshufflerOLD(formula, valuations, add=None):
#     formula, valuations = simplify(formula, valuations, add)
#     if formula == []: # if we managed to empty the list, the formula is satisfied
#         return valuations
#     if [] in formula: # if there is an empty clause in the formula, the formula is not satisfied
#         raise Exception('Contradiction!')
#     shuffled_list = [e for e, x in valuations.items() if x is None]
#     shuffle(shuffled_list)
#     for literal in shuffled_list:
#         try:
#             #print "1.",literal
#             #print valuations
#             return SATshuffler(list(formula), dict(valuations), [literal])
#         except Exception:
#             #print "2.", literal
#             #print valuations
#             try:
#                 return SATshuffler(list(formula), dict(valuations), [-literal])
#             except Exception:
#                 continue
#     raise Exception('Contradiction2!')
#             # if calc_valuations is None: # try assigning a Falce value to the picked literal
#             #     return SATshuffler(list(formula), dict(valuations), [-literal])
#             # else: # return the result if it exists
#             #     return calc_valuations

# def SATdll(formula, valuations, add=None):
#     formula, valuations = simplify(formula, valuations, add)
#     print(len(formula))
#     if formula == []: # if we managed to empty the list, the formula is satisfied
#         return valuations
#     if [] in formula: # if there is an empty clause in the formula, the formula is not satisfied
#         return None
#     remain = [e for e, x in valuations.items() if x is None]
#     for literal in remain:
#         sol = SATdll(list(formula), dict(valuations), [literal])
#         if sol is not None:
#             return sol
#         sol = SATdll(list(formula), dict(valuations), [-literal])
#         if sol is not None:
#             return sol
#     return None

def SATshuffler(formula, valuations, add=None):
    formula, valuations = simplify(formula, valuations, add)
    if formula == []: # if we managed to empty the list, the formula is satisfied
        return valuations
    if [] in formula: # if there is an empty clause in the formula, the formula is not satisfied
        return None
    shuffled_list = [e for e, x in valuations.items() if x is None]
    shuffle(shuffled_list)
    for literal in shuffled_list:
        sol = SATshuffler(list(formula), dict(valuations), [literal])
        if sol is not None:
            return sol
        sol = SATshuffler(list(formula), dict(valuations), [-literal])
        if sol is not None:
            return sol
    print("TU")
    return None

# def SATmaxpicker(formula, valuations, add=None):
#     formula, valuations = simplify(formula, valuations, add)
#     if formula == []: # if we managed to empty the list, the formula is satisfied
#         return valuations
#     if [] in formula: # if there is an empty clause in the formula, the formula is not satisfied
#         raise Exception('Contradiction!')
#     occ = dict.fromkeys((e for e, x in valuations.items() if x is None), 0)
#     for f in formula:
#         for v in f:
#             occ[abs(v)] += 1
#     try:
#         return SATmaxpicker(list(formula), dict(valuations), [max(occ, key=occ.get)])
#     except Exception:
#         return SATmaxpicker(list(formula), dict(valuations), [-(max(occ, key=occ.get))])


#Main
# if len(sys.argv) < 3:
#     print('Wrong input parameters!')
#     sys.exit(0)

# input_file = sys.argv[1]
# output_file = sys.argv[2]
# formula, variables = parse_inst(input_file)
formula, variables = parse_inst('inputs/input5')

#Try SATshuffler
solution = SATshuffler(list(formula), dict(variables))
if solution is not None:
    print(solution)
else:
    print("FAIL")

#Try SATmaxpicker
# try:
#     solution = SATmaxpicker(formula, variables)
# except Exception as contradiction:
#     print('FAIL:', contradiction)
#     sys.exit(0)
# print(solution)

# with open(output_file, 'w') as file:
#     if solution == None:
#         print("FAIL")
#         file.write('0');
#     else:
#         print("SUCCESS")
#         # formula[iid] = [e for e in formula[iid] if e not in (literalToRemove & set(formula[iid]))]
#         file.write(str([x if y else -x for x, y in solution.items()]))
