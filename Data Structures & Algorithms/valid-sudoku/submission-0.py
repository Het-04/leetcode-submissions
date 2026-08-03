class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                
                result = board[r][c]
            
                if result == ".":
                    continue

                if (result in rows[r]) or (result in cols[c]) or (result in squares[(r//3, c//3)]):
                    return False
            
                rows[r].add(result)
                cols[c].add(result)
                squares[(r//3, c//3)].add(result)
        
        return True
        