user_id={    
   101:{"user_name":"Alizay", "email":"alizay@example"},
   102:{"user_name":"Ali", "email":"aliy@example"},
   103:{"user_name":"Faiza", "email":"faiza@example"},
   104:{"user_name":"Rahmen", "email":"Rahmeen2134@example"}
} 

take = int(input("Enter your ID: "))
if take in user_id:
    print(user_id[take].items())
else:
    print("ID not found, please try again.")



# if take in user_id:
#     print(user_id[101].items())
# elif take == 102:
#     print(user_id[102].items())
# elif take == 103:       
#     print(user_id[103].items())
# elif take == 104:
#     print(user_id[104].items())
# else:
#     print("ID not found, please try again.")    




# if take == 101:
#    print(user_id[101].items())
# elif take == 102:
#     print(user_id[102].get("user_name"), user_id[102].get("email"))
# elif take == 103:
#     print(user_id[103].get("user_name"), user_id[103].get("email"))
# elif take == 104:
#     print(user_id[104].get("user_name"), user_id[104].get("email"))
# else:
#     print("ID not found, please try again.")







# take = input("Enter your ID: ")
# if take == "AF23":
#     print(AF23.get("user_name"),  AF23.get("email"))
# elif take == "AF24":
#     print(AF24.get("user_name"),  AF23.get("email"))
# elif take == "AF25":
#     print(AF25.get("user_name"),  AF23.get("email"))
# elif take == "AF26":
#     print(AF26.get("user_name"),  AF23.get("email"))
# else:
#     print("ID not found, please try again.")



