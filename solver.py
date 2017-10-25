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
                continue
            if line[0] == 'p':
                num_vars = int(line[2])
                num_clauses = int(line[3])
                continue
            for var in line[:-1]:
                var = abs(int(var))
                if not(var in used_vars):
                    used_vars[var] = boolean.Variable(var)
            formula.append(
                boolean.Or(
                    [
                        [used_vars[int(x)] 
                        if int(x) > 0 
                        else boolean.Not(used_vars[abs(int(x))]) 
                        for x in line[:-1]], len(line[:-1])
                    ]
                )
            )
        formula = boolean.And([formula, len(formula)])
        return (num_vars, num_clauses, formula)

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
    else:
        print('Please provide input/output filename arguments')
        sys.exit(-1)
    num_vars, num_clauses, formula = handle_input(input_file_name)
    solution = solver_methods.dpll(formula)
    print("Solution = ", solution)
