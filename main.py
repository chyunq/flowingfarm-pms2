import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from excel_reader import OrderReader

class FlowingFarmApp:

    def __init__(self, root):

        self.root = root
        self.root.title("FlowingFarm PMS")
        self.root.geometry("800x600")

        self.order_file = ""

        self.make_ui()

    def make_ui(self):

        title = tk.Label(
            self.root,
            text="플로잉팜 생산관리",
            font=("맑은 고딕", 22, "bold")
        )

        title.pack(pady=20)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.path = tk.StringVar()

        entry = ttk.Entry(
            frame,
            width=70,
            textvariable=self.path
        )

        entry.grid(row=0, column=0, padx=5)

        ttk.Button(
            frame,
            text="발주파일 선택",
            command=self.select_file
        ).grid(row=0, column=1)

        ttk.Separator(self.root).pack(fill="x", pady=15)

        self.output = tk.Text(
            self.root,
            width=90,
            height=20,
            font=("Consolas", 11)
        )

        self.output.pack()

        ttk.Button(
            self.root,
            text="생산계획 생성",
            command=self.make_plan
        ).pack(pady=15)

    def select_file(self):

        filename = filedialog.askopenfilename(

            title="발주파일 선택",

            filetypes=[
                ("Excel", "*.xlsx"),
                ("Excel", "*.xls")
            ]

        )

        if filename:

            self.order_file = filename
            self.path.set(filename)

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

self.output.delete(1.0, tk.END)

self.output.insert(tk.END, "===== 주문 집계 =====\n\n")

self.output.insert(
    tk.END,
    f"무농약콩나물 : {result['무농약콩나물']:.1f} kg\n"
)

self.output.insert(
    tk.END,
    f"GAP콩나물 : {result['GAP콩나물']:.1f} kg\n"
)

self.output.insert(
    tk.END,
    f"GAP숙주나물 : {result['GAP숙주나물']:.1f} kg\n"
)


def main():

    root = tk.Tk()

    FlowingFarmApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
