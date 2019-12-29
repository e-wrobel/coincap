import requests

from coincap import Coincap
from structures.structures import ExchangeStructure


class Exchanges(Coincap):

    def get_exchanges(self):
        """
        The /exchanges endpoint offers an understanding into the where cryptocurrency is being exchanged and offers
        high-level information on those exchanges. CoinCap strives to provide transparency in the recency of our
        exchange data. For that purpose you will find an "updated" key for each exchange. For more details into
        coin pairs and volume, see the /markets endpoint.

        :return: [ExchangeStructure]
        :rtype: list()
        """

        url = self.url + "/exchanges"
        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return [ExchangeStructure]

    def get_exchange_by_id(self, id):
        """
        The /exchanges endpoint offers an understanding into the where cryptocurrency is being exchanged and offers
        high-level information on those exchanges. CoinCap strives to provide transparency in the recency of our
        exchange data. For that purpose you will find an "updated" key for each exchange. For more details into
        coin pairs and volume, see the /markets endpoint. This returns exchange by ID.

        :param id: currency ID

        :return: ExchangeStructure

        :rtype: dict()
        """

        url = self.url + "/exchanges/" + id

        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return ExchangeStructure
