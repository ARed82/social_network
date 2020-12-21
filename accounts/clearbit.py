import clearbit

from social_network.settings import CLEARBIT_KEY


class Clearbit():
    def __init__(self, email):
        self.clearbit = clearbit
        self.clearbit.key = CLEARBIT_KEY
        self.email = email

    def enrichment_api(self):
        return self.clearbit.Enrichment.find(email=self.email, stream=True)
