#include <cstddef>

#include "matmul.hpp"


matrix multiply(matrix A, matrix B) {
  std::vector<std::vector<int> > C;
  std::vector<int> row;
  size_t rows = A.size();
  size_t cols = B[0].size();

  for (size_t i = 0; i < rows; i++) {
    for (size_t j = 0; j < cols; j++) {
      int sum = 0;
      for (size_t k = 0; k < A[0].size(); k++) {
        sum += A[i][k] * B[k][j];
      }
      row.push_back(sum);
    }
    C.push_back(row);
    row.clear();
  }
  return C;
}

matrix multiplyChain(std::vector<matrix> chain) {
  matrix result = chain[0];
  for (size_t i = 1; i < chain.size(); i++) {
    result = multiply(result, chain[i]);
  }
  return result;
}
