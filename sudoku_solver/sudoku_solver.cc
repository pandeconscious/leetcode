#include <iostream>
#include <vector>
#include <cmath>


using namespace std;

class Solution {
private:
	int n, nSub;

	void GetSubSquareTopLeftIndices(int r, int c, int& start_r, int& start_c){
		int rowDiV = r/nSub;	
		int colDiv = c/nSub;
		start_r = rowDiV*nSub;
		start_c = colDiv*nSub;
	}

	//function checks if the sudoku has no other character x along its row r 
	//on inserting character x at position (r,c)
	bool isRowWiseValid(vector<vector<char> >& board, int r, int c, char x){
		for(int c_ = 0; c_ < n; c_++){
			if(board[r][c_] == x)
				return false;
		}
		return true;
	}

	//function checks if the sudoku has no other character x along its  col c 
	//on inserting character x at position (r,c)
	bool isColWiseValid(vector<vector<char> >& board, int r, int c, char x){
		for(int r_ = 0; r_ < n; r_++){
			if(board[r_][c] == x)
				return false;
		}
		return true;
	}

	//function checks if the sudoku has no other character x in the corresponding subsquare 
	//on inserting character x at position (r,c)
	bool isSubSquareWiseValid(vector<vector<char> >&board, int r, int c, char x){
		int start_r, start_c;
		GetSubSquareTopLeftIndices(r, c, start_r, start_c);
		for(int i = start_r; i < start_r + nSub; i++){
			for(int j = start_c; j < start_c + nSub; j++){
				if(board[i][j] == x)
					return false;
			}
		}
		return true;
	}


	bool solveSudokuUtil(vector<vector<char> >& board, int r, int c){
		if(r >= n){
			return true;
		}
		if(c >= n){
			return solveSudokuUtil(board, r+1, 0);
		}
		if(board[r][c] == '.'){
			for(int i = 1; i <= n; i++){
				char val = '0'+i;
				if(isRowWiseValid(board, r, c, val) && isColWiseValid(board, r, c, val) && isSubSquareWiseValid(board, r, c, val)){
					board[r][c] = val;	
					if(solveSudokuUtil(board, r, c+1)){
						return true;
					}
				}
			}
			board[r][c] = '.';
			return false;
		}
		else{
			return solveSudokuUtil(board,r, c+1);
		}
	}

public:
    void solveSudoku(vector<vector<char> >& board) {
		n = board.size(); 
		nSub = (int)sqrt(n);
		if(n == 0 || n == 1)
			return;
		solveSudokuUtil(board, 0, 0);			
    }
};

int main(){
	Solution* sol = new Solution();	
	vector<vector<char> > arr(4);
	for(int i = 0; i < 4; i++){
		arr[i].resize(4, '.');
	}
	sol->solveSudoku(arr);
	return 0;
}
