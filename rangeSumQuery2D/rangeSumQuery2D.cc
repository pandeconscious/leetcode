#include <vector>

using namespace std;

class NumMatrix {
private:
	vector<vector<int> > SumMat;
public:
    NumMatrix(vector<vector<int> > &matrix) {
	   if(matrix.size() != 0 && matrix[0].size() != 0){
		   int numRows = matrix.size();
		   int numCols = matrix[0].size();
		   SumMat.resize(numRows);
		   for(int i = 0; i < numRows; i++){
				SumMat[i].resize(numCols);
		   }
		   SumMat[0][0] = matrix[0][0];
		   for(int i = 0; i < numRows; i++){
				for(int j = 0; j < numCols; j++){
					if(i != 0 || j != 0){
						if(i == 0){
							SumMat[i][j] = SumMat[i][j-1] + matrix[i][j];
						}
						else if(j == 0){
							SumMat[i][j] = SumMat[i-1][j] + matrix[i][j];
						}
						else{
							SumMat[i][j] = SumMat[i-1][j] + SumMat[i][j-1] - SumMat[i-1][j-1] + matrix[i][j];
						}
					}
				}
		   }
	   }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
		if(SumMat.size() == 0)
			return 0;
       	if(row1 == 0 && col1 == 0){
			return SumMat[row2][col2];
		}
		else if(row1 == 0 && col1 != 0){
			return SumMat[row2][col2] - SumMat[row2][col1-1];
		}
		else if(row1 != 0 && col1 == 0){
			return SumMat[row2][col2] - SumMat[row1-1][col2];
		}
		else{
			return SumMat[row2][col2] + SumMat[row1-1][col1-1] - SumMat[row2][col1-1] - SumMat[row1-1][col2];
		}
    }
};

int main(){

	return 0;
}


// Your NumMatrix object will be instantiated and called as such:
// NumMatrix numMatrix(matrix);
// numMatrix.sumRegion(0, 1, 2, 3);
// numMatrix.sumRegion(1, 2, 3, 4);
