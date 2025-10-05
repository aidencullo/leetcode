impl Solution {
    pub fn satisfies_conditions(grid: Vec<Vec<i32>>) -> bool {
        let rows = grid.len();
        let cols = if rows > 0 { grid[0].len() } else { 0 };
        for i in 0..rows {
            for j in 0..cols {
                if j < cols - 1 && grid[i][j] == grid[i][j + 1] {
                    return false;
                }
                if i < rows - 1 && grid[i][j] != grid[i + 1][j] {
                    return false;
                }
            }
        }
        true
    }
}
