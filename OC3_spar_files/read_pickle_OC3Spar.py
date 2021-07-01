# import any modules
import pickle
import numpy as np


# open pickle file
with open('outputs/refturb_output.pkl', 'rb') as f:
    pickle_data = pickle.load(f)
    
# # read in the contents of the pickle file
# print(type(pickle_data))
# print(len(pickle_data))
# print(pickle_data[0])
# print(len(pickle_data[0]))
# print(type(pickle_data[0][1]))
# rho_fiber_dict = pickle_data[0][1]
# 
# for key in rho_fiber_dict.keys():
#     print(key, rho_fiber_dict[key])
# 
# 
# # print out the keys available (data available) within the pickle file
# for item in pickle_data:
#     name, data_dict = item[0], item[1]
#     print(name, data_dict)
#     exit()


# identify the keys that we're interested in
# (name, idx) pairs here
keys_of_interest = [
    "floatingse.platform_mass",
    "floatingse.platform_center_of_mass",
    "floatingse.platform_I_total",
    "floatingse.member0.buoyancy_force",
    ]
    
output_data = {}

# grab specific data from pickle file using those keys we've identified
for item in pickle_data:
    abs_name, data_dict = item[0], item[1]
    prom_name = data_dict['prom_name']
    
    for key in keys_of_interest:
        
        if key in prom_name:
            output_data[key] = data_dict['value']
            
            
print(output_data)
            
            


# set up plotting script for data we want to visualize



# Actually plot data