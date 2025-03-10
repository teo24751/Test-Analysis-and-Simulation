import numpy as np
import main
import readData

#Initial values
width=1
crack_lengths=np.array(range(1,10))
loads=np.array([11,12,13,14,17,20,36,45,77,80])
displacements=np.array(range(20,30))
x=crack_lengths/width


#Linearization of the load-displacement curve
#Only a part of the data falls on the linear part of the curve - LS regression
initial_linear_index=2
final_linear_index=8

print(loads)
print(displacements)
new_loads=loads[initial_linear_index:final_linear_index]
new_displacements=displacements[initial_linear_index:final_linear_index]
print(new_loads)
print(new_displacements)

matrix=np.matrix([[final_linear_index-initial_linear_index,np.sum(new_displacements)],[np.sum(new_displacements),np.sum(new_displacements**2)]])
print(matrix)
vector_values=np.matrix([[np.sum(new_loads)],[np.sum(new_loads*new_displacements)]])
line_parameters=np.dot(np.linalg.inv(matrix),vector_values)
print('Line parameters: ', line_parameters)

offset_line_parameters=np.matrix([[line_parameters[0,0]],[line_parameters[1,0]/1.05]])
print('Offset line parameters: ',offset_line_parameters)
linearized_loads=offset_line_parameters[0,0]+offset_line_parameters[1,0]*displacements
print('Linearized loads',linearized_loads)
differences=loads-linearized_loads
differences=list(differences)[1:]
print(differences)

intersection_point_index=differences.index(min(differences))
intersection_load=loads[intersection_point_index]
intersection_displacement=displacements[intersection_point_index]
print(intersection_load)

print(readData.load_displacement_curve(3))

#Now the appropriate load has to be determined:
if intersection_load/max(loads)>1.1:
    print('The test is invalid!')
elif intersection_displacement:

else:
    P_Q=intersection_load
P_Q=intersection_load
