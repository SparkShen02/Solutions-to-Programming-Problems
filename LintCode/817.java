/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * obj.update(row,col,val);
 * int param_2 = obj.sumRegion(row1,col1,row2,col2);
 */
 /**
  * https://blog.csdn.net/XT_NOI/article/details/72715904
  * S(x1, y1, x2, y2) 表示以 (x1, y1) 为左上元素和以 (x2, y2) 为右下元素的矩阵中所有元素的和
  * S(x1, y1, x2, y2) = S(0, 0, x2, y2) + S(0, 0, x1−1, y1−1) − S(0, 0, x1−1, y2) − S(0, 0, x2, y1−1)
  * prefixSum[x][y]表示S(0,0,x,y)
  * -->
  * S(x1, y1, x2, y2) = prefixSum[x2][y2] + prefixSum[x1−1][y1−1] 
  *                     − prefixSum[x1−1][y2] − prefixSum[x2][y1−1]
  * prefixSum[x][y] = matrix[x][y] + prefixSum[x−1][y] + matrix[x][y−1] − prefixSum[x−1][y−1]
  */
class NumMatrix {
    private int[][] prefixSum;
    private int[][] matrix;
    private int row;
    private int col;
    
    public NumMatrix(int[][] matrix) {
        this.matrix = matrix;
        
        row = matrix.length; 
        col = matrix[0].length; 
        prefixSum = new int[row][col]; 
  
        prefixSum[0][0] = matrix[0][0]; 
        // Filling first row and first column 
        for (int i=1; i<col; i++){ prefixSum[0][i] = prefixSum[0][i-1] + matrix[0][i]; }
        for (int i=1; i<row; i++){ prefixSum[i][0] = prefixSum[i-1][0] + matrix[i][0]; }
  
        for (int i=1; i<row; i++){
            for (int j=1; j<col; j++){ 
                prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + matrix[i][j]; 
            }
        }
    }
    
    public void update(int row1, int col1, int val) {
        int change=val-matrix[row1][col1];
        matrix[row1][col1]=val;
        
        for (int i=row1; i<row; i++){
            for (int j=col1; j<col; j++){
                prefixSum[i][j]+=change;
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        if (row1==0 && col1==0){ return prefixSum[row2][col2]; }
        if (row1==0){ return prefixSum[row2][col2] - prefixSum[row2][col1-1]; }
        if (col1==0){ return prefixSum[row2][col2] - prefixSum[row1-1][col2]; }
        
        return prefixSum[row2][col2] + prefixSum[row1-1][col1-1] - prefixSum[row1-1][col2] 
               - prefixSum[row2][col1-1];
    }
}