class PolicyNotFoundException(Exception):
    def __init__(self, message="Policy not found"):
        self.message = message
        super().__init__(self.message)

class YourClass:
    def __init__(self):
        # Your class initialization code here
        self.policies = {"policy1": "Details for Policy 1", "policy2": "Details for Policy 2"}

    def updatePolicy(self, policy_name, new_details):
        if policy_name not in self.policies:
            raise PolicyNotFoundException(f"Policy '{policy_name}' not found")

        # Your update policy logic goes here
        # For example, update the policy details
        self.policies[policy_name] = new_details
        print(f"Policy '{policy_name}' updated with details: {new_details}")


# Create an instance of YourClass
your_instance = YourClass()

try:
    # Try to update a policy
    your_instance.updatePolicy("Health", "New Details for Policy 3")
except PolicyNotFoundException as e:
    # Handle the custom exception
    print(f"Exception: {e}")

