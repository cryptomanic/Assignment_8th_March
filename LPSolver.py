class LPSolver:
    co_cof, maxPos, minPos, x, keep_track = [], [], [], [0,0,0,0], []    
    def solve(self,method_name,objctve,cnstrts_rs,cnstrts_ls) : 
        if method_name == 'Simplex':
            # plot constraint regions                
            self.graph_plot(cnstrts_rs,cnstrts_ls)
            # variables coefficient of constraints
            for i in cnstrts_ls:
                self.co_cof += [[j for j in i]]
            for i in range(len(cnstrts_rs)):
                self.co_cof[i] += [0 for j in range(len(cnstrts_rs))]
                self.co_cof[i][len(objctve)+i] = 1
            # objective function coefficient
            ob_cof = objctve + [0 for i in range(len(cnstrts_rs))]
            # variables that will provide final solution
            fin_cof = [0 for i in range(len(cnstrts_rs))]    
            self.keep_track = [i+3 for i in range(len(cnstrts_rs))] 
            while True:
                # finding the bottom rows by C-B*V
                for i in range(len(ob_cof)):
                    sum = 0
                    for j in range(len(cnstrts_rs)):
                        sum += self.co_cof[j][i]*fin_cof[j]
                    self.maxPos += [ob_cof[i]-sum]          
                # check all the elements in bottom rows less than or equal to zero
                counter = 0
                for i in self.maxPos:
                    if i <= 0:
                        counter += 1
                if counter == len(ob_cof):
                    break
                # find index of maxvalue in bottom rows
                index_bottom = self.maxPos.index(max(self.maxPos)) 
                # finding the right column
                for i in range(len(cnstrts_rs)):
                    if self.co_cof[i][index_bottom] != 0:
                        self.minPos += [cnstrts_rs[i]*1.0/self.co_cof[i][index_bottom]]
                    elif cnstrts_rs[i] > 0:
                        self.minPos += ["Infinity"]
                    else:
                        self.minPos += ["-Infinity"] 
                counter = 0
                # check whether right column element are less than or equal to 0
                for i in self.minPos:
                    if i != "Infinity":
                        if i == "-Infinity":
                            counter += 1
                        elif i<=0:    
                            counter += 1
                if counter == len(cnstrts_rs):
                    return " Problem Is Unbounded "
                # list of positive value in right column
                pos_val_collec = []
                for i in self.minPos:
                    if i!="Infinity" and i!="-Infinity":
                        if i>0:
                           pos_val_collec += [i] 
                # false index of minimum value in right column
                index_right = pos_val_collec.index(min(pos_val_collec))+1              
                # find index with respect to right column
                counter = 0
                for i in self.minPos:
                   if i!="Infinity" and i!="-Infinity":
                        if i > 0:
                            counter += 1
                   if counter == index_right:
                        index_right = self.minPos.index(i)
                        break 
                # set incoming variable value
                fin_cof[index_right] = ob_cof[index_bottom]            
                cnstrts_rs[index_right] = cnstrts_rs[index_right]*1.0/self.co_cof[index_right][index_bottom]
                # updating keep_track list
                self.keep_track[index_right] = index_bottom+1
                # pivot element
                pivot = self.co_cof[index_right][index_bottom]     
                # divide row containing pivot by pivot element value
                for i in range(len(ob_cof)):
                    self.co_cof[index_right][i] = self.co_cof[index_right][i]/(pivot*1.0)    
                # make all elements except pivot equal to zero in column containing pivot element
                for i in range(len(cnstrts_rs)):
                    if i != index_right:
                        num = self.co_cof[i][index_bottom]
                        for j in range(len(ob_cof)):
                             self.co_cof[i][j] -= num*self.co_cof[index_right][j]
                        cnstrts_rs[i] -= num*cnstrts_rs[index_right]
                # updating graph
                self.x[0] = self.x[2]
                self.x[1] = self.x[3]
                if 1 in self.keep_track:
                    self.x[2] = cnstrts_rs[self.keep_track.index(1)]
                if 2 in self.keep_track:
                    self.x[3] = cnstrts_rs[self.keep_track.index(2)]                   
                self.status_aft_e_iteration()
                print (self.co_cof, self.maxPos, self.minPos, self.x, self.keep_track, ob_cof,fin_cof)        
                self.maxPos, self.minPos = [], []                             
        sum = 0
        for i in range(len(fin_cof)):
            sum += fin_cof[i]*cnstrts_rs[i]
        return sum     
    # display constraints via graph
    def graph_plot(self,rs_cnstrts,ls_cnstrts):
        import matplotlib.pyplot as plt
        plt.plot(0,0,'ko')
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        for i in range(len(rs_cnstrts)):
            x = [0,rs_cnstrts[i]*1.0/ls_cnstrts[i][0]]
            y = [rs_cnstrts[i]*1.0/ls_cnstrts[i][1],0]
            plt.plot(x,y,linewidth=3.0)
            plt.show()
    def status_aft_e_iteration(self):
        import matplotlib.pyplot as plt
        x1, y1, x2, y2 = self.x[0], self.x[1], self.x[2], self.x[3]
        plt.plot(x2, y2,'ko')
        plt.annotate('', xy = ((x1+2*x2)/3.0,(y1+2*y2)/3.0), xytext = ((x2+2*x1)/3.0,(y2+2*y1)/3.0), 
        arrowprops = dict(facecolor = 'black',shrink = 0.03))
        plt.show()
