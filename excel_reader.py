import pandas as pd


class OrderReader:

    def __init__(self):
        self.df = None

    def load(self, filename):
        """
        발주 엑셀 읽기
        """
        self.df = pd.read_excel(filename)

        return self.df

    def summary(self):

        if self.df is None:
            return None

        result = {
            "무농약콩나물": 0,
            "GAP콩나물": 0,
            "GAP숙주나물": 0
        }

        # 컬럼명 자동 찾기
        product_col = None
        qty_col = None

        for col in self.df.columns:

            text = str(col)

            if ("품목" in text) or ("식재료" in text):
                product_col = col

            if ("수량" in text):
                qty_col = col

        if product_col is None:
            raise Exception("품목 컬럼을 찾을 수 없습니다.")

        if qty_col is None:
            raise Exception("수량 컬럼을 찾을 수 없습니다.")

        for _, row in self.df.iterrows():

            product = str(row[product_col])
            qty = float(row[qty_col])

            if "무농약" in product and "콩나물" in product:
                result["무농약콩나물"] += qty

            elif "GAP" in product and "숙주" in product:
                result["GAP숙주나물"] += qty

            elif "GAP" in product and "콩나물" in product:
                result["GAP콩나물"] += qty

        return result
