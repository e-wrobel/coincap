from api.assets import Assets
from api.rates import Rates

if __name__ == '__main__':
    main_url = "https://api.coincap.io/v2"
    a = Assets(main_url).get_assets()

    print("Get all assets data: {}".format(a))

    b = Rates(main_url)
    d = b.get_rate_by_id("bitcoin")

    print(d)
