import tkinter as tk
from decimal import Decimal, getcontext, DivisionByZero, InvalidOperation

getcontext().prec = 55

def calculate():
    try:
        num1 = Decimal(entry_num1.get())
        num2 = Decimal(entry_num2.get())
        op = operation.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            label_result.config(text="اختار عملية صحيحة")
            return

        result_str = format(result, f'.50f')
        label_result.config(text=f"الناتج:\n{result_str}")

    except DivisionByZero:
        label_result.config(text="خطأ: القسمة على صفر ممنوعة")
    except InvalidOperation:
        label_result.config(text="خطأ: أدخل أرقام صحيحة")
    except Exception as e:
        label_result.config(text=f"خطأ: {str(e)}")

def paste_num1():
    try:
        clipboard = root.clipboard_get()
        entry_num1.delete(0, tk.END)
        entry_num1.insert(0, clipboard)
    except:
        pass

def paste_num2():
    try:
        clipboard = root.clipboard_get()
        entry_num2.delete(0, tk.END)
        entry_num2.insert(0, clipboard)
    except:
        pass

def copy_result():
    result_text = label_result.cget("text").replace("الناتج:\n", "")
    root.clipboard_clear()
    root.clipboard_append(result_text)

root = tk.Tk()
root.title("حاسبة بدقة 50 رقم عشري")

tk.Label(root, text="الرقم الأول:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root, width=40)
entry_num1.grid(row=0, column=1, padx=10, pady=5)
btn_paste1 = tk.Button(root, text="لصق", command=paste_num1)
btn_paste1.grid(row=0, column=2, padx=5)

tk.Label(root, text="الرقم الثاني:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root, width=40)
entry_num2.grid(row=1, column=1, padx=10, pady=5)
btn_paste2 = tk.Button(root, text="لصق", command=paste_num2)
btn_paste2.grid(row=1, column=2, padx=5)

tk.Label(root, text="اختر العملية:").grid(row=2, column=0, padx=10, pady=5)
operation = tk.StringVar(root)
operation.set('+')
options = ['+', '-', '*', '/']
dropdown = tk.OptionMenu(root, operation, *options)
dropdown.grid(row=2, column=1, padx=10, pady=5, sticky='w')

btn_calc = tk.Button(root, text="احسب", command=calculate)
btn_calc.grid(row=3, column=0, columnspan=3, pady=10)

label_result = tk.Label(root, text="الناتج هنا", justify='left')
label_result.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

btn_copy = tk.Button(root, text="نسخ النتيجة", command=copy_result)
btn_copy.grid(row=5, column=0, columnspan=3, pady=5)

root.mainloop()
