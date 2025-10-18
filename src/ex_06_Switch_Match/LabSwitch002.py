print("Enter which test you want to run")
test_type = input("Enter test type: API,UI,Performance,Security ")

match test_type:
    case "API":
        print("We are running API test ")
    case "UI":
        print("We are running UI test ")
    case "Performance":
        print("We are running Performance test ")
    case "Security":
        print("We are running Security test ")
    case _:
        print("Invalid test type")

# test_type = input("Enter test type: ").strip()
# if test_type == "API":
#     print("We are running API test ")
# elif test_type == "UI":
#     print("We are running UI test ")
# elif test_type == "Performance":
#     print("We are running Performance test ")
# elif test_type == "Security":
#     print("We are running Security test ")
# else:
#     print("Invalid test type")