import data_personal

def main():
    
    my_i=input().split()
    fr_i=input().split()
    fam_i=input().split()
        
    my_infor=data_personal.Data(my_i[0],my_i[1],my_i[2],my_i[3])
    friend_infor=data_personal.Data(fr_i[0],fr_i[1],fr_i[2],fr_i[3])
    family_infor=data_personal.Data(fam_i[0],fam_i[1],fam_i[2],fam_i[3])
    
    print('My information: ')
    print('Name: ', my_infor.get_name())
    print('Address: ', my_infor.get_address())
    print('Age: ', my_infor.get_age())
    print('Phone number: ', my_infor.get_phone_number())
    
    print('Friend"s information: ')
    print('Name: ',friend_infor.get_name())
    print('Address: ',friend_infor.get_address())
    print('Age: ',friend_infor.get_age())
    print('Phone number: ',friend_infor.get_phone_number())
    
    print('Family"s information: ')
    print('Name: ', family_infor.get_name())
    print('Address: ',family_infor.get_address())
    print('Age: ',family_infor.get_age())
    print('Phone number: ', family_infor.get_phone_number())
main()
