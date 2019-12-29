import requests

from coincap import Coincap
from structures.structures import MarketsStructure


class Exchanges(Coincap):

    def get_markets(self):
        """
        Take a closer look into exchanges with the /markets endpoint. Similar to the /exchanges endpoint, we strive
        to offer transparency into how real-time our data is with a key identifying when the market was last updated.
        For a historical view on how a market has performed, see the /candles endpoint. All market data represents
        actual trades processed, orders on an exchange are not represented. Data received from individual markets is
        used to calculate the current price of an asset.

        :return: [MarketsStructure]
        :rtype: list()
        """

        url = self.url + "/markets"
        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return [MarketsStructure]
