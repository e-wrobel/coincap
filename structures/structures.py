AssetStructure = {
    "id": None,  # unique identifier for asset,
    "rank": None,  # rank is in ascending order - this number is directly associated with the marketcap whereas
    # the highest marketcap receives rank 1

    "symbol": None,  # most common symbol used to identify this asset on an exchange
    "name": None,  # proper name for asset
    "supply": None,  # available supply for trading
    "maxSupply": None,  # total quantity of asset issued
    "marketCapUsd": None,  # supply x price
    "volumeUsd24Hr": None,  # quantity of trading volume represented in USD over the last 24 hours
    "priceUsd": None,  # volume-weighted price based on real-time market data, translated to USD
    "changePercent24Hr": None,  # the direction and value change in the last 24 hours
    "vwap24Hr": None  # Volume Weighted Average Price in the last 24 hours
}

AssetHistoryStructure = {
    "priceUsd": None,  # volume - weighted price based on real - time market data, translated to USD
    "time": None  # timestamp in UNIX in milliseconds
}

AssetByMarketStructure = {
    "exchangeId": None,  # unique identifier for exchange
    "baseId": None,  # unique identifier for this asset, base is asset purchased
    "quoteId": None,  # unique identifier for this asset, quote is asset used to purchase based
    "baseSymbol": None,  # most common symbol used to identify asset, base is asset purchased
    "quoteSymbol": None,  # most common symbol used to identify asset, quote is asset used to purchase base
    "volumeUsd24Hr": None,  # volume transacted on this market in last 24 hours
    "priceUsd": None,  # the amount of quote asset traded for one unit of base asset
    "volumePercent": None  # percent of quote asset volume
}

RateStructure = {
    "id": None,  # unique identifier for asset or fiat
    "symbol": None,  # most common symbol used to identify asset or fiat
    "currencySymbol": None,  # currency symbol used to identify asset or fiat
    "rateUsd": None,  # rate conversion to USD
    "type": None  # type of currency - fiat or crypto
}

ExchangeStructure = {
    "id": None,  # unique identifier for exchange
    "name": None,  # proper name of exchange
    "rank": None,  # rank is in ascending order - this number is directly associated with the total exchange volume
    # whereas the highest volume exchange receives rank 1

    "percentTotalVolume": None,  # the amount of daily volume a single exchange transacts in relation to total
    # daily volume of all exchanges

    "volumeUsd": None,  # daily volume represented in USD
    "tradingPairs": None,  # number of trading pairs (or markets) offered by exchange
    "socket": None,  # true/false, true = trade socket available, false = trade socket unavailable
    "exchangeUrl": None,  # website to exchange
    "updated": None,  # UNIX timestamp (milliseconds) since information was received from this exchange
}

MarketsStructure = {
    "exchangeId": None,  # unique identifier for exchange
    "rank": None,  # rank is in ascending order - this number represents the amount of volume transacted by this
    # market in relation to other markets on that exchange

    "baseSymbol": None,  # most common symbol used to identify asset, base is asset purchased
    "baseId": None,  # unique identifier for this asset, base is asset purchased
    "quoteSymbol": None,  # most common symbol used to identify asset, quote is asset used to purchase base
    "quoteId": None,  # unique identifier for this asset, quote is asset used to purchase base
    "priceQuote": None,  # the amount of quote asset traded for one unit of base asset
    "priceUsd": None,  # quote price translated to USD
    "volumeUsd24Hr": None,  # volume transacted on this market in last 24 hours
    "percentExchangeVolume": None,  # the amount of daily volume a single market transacts in relation to total
    # daily volume of all markets on the exchange

    "tradesCount24Hr": None,  # number of trades on this market in the last 24 hours
    "updated": None,  # UNIX timestamp (milliseconds) since information was received from this particular market
}

CandlesStructure = {
    "open": None,  # the price (quote) at which the first transaction was completed in a given time period
    "high": None,  # the top price (quote) at which the base was traded during the time period
    "low": None,  # the bottom price (quote) at which the base was traded during the time period
    "close": None,  # the price (quote) at which the last transaction was completed in a given time period
    "volume": None,  # the amount of base asset traded in the given time period
    "period": None  # timestamp for starting of that time period, represented in UNIX milliseconds
}
