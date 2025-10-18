#In automation, you often compare expected and actual outputs.
#Write code to check if a test case passed or failed.

#expected_title = "Dashboard"
#actual_title = "Dashboard "
#✅ Test Passed – Title matches

actual_title = input("Enter actual title: ").strip()
expected_title = input("Enter expected title: ").strip()
if expected_title.lower() == actual_title.lower():
    print("Title Matches -Passed")
else:
    print("Title doesn't Matches -Failed")