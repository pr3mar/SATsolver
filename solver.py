from random import shuffle
import re, sys, copy, time, argparse, os.path
import itertools
from collections import Counter

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def parse_args():
    parser = argparse.ArgumentParser(description='SAT solver by Marko Prelevikj and Luka Zlatecan')
    parser.add_argument('-i', '--input', required=True, default='empty',
                            help='[required] Input file', metavar="FILE",
                                type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-o', '--output', required=True, default='empty',
                            help='[required] Output file', metavar="FILE")
    args = parser.parse_args()    
    return args

def parse_inst(input_file): # parse CNF files
    with open(input_file) as f: s = f.read()
    clauses = s.split('\n')
    fs = 0
    nvars = 0
    parsed = []
    vars = set()
    for f in clauses:
        if f.startswith('c'):
            continue
        elif f.startswith('p'):
            prob = re.split('\s+', f)
            nvars = int(prob[2])
            fs = int(prob[3])
        elif f.strip() == '':
            continue
        else:
            cl = list(map(lambda x: int(x), f.strip().split(' ')))
            cl.pop()
            vars = vars.union(set([abs(x) for x in cl]))
            parsed.append(cl)
    return parsed, dict.fromkeys(vars, None)

## modified simplify
def simplify(formula, valuations, add=None):
    if not (add is None):
        formula.insert(0, add)
    id = 0
    # print(formula)
    while id < len(formula): # identify all the unit clauses
        if len(formula[id]) == 1:
            val = formula[id][0]
            valuations[abs(val)] = val > 0 # value needed to be true
            iid = 0
            while iid < len(formula): # remove all clauses where the unit literal appears
                if val in formula[iid]:
                    formula.remove(formula[iid])
                    iid -= 1
                elif -val in formula[iid]:
                    formula[iid].remove(-val)
                    if(len(formula[iid]) == 0):
                        return formula, valuations
                iid += 1
            id = 0
        else:
            id += 1
    return formula, valuations

def SATsolver(formula, valuations, add=None):
    formula, valuations = simplify(formula, valuations, add)
    if formula == []: # if we managed to empty the list, the formula is satisfied
        return valuations
    if [] in formula: # if there is an empty clause in the formula, the formula is not satisfied
        raise Exception('Contradiction!')
    shuffled_list = [e for e, x in valuations.items() if x is None]
    shuffle(shuffled_list)
    for literal in shuffled_list:
        value = valuations[literal]
        try:
            return SATsolver(copy.deepcopy(formula), copy.deepcopy(valuations), [literal])
        except Exception:
            try:
                return SATsolver(list(formula), dict(valuations), [-literal])
            except Exception:
                continue
    raise Exception('No match!')

def findMaxOccList(formula):
    totals = Counter(i for i in map(abs, list(itertools.chain.from_iterable(formula))))
    return sorted(totals, key=totals.get, reverse=True)

def SATsolverMax(formula, valuations, add=None):
    formula, valuations = simplify(formula, valuations, add)
    if formula == []: # if we managed to empty the list, the formula is satisfied
        return valuations
    if [] in formula: # if there is an empty clause in the formula, the formula is not satisfied
        raise Exception('Contradiction!')
    maxOcc_list = findMaxOccList(formula)
    for literal in maxOcc_list:
        value = valuations[literal]
        try:
            return SATsolverMax(copy.deepcopy(formula), copy.deepcopy(valuations), [literal])
        except Exception:
            try:
                return SATsolverMax(list(formula), dict(valuations), [-literal])
            except Exception:
                continue
    raise Exception('No match!')

def findMaxOcc(formula):
    totals = Counter(i for i in map(abs, list(itertools.chain.from_iterable(formula))))
    return sorted(totals, key=totals.get, reverse=True)[0]

def SATsolverMaxBin(formula, valuations, add=None):
    formula, valuations = simplify(formula, valuations, add)
    if formula == []: # if we managed to empty the list, the formula is satisfied
        return valuations
    if [] in formula: # if there is an empty clause in the formula, the formula is not satisfied
        raise Exception('Contradiction!')
    maxOcc_el = findMaxOcc(formula)
    try:
        return SATsolverMaxBin(copy.deepcopy(formula), copy.deepcopy(valuations), [maxOcc_el])
    except Exception:
        try:
            return SATsolverMaxBin(list(formula), dict(valuations), [-maxOcc_el])
        except Exception:
            raise Exception('No match!')
    
def main():
    args = parse_args()
    formula, variables = parse_inst(args.input)
    findMaxOcc(formula)
    try:
        #Shuffle
        print('Finding solution for shuffler:')
        time_started = time.time()
        solution = SATsolver(formula, variables)
        time_ended = time.time()
        print('Execution time:', time_ended - time_started)
        #Max occurrence
        print('Finding solution for max occurrence:')
        time_started = time.time()
        solution = SATsolverMax(formula, variables)
        time_ended = time.time()
        print('Execution time:', time_ended - time_started)
        #Max occurrence binary
        print('Finding solution for binary max occurrence:')
        time_started = time.time()
        solution = SATsolverMaxBin(formula, variables)
        time_ended = time.time()
        print('Execution time:', time_ended - time_started)
    except Exception as error:
        solution = None

    print('Final solution', solution)
    # with open(args.output, 'w') as file:
    #     if solution is None:
    #         print('FAIL')
    #         file.write('0');
    #     else:
    #         print('SUCCESS')
    #         for x, y in solution.items():
    #             file.write('{} '.format(x if y else -x))

if __name__ == '__main__':
    main()
