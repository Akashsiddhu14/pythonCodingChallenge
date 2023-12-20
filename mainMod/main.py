from dao import insuranceInterface


class mainMod:
    object=insuranceInterface.InsuranceServiceImpl()
    user_input = input("Enter which function you want to execute = ")
    if user_input == 'createPolicy':
        result = object.createPolicy()
        print(result)
    elif user_input == 'getPolicy':
        claimNumber = int(input("Enter claimNumber To Get Policy Result = "))
        result = object.getPolicy(claimNumber)
        print(result)
    elif user_input == 'getAllPolicies':
        getAllPolicies = (input("Enter claimNumber  to get Policy =  "))
        result = object.getAllPolicies()
        print(result)
    else:
        print('Entered Invalid Input')

