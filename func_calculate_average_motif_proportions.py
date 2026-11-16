# RAnsarihaghi: Code to calculate the numbers of motifs, from single cells to 100-cell motifs, in a cell population with different probabilities of tube formation between cells in a linear network.
Ncells=100 # Number of cells
Nbonds=Ncells-1 # Number of bonds between cells: 10 cells have 9 bonds, 20 cells have 19 bonds, and so on.
Pp_values =  [0.75]#[i/5.0 for i in range(0, 6)]# Define the values of Pp to use. Pp is the probability that a tube exists. 
Pq_values = [1-Pp_values[0]]#[i/5.0 for i in range(0, 6)][::-1]# Define the values of Pq to use. Pq is the probability that a tube is absent.   

def get_output():
    import random
    import numpy as np
    from numpy.random import choice

    # Create a random list of 0s and 1s using the specified probabilities:
    Vs=[]
    #Pq_values = [0.75]#[i/5.0 for i in range(0, 6)][::-1]# Define the values of Pq to use. Pq is the probability that a tube is absent.
    #Pp_values =  [0.25]#[i/5.0 for i in range(0, 6)]# Define the values of Pp to use. Pp is the probability that a tube exists.    
    for i in range(len(Pq_values)): 
        Pq = Pq_values[i]
        Pp = Pp_values[i]
        V = random.choices ([0, 1], weights=[Pq, Pp], k=int(Nbonds)) 
        Vs.append(V)
    #print('vs=',Vs)

    string = "Cell"
    Vcells=[]
    for V in Vs:
        Vcell = []
        # Add 'Cell' as an element between the members of the randomly generated list V:   
        for elem in V:
            Vcell.append(elem)
            Vcell.append(string)   
        Vcell.insert(0,string)
        Vcells.append(Vcell)    
   #print(Vcells)       

    # Create a list containing the indices of all 1s in each Vcell list:
    one_indexs=[]
    for vcelllist in Vcells:
        one_index=[]
        for mem in range(len(Vcell)):
            if vcelllist[mem]==1:
                one_index.append(mem)
        one_indexs.append(one_index)
    #print('one_indexs:',one_indexs)

    # Create a list to calculate and store the distances between consecutive 1s:
    twos_lists=[]
    for oneindlist in one_indexs:
        twos_list=[]
        for indone in range(len(oneindlist)-1):
            if oneindlist[indone+1]-(oneindlist[indone])==2:   # Find distances of 2, indicating that two adjacent cells are connected. 
                twos_list.append(2)
            else:
                mtwos=oneindlist[indone+1]-(oneindlist[indone]) # Find distances other than 2, indicating that the connected cells are not adjacent.
                twos_list.append(mtwos)
        twos_lists.append(twos_list)
    #print('twos_lists:',twos_lists)

    # Define a function to count consecutive occurrences of 2:
    def count_twos(twos_lists):
        counts_list=[]
        for twoslist in twos_lists:
            counts = []
            current_count = 0
            for num in twoslist:
                if num == 2:
                    current_count += 1
                if num!=2:
                    counts.append(current_count) # Add the current count of consecutive 2s.             
                    current_count = 0                         
            counts.append(current_count)
            counts_list.append(counts)
        return counts_list
    counts_list = count_twos(twos_lists) # Call the function.
    #print('counts_list:',counts_list)

    # Record the counts of motifs containing multiple cells:
    values_list = [] 
    for countlist in counts_list:
        values = [0]*Ncells
        for i in countlist:
            if i < 1 or i > Ncells-2:
                continue
            values[i+1] += 1
        values_list.append(values)
    #print('values_list:',values_list)    

    # Count the number of two-cell motifs: 
    set1 = ['Cell', 1, 'Cell', 0]
    set2 = [0, 'Cell', 1, 'Cell']
    set3 = [0, 'Cell', 1, 'Cell', 0]
    for x, listcell in enumerate(Vcells):
        d = 0
        if listcell[0:4] == set1:
            d += 1            
        if listcell[-4:] == set2:
            d += 1            
        z = 0
        while z < len(listcell):
            if listcell[z:z+5] == set3:
                d += 1
                z += 2       
            else:
                z += 1
        values_list[x][1] = d
    #print('values_list:',values_list)  
    
    # Calculate the number of single cells and add it to values_list.   
    coefficient_values = [i+1 for i in range(Ncells)]
    for n, vcelllist in enumerate(Vcells):
        single = Ncells - sum(value * coefficient_values[m] for m, value in enumerate(values_list[n]))
        values_list[n][0] = single
    #print('values_list:',values_list)

    output= values_list
    return output
 
