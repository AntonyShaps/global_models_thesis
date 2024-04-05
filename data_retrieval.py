from binance_historical_data import BinanceDataDumper
import datetime as dt

#defining time period variables
start = dt.date(year = 2022, month = 12, day = 29)
end = dt.date(year = 2024, month = 1, day = 1)


#initialzise data dumper object from BinanceDataDumper
data_dumper = BinanceDataDumper(
    path_dir_where_to_dump="./data",
    asset_class="spot",
    data_type="klines",
    data_frequency="1h"
)

#calling dump_data method to retrieve data
data_dumper.dump_data(
    date_start=start,
    date_end=end,
    is_to_update_existing=False,
    tickers_to_exclude=None,
)