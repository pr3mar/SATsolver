# SAT solver

A SAT solver by Marko Prelevikj and Luka Zlatečan

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

For running this project you need to have Python installed on your local machine.

### Installing

Download project with git clone command.

```
git clone https://github.com/pr3mar/SATsolver.git
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
### Arguments

* **-i/--input** [required] -> Input file name
* **-o/--output** [required] -> Output file name
* **-m/--method** [optional] -> Method to solve the problem. Available options: (all|greedy|shuffle|max|bin). Default is `all`

### Examples

There are some prepared input files inside **/inputs** folder.

## Authors

* **Marko Prelevikj**
* **Luka Zlatečan**