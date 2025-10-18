#You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.

#I/P response = 404 , O/P ❌ Failed API Request
#I/P response = 200 , O/P ✅ Passed API Request

API_Check=int(input("Enter your response code "))
if API_Check==200:
    print("✅ Passed API Request",200)
elif API_Check==404:
    print("❌ Failed API Request",404)
else:
    print("Enter valid response code")