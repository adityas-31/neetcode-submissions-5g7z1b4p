class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = self.checkRows(board)
        c = self.checkColumns(board)
        b = self.checkSectors(board)

        if r != True or c != True or b != True:
            return False
        return True
        # print("Rows are unique - " , r)
        # print("Columns are unique - " , c)
        
        

    def checkRows(self, board:List[List[str]]) -> bool:
        valid = True
        for row in board:
            if valid == True:
                n_count = dict()
                for n in row:
                    if n in n_count and n != '.':
                        n_count[n] += 1 #if any number is repeated in the row, break from the loop and set valid to false
                        valid = False
                        break
                    else:
                        n_count[n] = 1
            elif valid == False:
                break
        return valid

    def checkColumns(self , board:List[List[str]]) -> bool:
        
        cols = [[] for row in board] #have cols be a list of lists
        for i in range(8):
            for rows in board:
                cols[i].append([rows[i]][0])
        valid = self.checkRows(cols)
        # print("cols to rows = " , cols)
        return valid
            
    def checkSectors(self, board:List[List[str]]) -> bool:
        rows = list(list())
        b1 = board[:3]
        b2 = board[3:6]
        b3 = board[6:]
        g1 = [i[:3] for i in b1]
        g2 = [i[3:6] for i in b1]
        # print(g1)
        g = list(list())
        for r_ in range(1,4):
            
            r = r_ * 3
            # print(r)
            if r == 3:
                g.append([i[:3] for i in b1])
                g.append([i[:3] for i in b2])
                g.append([i[:3] for i in b3])
                
            elif r == 6:
                g.append([i[3:6] for i in b1])
                g.append([i[3:6] for i in b2])
                g.append([i[3:6] for i in b3])
            elif r == 9:
                g.append([i[6:] for i in b1])
                g.append([i[6:] for i in b2])
                g.append([i[6:] for i in b3])
        g_fin = []
        for box in g:
            box = box[0]+box[1]+box[2]
            g_fin.append(box)

        
        # print("final grid as rows = " , g_fin , "\nlen of g_fin is ", len(g_fin))
        valid = self.checkRows(g_fin)
        return valid


