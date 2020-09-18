import numpy as np
from time import perf_counter

def DNA_Neumann():
        
    start = perf_counter()
        
    semillas = [[512//2, 512//2]]
    
    grilla = np.zeros((512, 512), dtype = int)
    
    i_grilla = [[x,y] for x in range(512) for y in range(512)]

    for cord in semillas: 
        i_grilla.remove(cord)
        grilla[cord[1]][cord[0]] = 1
         
    i_random = np.random.choice(512*512-len(semillas), size = 20000, replace = False)

    pos = np.array([i_grilla[i] for i in i_random])    
        
    print(perf_counter()-start)
            
    eliminar = np.ones(len(pos), dtype = bool)
        
    for i in range(len(pos)):
        
        x, y = pos[i][0], pos[i][1]
            
        if grilla[y][(x-1)] or grilla[(y-1)][(x-1)] or grilla[(y-1)][x]:
            grilla[y, x] = 1
            eliminar[i] = False 
        else:
            x_p = (x+1) % grilla.shape[1]
    
            if grilla[(y-1)][x_p] or grilla[y][x_p]:
                grilla[y, x] = 1
                eliminar[i] = False 
            else:
                y_p = (y+1) % grilla.shape[0]
                
                if grilla[y_p][x] or grilla[y_p][x-1] or grilla[y_p][x_p]:
                    grilla[y, x] = 1
                    eliminar[i] = False 

    pos = pos[eliminar]        
    
    for t in range(1000000):
        
        pos = np.mod(pos + np.random.randint(-1,2, size = (pos.shape[0], 2)), 512)
        
        eliminar = np.ones(len(pos), dtype = bool)
        
        for i in range(len(pos)):
        
            x, y = pos[i][0], pos[i][1]
            
            if grilla[y][(x-1)] or grilla[(y-1)][(x-1)] or grilla[(y-1)][x]:
                grilla[y, x] = 1
                eliminar[i] = False 
            else:
                x_p = (x+1) % grilla.shape[1]
    
                if grilla[(y-1)][x_p] or grilla[y][x_p]:
                    grilla[y, x] = 1
                    eliminar[i] = False 
                else:
                    y_p = (y+1) % grilla.shape[0]
                    
                    if grilla[y_p][x] or grilla[y_p][x-1] or grilla[y_p][x_p]:
                        grilla[y, x] = 1
                        eliminar[i] = False 

        pos = pos[eliminar]
                
    print(perf_counter()-start)
    print(pos.shape)
    
    return grilla, pos
    
grilla, pos = DNA_Neumann()
np.savetxt('grilla.txt', grilla, delimiter = ' ', fmt = '%d')
np.savetxt('camina.txt', grilla, delimiter = ' ', fmt = '%d')
