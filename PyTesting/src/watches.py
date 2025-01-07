class watchCollection:

    def __init__(self, name:str, watches=None):
        self.name = str(name) if name != None else "None"

        self.collection_value = 0
        self.cashflow = 0
        self.watch_id = 0000

        # tmp
        self.watches = {}

        # if watches is None:
        #     self.watches = {}
        # else:
        #     self._validate_watches(watches)
        #     self.watches = watches

    def purchase_watch(self, brand, model, price, year=None, serial_num=None) -> dict:
        self.watches[self.watch_id + 1] = dict(brand=brand, model=model, price=price, year=year, serial_num=serial_num)

        self.cash_flow -= price

        self.collection_value = price * 1.5 if brand == "Rolex" else price * .95

    def trade_in(self):
        pass

    def sell_watch(self):
        pass

    def add_watch(self, gift=True):
        pass

    def update_watch_valuation(self, watch_id, value_change):
        self.watches[watch_id]["price"] = self.watches[watch_id]["price"] + value_change

    # def _validate_watches():
    #     pass