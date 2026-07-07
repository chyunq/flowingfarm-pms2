import tkinter as tk
from tkinter import ttk, filedialog, messagebox


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

        self.output.delete(1.0, tk.END)

        self.output.insert(tk.END, "=" * 60 + "\n")
        self.output.insert(tk.END, "플로잉팜 생산관리\n")
        self.output.insert(tk.END, "=" * 60 + "\n\n")

        self.output.insert(
            tk.END,
            f"선택된 발주파일\n\n{self.order_file}\n\n"
        )

        self.output.insert(
            tk.END,
            "다음 버전에서 자동으로\n"
        )

        self.output.insert(
            tk.END,
            "- 무농약콩나물 집계\n"
        )

        self.output.insert(
            tk.END,
            "- GAP콩나물 집계\n"
        )

        self.output.insert(
            tk.END,
            "- GAP숙주 집계\n"
        )

        self.output.insert(
            tk.END,
            "- 콩 필요량 계산\n"
        )

        self.output.insert(
            tk.END,
            "- 생산계획 엑셀 생성\n"
        )

        self.output.insert(
            tk.END,
            "기능이 연결됩니다.\n"
        )


def main():

    root = tk.Tk()

    FlowingFarmApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
