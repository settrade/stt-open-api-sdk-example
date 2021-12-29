import settrade.openapi
from settrade.openapi import Investor

############################# login #############################
investor = Investor(
    app_id="8uuaMP1npccDixrg",    
    app_secret="APX6wnqzk/yoVLIRyQ4ps4Fm13uzbC4tL5nyjAwwCKue",
    app_code="SANDBOX",
    broker_id="SANDBOX",
    is_auto_queue=False)

############################# Equity #############################
equity = investor.Equity(account_no="settrade-E")

equity.place_order(
    symbol="PTT",
    price=38,
    volume=100,
    side="BUY",
    pin="000000")