import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
import assets


def generate_qr():
    content = url_entry.get()

    if not content.strip():
        messagebox.showwarning("Warning", "Please first enter a URL or text")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG File", "*.png")],
        title="Save QR Code as..."
    )

    if not file_path:
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(content)
        qr.make(fit=True)

        img = qr.make_image(fill_color="#1f2933", back_color="white")
        img.save(file_path)

        messagebox.showinfo("Success", "QR Code has been sucessfully generated!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def main():
    global window, url_entry

    window = tk.Tk()
    window.title("QR Code Generator")
    window.iconbitmap("../assets/qrcode.ico")
    window.geometry("420x300")
    window.resizable(False, False)
    window.configure(bg="#1f2933")

    card = tk.Frame(window, bg="#f9fafb", bd=0)
    card.place(relx=0.5, rely=0.5, anchor="center", width=360, height=240)

    title_label = tk.Label(
        card,
        text="QR Code Generator",
        font=("Segoe UI", 16, "bold"),
        bg="#f9fafb",
        fg="#111827"
    )
    title_label.pack(pady=(20, 10))

    desc_label = tk.Label(
        card,
        text="Enter a URL or text",
        font=("Segoe UI", 10),
        bg="#f9fafb",
        fg="#6b7280"
    )
    desc_label.pack(pady=(0, 10))

    url_entry = tk.Entry(
        card,
        font=("Segoe UI", 11),
        width=32,
        bd=1,
        relief="solid"
    )
    url_entry.pack(pady=5, ipady=6)

    generate_button = tk.Button(
        card,
        text="Generate QR Code",
        font=("Segoe UI", 11, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        bd=0,
        padx=20,
        pady=8,
        cursor="hand2",
        command=generate_qr
    )
    generate_button.pack(pady=20)

    window.mainloop()


if __name__ == "__main__":
    main()