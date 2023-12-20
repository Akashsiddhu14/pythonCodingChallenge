class Claim:
    def __init__(self, claimId, claimNumber, dateFiled, claimAmount, status, policy, client):
        self._claimId = claimId
        self._claimNumber = claimNumber
        self._dateFiled = dateFiled
        self._claimAmount = claimAmount
        self._status = status
        self._policy = policy
        self._client = client

    def getClaimId(self):
        return self._claimId

    def getClaimNumber(self):
        return self._claimNumber

    def getDateFiled(self):
        return self._dateFiled

    def getClaimAmount(self):
        return self._claimAmount

    def getStatus(self):
        return self._status

    def getPolicy(self):
        return self._policy

    def getClient(self):
        return self._client

    def setClaimId(self, claimId):
        self._claimId = claimId

    def setClaimNumber(self, claimNumber):
        self._claimNumber = claimNumber

    def setDateFiled(self, dateFiled):
        self._dateFiled = dateFiled

    def setClaimAmount(self, claimAmount):
        self._claimAmount = claimAmount

    def setStatus(self, status):
        self._status = status

    def setPolicy(self, policy):
        self._policy = policy

    def setClient(self, client):
        self._client = client