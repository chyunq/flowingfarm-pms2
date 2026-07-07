    def make_plan(self):

        if self.order_file == "":
            messagebox.showwarning(
                "알림",
                "발주파일을 선택하세요."
            )
            return

        reader = OrderReader()

        reader.load(self.order_file)

        result = reader.summary()

        calculator = ProductionCalculator()

        plan = calculator.calculate(result)

        self.output.delete(1.0, tk.END)

        self.output.insert(tk.END, "===== 생산계획 =====\n\n")

        for item, info in plan.items():

            self.output.insert(tk.END, f"{item}\n")
            self.output.insert(tk.END, "-" * 30 + "\n")

            self.output.insert(
                tk.END,
                f"주문량 : {info['주문량']} kg\n"
            )

            self.output.insert(
                tk.END,
                f"필요콩 : {info['필요콩']} kg\n"
            )

            self.output.insert(
                tk.END,
                f"월 투입 : {info['월투입']} kg\n"
            )

            self.output.insert(
                tk.END,
                f"수 투입 : {info['수투입']} kg\n"
            )

            self.output.insert(
                tk.END,
                f"금 투입 : {info['금투입']} kg\n\n"
            )
