import settrade.openapi
from settrade.openapi import Investor

############################# login #############################
investor = Investor(
    app_id="8uuaMP1npccDixrg",    
    app_secret="APX6wnqzk/yoVLIRyQ4ps4Fm13uzbC4tL5nyjAwwCKue",
    app_code="SANDBOX",
    broker_id="SANDBOX",
    is_auto_queue=False)

############################# Derivative #############################
deri = investor.Derivatives(account_no = "settrade-D")

deri.place_order(symbol="S50M22",
    price=950,
    volume=13,
    side="SHORT",
    position="AUTO",
    pin="000000", 
    price_type="LIMIT",
    validity_type="GOOD_TILL_DAY")