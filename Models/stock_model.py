class Stock:
    def __init__(self, symbol, price, timestamp):
        self.symbol = symbol
        self.price = price
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'price': self.price,
            'timestamp': self.timestamp
        }
