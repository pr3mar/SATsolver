__author__= "Marko Prelevikj @ Approximation and Randomization algorithms 11.2017, Ljubljana, Slovenia"
import itertools, numpy as np

# not the most optimized solution, but it generates the inputs well
def reduce_nq_sat(n):
    output = ""
    numEls = 0
    for i in range(1, n + 1):
        rows = [str(i) + str(j) for j in range(1, n+1)]
        cols = [str(j) + str(i) for j in range(1, n+1)]
        for jj in rows:
            output += str(jj) + ' '
        numEls += 1
        output += '0\n'
        for jj in ['-' + str(x[0]) + ' -' + str(x[1]) + ' 0\n' for x in itertools.combinations(rows, 2)]:
            output += jj
            numEls += 1
        for jj in ['-' + str(x[0]) + ' -' + str(x[1]) + ' 0\n' for x in itertools.combinations(cols, 2)]:
            output += jj
            numEls += 1 
    rows, cols = np.indices((n, n))
    rows2 = np.fliplr(rows)
    cols2 = np.fliplr(cols)
    for i in range(-(n - 2), n -1):
        row_vals = np.diag(rows, k = i) + 1
        col_vals = np.diag(cols, k = i) + 1
        row2_vals = np.diag(rows2, k = i) + 1
        col2_vals = np.diag(cols2, k = i) + 1
        d1 = [str(jj[0]) + str(jj[1]) for jj in [x for x in zip(row_vals, col_vals)]]
        d2 = [str(jj[0]) + str(jj[1]) for jj in [x for x in zip(row2_vals, col2_vals)]]
        for jj in ['-' + str(x[0]) + ' -' + str(x[1]) + ' 0\n' for x in itertools.combinations(d1, 2)]:
            output += jj
            numEls += 1
        for jj in ['-' + str(x[0]) + ' -' + str(x[1]) + ' 0\n' for x in itertools.combinations(d2, 2)]:
            output += jj
            numEls += 1
    print(numEls)
    return output

dimacs = reduce_nq_sat(30)
with open('inputs/nqueen.in', 'w') as file:
    file.write(dimacs)
