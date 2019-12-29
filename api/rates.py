import requests

from coincap import Coincap
from structures.structures import RateStructure


class Rates(Coincap):

    def get_rates(self):
        """
        All prices on the CoinCap API are standardized in USD (United States Dollar). To make translating to other
        values easy, CoinCap now offers a Rates endpoint. We offer fiat and top cryptocurrency translated rates.
        Fiat rates are available through OpenExchangeRates.org.

        :return: [RateStructure]
        :rtype: list()
        """

        url = self.url + "/rates"
        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return [RateStructure]

    def get_rate_by_id(self, id):
        """
        The asset price is a volume-weighted average calculated by collecting ticker data from exchanges. Each exchange
        contributes to this price in relation to their volume, meaning higher volume exchanges have more affect on this
        global price. All values are translated into USD (United States Dollar) and can be translated into other units
        of measurement through the /rates endpoint. Data are gathered for given currency.

        :param id: currency ID

        :return: RateStructure

        :rtype: dict()
        """

        url = self.url + "/rates/" + id

        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return RateStructure

