registered = input()
fee_paid = input()
identity_verified = input()
system_check = input()

# Check whether the student can access the online exam
if registered == "Yes":
    if fee_paid == "Yes" and identity_verified == "Yes":
        if system_check == "Pass":
            print("Access Granted")
        else:
            print("Access Denied: System Check Failed")
    else:
        print("Access Denied: Verification Pending")
else:
    print("Access Denied: Registration Incomplete")