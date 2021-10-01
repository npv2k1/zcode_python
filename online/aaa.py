
# # current_alien_color='green'
# # if current_alien_color == 'green':
# #     print("You just earned 5 points!")
# # else:
# #     print("You just earned 10 points!")

# # current_alien_color='red'
# # if current_alien_color == 'green':
# #     print("You just earned 5 points!")
# # else:
# #     print("You just earned 10 points!")


# while True:
#     gpa = float(input())
#     if gpa == 0:
#         break
#     if gpa >= 3.6:
#         print("Xuat sac")
#     elif gpa >= 3.2 :
#         print("Gioi")
#     elif gpa >= 2.5:
#         print("Kha")
#     elif gpa >= 2.0:
#         print('Trung binh')
#     else:
#         print('Khong dat yeu cau')



# print('-'*10)
# # game loop
# while True:
#     current_alien_color = input()
#     if(current_alien_color == '0'):
#         break
#     if current_alien_color == 'green':
#         print("You just earned 5 points!")
#     if current_alien_color == 'yellow':
#         print("You just earned 10 points!")
#     if current_alien_color == 'red':
#         print("You just earned 15 points!")



# print('-'*10)
# favorite_fruits = ['chuoi', 'cam', 'tao','xoai','oi']
# fruit = 'chuoi'
# if fruit in favorite_fruits:
#     print('You really like',fruit)

# a=[]
# for i in a:
#     print(i)


current_users = ['admin', 'an', 'hai', 'nguyen', 'ha']
for user in current_users:
    if (user == 'admin'):
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello", user, ", thank you for logging in again.")

current_users=[]
if(len(current_users)==0):
    print("We need to find some user")





current_users = ['admin', 'an', 'hai', 'nguyen', 'ha']
new_users = ['nguyen','linh','hoang','minh','nhat']
for new_user in new_users:
    if new_user in current_users:
        print(new_user + " is already taken")
    else:
        print(new_user + " is available")


new_users = ['Nguyen','Linh','hoang','minh','nhat']    
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " is already taken")
    else:
        print(new_user + " is available")
    
