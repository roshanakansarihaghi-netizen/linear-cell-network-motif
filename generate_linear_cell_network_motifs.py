# R_Ansarihaghi
import func_calculate_average_motif_proportions
import time
import json

start_time = time.time()

# Call get_output once before the loop; the duplicate call has been removed.
results = []
R = 1000  # Number of simulation repeats
for i in range(R):
    output = func_calculate_average_motif_proportions.get_output()
    results.append(output)
print('results =', results)
#print(len(results))

# Calculate the elapsed time ---------------------------------------------
elapsed_time = time.time() - start_time
elapsed_time_rounded = round(elapsed_time, 3)
print(f"Elapsed time: {elapsed_time_rounded} seconds")
# -------------------------------------------------------------------------
# Calculate the proportion for each element using nested loops:
proportion_results = []
for outer_list in results:
    current_outer_proportion = []
    for inner_list in outer_list:
        current_inner_proportion = []
        for element in inner_list:
            proportion = (element / func_calculate_average_motif_proportions.Ncells)
            current_inner_proportion.append(proportion)
        current_outer_proportion.append(current_inner_proportion)           
    proportion_results.append(current_outer_proportion)  
print(proportion_results)       
#print(len(current_inner_proportion),len(current_outer_proportion), len(proportion_results))

# Sum corresponding elements across all repeats and calculate their averages; repeat this for each inner list.
average_proportion_results = []
#average_proportion_results2 = []
for i in range(len(proportion_results[0])):
    ave = [0] * func_calculate_average_motif_proportions.Ncells
    for j in range(len(proportion_results)):
        for k in range(func_calculate_average_motif_proportions.Ncells):
            ave[k] += ((proportion_results[j][i][k])/R)
    #average_proportion_results2.append(ave)
    ave = [round(float(element), 5) for element in ave]    
    average_proportion_results.append(ave)        
print('average_proportion=',average_proportion_results)
#print('aveerage_proportion2=',average_proportion_results2)
#print(len(ave),len(average_proportion_results))

# Write the results to a text file.
with open(f"output_average_precent_{R}repeat_{func_calculate_average_motif_proportions.Ncells}cell_{func_calculate_average_motif_proportions.Pp_values[0]}.txt", "w") as file:
    json.dump(average_proportion_results, file)



