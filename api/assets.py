import requests

from coincap import Coincap
from structures.structures import AssetStructure, AssetHistoryStructure, AssetByMarketStructure


class Assets(Coincap):

    def get_assets(self):
        """
        The asset price is a volume-weighted average calculated by collecting ticker data from exchanges. Each exchange
        contributes to this price in relation to their volume, meaning higher volume exchanges have more affect on this
        global price. All values are translated into USD (United States Dollar) and can be translated into other units
        of measurement through the /rates endpoint.

        :return: [AssetStructure]
        :rtype: list()
        """

        url = self.url + "/assets"
        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return [AssetStructure]

    def get_asset(self, id):
        """
        The asset price is a volume-weighted average calculated by collecting ticker data from exchanges. Each exchange
        contributes to this price in relation to their volume, meaning higher volume exchanges have more affect on this
        global price. All values are translated into USD (United States Dollar) and can be translated into other units
        of measurement through the /rates endpoint. Data are gathered for given currency.

        :param id: currency ID

        :return: AssetStructure

        :rtype: dict()
        """

        url = self.url + "/assets/" + id

        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return AssetStructure

    def get_asset_history(self, id, interval):
        """
        The asset price is a volume-weighted average calculated by collecting ticker data from exchanges. Each exchange
        contributes to this price in relation to their volume, meaning higher volume exchanges have more affect on this
        global price. All values are translated into USD (United States Dollar) and can be translated into other units
        of measurement through the /rates endpoint. Data are gathered for given currency and interval.

        :param id: currency ID
        :param interval: m1, m5, m15, m30, h1, h2, h6, h12, d1

        :return: AssetStructure

        :rtype: dict()
        """

        url = self.url + "/assets/" + id +"/history?interval=" + interval

        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return AssetHistoryStructure

    def get_asset_by_market(self, id):
        """
        The asset price is a volume-weighted average calculated by collecting ticker data from exchanges. Each exchange
        contributes to this price in relation to their volume, meaning higher volume exchanges have more affect on this
        global price. All values are translated into USD (United States Dollar) and can be translated into other units
        of measurement through the /rates endpoint. Data are gathered for given currency and interval.

        :param id: currency ID

        :return: [AssetByMarketStructure]
        :rtype: dict()
        """

        url = self.url + "/assets/" + id + "/markets"

        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return [AssetByMarketStructure]
