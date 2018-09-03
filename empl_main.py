import empl

def main():
    
   employee1=input().split()
   employee2=input().split()
   employee3=input().split()
   
   j1=empl.Employee(employee1[0],employee1[1],employee1[2],employee1[3])
   j2=empl.Employee(employee2[0],employee2[1],employee2[2],employee2[3])
   j3=empl.Employee(employee3[0],employee3[1],employee3[2],employee3[3])
   
   
   print('--'*20)
   print('Name',' ','ID Number', ' ', 'Department', ' ', 'Job Title')
   print('--'*20)
   print(j1.get_name(),' '*5,j1.get_ID_number(),' '*5, j1.get_department(),' '*5,j1.get_job_title())
   print(j2.get_name(),' '*5,j2.get_ID_number(),' '*5, j2.get_department(),' '*5,j2.get_job_title())
   print(j3.get_name(),' '*5,j3.get_ID_number(),' '*5, j3.get_department(),' '*5,j3.get_job_title())
    
   
    
main()
