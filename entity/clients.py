class Clients:
    def __init__(self, clientId, clientName, contactInfo, policy):
        self._clientId = clientId
        self._clientName = clientName
        self._contactInfo = contactInfo
        self._policy = policy

    def getClientId(self):
        return self._clientId

    def getClientName(self):
        return self._clientName

    def getContactInfo(self):
        return self._contactInfo

    def getPolicy(self):
        return self._policy

    def setClientId(self, clientId):
        self._clientId = clientId

    def setClientName(self, clientName):
        self._clientName = clientName

    def setContactInfo(self, contactInfo):
        self._contactInfo = contactInfo

    def setPolicy(self, policy):
        self._policy = policy
