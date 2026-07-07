class ProductionCalculator:

    def __init__(self):

        self.yield_rate = {
            "무농약콩나물": 4,
            "GAP콩나물": 6,
            "GAP숙주나물": 10
        }

    def calculate(self, orders):

        result = {}

        for item, qty in orders.items():

            bean = qty / self.yield_rate[item]

            result[item] = {

                "주문량": qty,

                "필요콩": round(bean, 1),

                "월투입": round(bean * 0.40, 1),

                "수투입": round(bean * 0.35, 1),

                "금투입": round(bean * 0.25, 1)

            }

        return result
