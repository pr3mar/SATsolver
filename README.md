# SAT solver

A SAT solver by Marko Prelevikj and Luka Zlatečan

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

For running this project you need to have Python 3.6 installed on your local machine.

### Installing

Download project with git clone command.

```
git clone https://github.com/pr3mar/SATsolver.git
git checkout ara # this is the branch for the ARA subject
```

## Running the tests

Run test with following comand:

```
python solver.py -i inputs/input2 -o outputs/output2 -m max
```
[not applicable since [issue #1](https://github.com/pr3mar/SATsolver/issues/1)] The output is going to be stored in a file named by the following convention:
```
<output file directory>/out_<method>_<provided file name with suffix>
```
where method is: 
`greedy, shuffle, max_occ, bin_max_occ`

To show strength of our solver we found an input with 497 variables and 5727 clauses which our solver managed to solve it under 3 seconds. Mentioned input is stored in **/inputs** folder and is named **input3.txt**. We run this test with method **bin-max-occ**  (**-m bin**), since this is our fastest method. 

Run this test with this command:
```
python solver.py -i inputs/input3.txt -o outputs/output3.txt -m bin
```

### N-Queens reducer
In the file `nqueen.py` is the reducer used to generate the input for the SAT solver for the N-Queens problem. 

### Arguments

* **-i/--input** [required] -> Input file name
* **-o/--output** [required] -> Output file name
* **-m/--method** [optional] -> Method to solve the problem. Available options: (all|greedy|shuffle|max|bin). The default option is `all`

### Examples

There are some prepared input files inside **/inputs** folder.

## Authors

* **Marko Prelevikj**
* **Luka Zlatečan**
