FH = open("pwd.txt", 'r')
all_lines = FH.readlines()
pwd = dict()

for line in all_lines:
    parts = line.strip().split(':')

    user = parts[0]    
    user_id = int(parts[2])
    real_name = parts[4]
    home = parts[5]
    pwd[user]= [user_id, real_name, home]

print("users in ascending order:")
users = sorted(pwd, key = lambda x:x[1], reverse = False)

for user in users:
    info = pwd[user]
    print("User ID:", info[0])
    print("Real Name:", info[1])
    print("Home Directory:", info[2])

    print()
