### Question:
You are given a matrix of size `(m * n)`, each matrix element if either `0 or 1`. `1` denotes that there is a House and `0` denotes there a Park. You have to determine that largest house group or one that has a maximum number of neighbours. The neighbours of the house at the position `(i, j)` will be the houses at position at `(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)`.

Testcase:
* Input<br>
    + First-line contains an integer n denoting the number of rows
    + Next line contains an integer m denoting the number of columns
    + Next, n line contains m spaces seperated matrix values i.e. either 0 or 1.
* Constraints<br>
    + $n\ge 1, m \le 2000$
    + `matrix[i][j]` can be either 0 or 1
* Output<br>
    + Biggest neighbour Size
