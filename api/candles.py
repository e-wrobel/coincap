import requests

from coincap import Coincap
from structures.structures import CandlesStructure


class Candles(Coincap):

    def get_candles(self, exchange, interval, baseID, quoteID, start=None, end=None):
        """

        The /candles endpoint offers a look into how a market has performed historically. This data is represented in
        OHLCV candles - Open, High, Low, Close, and Volume. Please note that many parameters are required to request
        candles for a specific market. Candle history goes back to the inception of an exchange - you may even find
        data for exchanges that have come and gone.


        :param exchange: exchange id (poloniex)
        :param interval: candle interval (m1, m5, m15, m30, h1, h2, h4, h8, h12, d1, w1)
        :param baseID: base id (ethereum)
        :param quoteID: quote id (bitcoin)
        :param start: UNIX time in milliseconds. omiting will return the most recent candles
        :param end: UNIX time in milliseconds. omiting will return the most recent candles

        :return: [CandlesStructure]
        :rtype: list()
        """

        if start is None or end is None:
            url = self.url + "/candles?exchange=" + exchange + "&interval=" + interval + \
                  "&baseId=" + baseID + "&quoteId=" + quoteID

        else:
            url = self.url + "/candles?exchange=" + exchange + "&interval=" + interval + \
                  "&baseId=" + baseID + "&quoteId=" + quoteID + "&start=" + start + "&end=" + end

        resp = requests.get(url)

        if resp.status_code < 300:
            return resp.json()["data"]

        return [CandlesStructure]
