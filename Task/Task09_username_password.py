#Check if the user can log in based on correct username and password.
# I/P - username = "admin" password = "1234"
# O/P - ✅ Login Successful
# O/P - For the Fail condition Other O/P = ❌ Invalid Credentials

Username = input("Enter username: ").strip()
Password = input("Enter password: ").strip()
if Username =="admin" and Password == "1234":
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")