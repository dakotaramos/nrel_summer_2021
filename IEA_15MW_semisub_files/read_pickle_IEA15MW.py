# import any modules
import pickle
import numpy as np
import pprint
import openpyxl


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
    "floatingse.platform_hull_mass",
    "floatingse.platform_ballast_mass",
    "floatingse.variable_ballast_mass",
    "floatingse.platform_center_of_mass",
    "floatingse.platform_center_of_buoyancy",
    "floatingse.platform_I_total",
    "floatingse.platform_displacement",
    ]
    
output_data = {}

# grab specific data from pickle file using those keys we've identified
for item in pickle_data:
    abs_name, data_dict = item[0], item[1]
    prom_name = data_dict['prom_name']
    
    for key in keys_of_interest:
        
        if key in prom_name:
            output_data[key] = data_dict['value']

# cleans up array values to remove unnecessary terms          
for k, v in output_data.items():
    if k == 'floatingse.platform_I_total':
        output_data[k] = v[0:3]        
    elif k == 'floatingse.platform_center_of_buoyancy':
        output_data[k] = v[2]
    elif k == 'floatingse.platform_center_of_mass':
        output_data[k] = v[2]
    else:
        pass 

pprint.pprint(output_data)         
            
# hardcode reference values from IEA15MW report
ref_data = {
    'ref_total_platform_mass' : 1.7854E+07,
    'ref_platform_hull_mass' : 3.914E+06,
    'ref_platform_fballast_mass' : 2.54E+06,
    'ref_platform_vballast_mass' : 1.13E+07,
    'ref_platform_CM' : -14.94,
    'ref_platform_CB' : -13.63,
    'ref_platform_I_total' : [1.251E+10, 1.251E+10, 2.367E+10],
    'ref_platform_displacement' : 20206.00,
    }

# calculates differences between reference and outputs
diff_data = {
    'diff_total_platform_mass' : (ref_data['ref_total_platform_mass'] - output_data['floatingse.platform_mass']),
    'diff_platform_hull_mass' : (ref_data['ref_platform_hull_mass'] - output_data['floatingse.platform_hull_mass']),
    'diff_platform_fballast_mass' : (ref_data['ref_platform_fballast_mass'] - output_data['floatingse.platform_ballast_mass']),
    'diff_platform_vballast_mass' : (ref_data['ref_platform_vballast_mass'] - output_data['floatingse.variable_ballast_mass']),
    'diff_platform_CM' : (ref_data['ref_platform_CM']- output_data['floatingse.platform_center_of_mass']),
    'diff_platform_CB' : (ref_data['ref_platform_CB'] - output_data['floatingse.platform_center_of_buoyancy']),
    'diff_platform_I_total' : (ref_data['ref_platform_I_total'] - output_data['floatingse.platform_I_total']),
    'diff_platform_displacement' : (ref_data['ref_platform_displacement'] - output_data['floatingse.platform_displacement'])
    }

pprint.pprint(diff_data)


# output data to excelworksheet
file = 'C:\Users\dpotere\Documents\git\nrel_summer_2021\IEA_15MW_semisub_files\IEA_15MW_semisub_output_comparisons.xlsx'
new_row = [
    output_data['floatingse.platform_mass'],
    None,
    output_data['floatingse.platform_hull_mass'],
    output_data['floatingse.platform_ballast_mass'],
    output_data['floatingse.variable_ballast_mass'],
    output_data['floatingse.platform_center_of_buoyancy'],
    output_data['floatingse.platform_center_of_mass'],
    output_data['floatingse.platform_displacement'],
    output_data['floatingse.platform_I_total'][0],
    output_data['floatingse.platform_I_total'][1],
    output_data['floatingse.platform_I_total'][2]
    ]

wb = openpyxl.load_workbook(filename=file)
ws = wb['fixed_ballast']
row = ws.get_highest_row() + 1

for col, entry in enumerate(new_row, start=1):
    ws.cell(row=row, column=col, value=entry)

wb.save(file)

# set up plotting script for data we want to visualize

# Actually plot data