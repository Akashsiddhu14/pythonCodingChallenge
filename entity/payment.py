class Payment:
    def __init__(self, paymentId, paymentDate, paymentAmount, client):
        self._paymentId = paymentId
        self._paymentDate = paymentDate
        self._paymentAmount = paymentAmount
        self._client = client

    def getPaymentId(self):
        return self._paymentId

    def getPaymentDate(self):
        return self._paymentDate

    def getPaymentAmount(self):
        return self._paymentAmount

    def getClient(self):
        return self._client

    def setPaymentId(self, paymentId):
        self._paymentId = paymentId

    def setPaymentDate(self, paymentDate):
        self._paymentDate = paymentDate

    def setPaymentAmount(self, paymentAmount):
        self._paymentAmount = paymentAmount

    def setClient(self, client):
        self._client = client

