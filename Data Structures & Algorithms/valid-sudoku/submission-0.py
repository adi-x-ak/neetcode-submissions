class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        flag = True
        
        for j in range(9):
            tmp = set()
            for i in range(9):
                a = board[i][j]
                if a == ".":
                    continue

                if int(a) > 9 or a in tmp:
                    return False

                if a not in tmp:
                    tmp.add(a)


        for i in range(9):
            tmp = set()
            for j in range(9):
                a = board[i][j]
                if a == ".":
                    continue

                if int(a) > 9 or a in tmp:
                    return False

                if a not in tmp:
                    tmp.add(a)

        for row in range(0,9,3):
            for col in range(0,9,3):
                tmp =set()

                for i in range(row,row+3):
                    for j in range(col,col+3):
                        a = board[i][j]

                        if a == ".":
                            continue

                        if int(a) > 9 or a in tmp:
                            return False

                
                        tmp.add(a) 


        return flag


        


        