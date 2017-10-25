__author__ = 'Marko Prelevikj'
import sys
import boolean
import solver_methods

def handle_input(input_file_name):
    '''
     handles the funtion input
    '''
    input_type = 0
    num_vars = 0
    num_clauses = 0
    formula = []
    used_vars = dict()
    with open(input_file_name) as file:
        for line in file:
            line = line.strip().split(' ')
            if line[0] == 'c':
                if len(line) > 1:
                    print('A comment: %', ' '.join(line[1:]))
                continue
            if line[0] == 'p':
                input_type = line[1]
                num_vars = int(line[2])
                num_clauses = int(line[3])
                continue
            print(line[:-1])
            for var in line[:-1]:
                var = abs(int(var))
                if var in used_vars:
                    print('Used:', used_vars[var],end='; ')
                else:
                    used_vars[var] = boolean.Variable(var)
                    print('New: ', used_vars[var],end='; ')
            print()
            formula.append(boolean.Or([[used_vars[int(x)] if int(x) > 0 else boolean.Not(used_vars[abs(int(x))]) for x in line[:-1]], len(line[:-1])]))
        formula = boolean.And([formula, len(formula)])
        print(formula)
    return (input_type, num_vars, num_clauses, formula)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
    else:
        print('Please provide input/output filename arguments')
        sys.exit(-1)

    intype, num_vars, num_clauses, formula = handle_input(input_file_name)
    solution = solver_methods.dpll(formula)

    print('Type: {}, number of vars {}, number of clauses {}.'.format(intype, num_vars, num_clauses))
    print(formula)
    print(solution)
