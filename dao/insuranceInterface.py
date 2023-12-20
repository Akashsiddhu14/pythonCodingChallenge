from entity import interface

object = interface.DBConnection
conn = object.getConnection()

class InsuranceServiceImpl:

    def createPolicy(self):
        query = "INSERT INTO Claim(claimId, claimNumber, dateFiled, claimAmount, status, policy, client) VALUES (4, 222, '2019-8-23', 1100, 'OPEN', 'Health', 'Lebron')"
        cursor = conn.cursor()

        try:
            cursor.execute(query)
            conn.commit()
            return "Policy created successfully"

        except Exception as e:
            conn.rollback()
            return f"Error creating policy: {str(e)}"

        finally:
            cursor.close()

    def getPolicy(self, claimNumber):
        string_del = f'SELECT * FROM claim WHERE claimNumber = {claimNumber}'
        cursor = conn.cursor()

        try:
            cursor.execute(string_del)
            result = cursor.fetchall()
            return result

        finally:
            cursor.close()

    def getAllPolicies(self):
        string_del = 'SELECT * FROM claim'
        cursor = conn.cursor()

        try:
            cursor.execute(string_del)
            result = cursor.fetchall()
            return result

        finally:
            cursor.close()

    def updatePolicy(self,status, policy):
        cursor = conn.cursor()
        try:
            update_query = f"UPDATE claim SET status = {status}  WHERE policy = {policy}"
            cursor.execute(update_query)
            conn.commit()

            print(f"Policy '{policy}' updated with status: {status}")
        except Exception as e:

            print(f"Error updating policy: {e}")
        finally:
            # Close the cursor
            cursor.close()



    def deletePolicy(self, policyId):
        string_del = f"DELETE FROM claim WHERE policy = '{policyId}';"
        print(string_del)

        cursor = conn.cursor()

        try:
            cursor.execute(string_del)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
