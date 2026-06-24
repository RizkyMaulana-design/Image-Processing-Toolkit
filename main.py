"""
=========================================================
PROJECT UAS PENGOLAHAN CITRA DIGITAL
=========================================================
Nama        : Rizky Maulana
NIM         : 312410430
Kelas       : I241C
Dosen       : Donny Maulana, S.Kom., M.M.S.I.
Deskripsi   : Implementasi GUI untuk 5 Tahap Pengolahan Citra
              dengan Fitur Save Image Otomatis
=========================================================
"""

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PIL import Image, ImageTk

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pengolahan Citra - UAS")
        self.root.geometry("1000x650")
        self.root.configure(bg="#1E1E1E")

        self.cv_image = None
        self.processed_image = None
        self.current_filename = "image.jpg"
        self.current_process = "original"

        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Label(self.root, text="UAS PENGOLAHAN CITRA DIGITAL", font=("Helvetica", 16, "bold"), bg="#1E1E1E", fg="#FFFFFF")
        header.pack(pady=15)

        # Main Frame
        main_frame = tk.Frame(self.root, bg="#1E1E1E")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Image Display Area (Original vs Processed)
        self.img_frame = tk.Frame(main_frame, bg="#2D2D2D", bd=2, relief=tk.FLAT)
        self.img_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        self.lbl_original = tk.Label(self.img_frame, text="Original Image", bg="#2D2D2D", fg="#AAAAAA")
        self.lbl_original.pack(side=tk.LEFT, padx=10, expand=True)

        self.lbl_processed = tk.Label(self.img_frame, text="Processed Image", bg="#2D2D2D", fg="#AAAAAA")
        self.lbl_processed.pack(side=tk.RIGHT, padx=10, expand=True)

        # Control Panel Area
        control_frame = tk.Frame(main_frame, bg="#1E1E1E", width=250)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        # Buttons (Styled with flat dark look)
        btn_style = {"bg": "#3A3A3A", "fg": "#FFFFFF", "font": ("Helvetica", 10), "width": 25, "bd": 0, "pady": 8}

        tk.Button(control_frame, text="1. Load Image", command=self.load_image, **btn_style).pack(pady=5)
        
        tk.Label(control_frame, text="Pilih Proses:", bg="#1E1E1E", fg="#FFFFFF", font=("Helvetica", 10, "bold")).pack(pady=(15,5))
        
        # 5 Proses Wajib
        self.btn_gray = tk.Button(control_frame, text="RGB to Grayscale", command=self.to_grayscale, **btn_style)
        self.btn_gray.pack(pady=5)
        
        self.btn_heq = tk.Button(control_frame, text="Histogram Equalization", command=self.histogram_equalization, **btn_style)
        self.btn_heq.pack(pady=5)
        
        self.btn_gauss = tk.Button(control_frame, text="Gaussian Filter", command=self.gaussian_filter, **btn_style)
        self.btn_gauss.pack(pady=5)
        
        self.btn_canny = tk.Button(control_frame, text="Canny Edge Detection", command=self.canny_edge, **btn_style)
        self.btn_canny.pack(pady=5)
        
        self.btn_thresh = tk.Button(control_frame, text="Thresholding", command=self.thresholding, **btn_style)
        self.btn_thresh.pack(pady=5)

        self.process_buttons = [self.btn_gray, self.btn_heq, self.btn_gauss, self.btn_canny, self.btn_thresh]
        
        # Tombol Save
        tk.Button(control_frame, text="💾 Simpan Gambar Hasil", command=self.save_image, bg="#28A745", fg="white", font=("Helvetica", 10, "bold"), width=25, bd=0, pady=8).pack(pady=(20, 5))

        # Tombol Reset
        tk.Button(control_frame, text="Reset to Original", command=self.reset_image, bg="#D9534F", fg="white", font=("Helvetica", 10), width=25, bd=0, pady=8).pack(pady=5)

    def set_active_button(self, active_btn, process_name):
        self.current_process = process_name
        for btn in self.process_buttons:
            btn.configure(bg="#3A3A3A")
        if active_btn:
            active_btn.configure(bg="#007ACC")

    def display_image(self, img_array, label_widget):
        img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB) if len(img_array.shape) == 3 else img_array
        img = Image.fromarray(img)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        label_widget.configure(image=img_tk, text="")
        label_widget.image = img_tk

    def load_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if filepath:
            self.cv_image = cv2.imread(filepath)
            self.processed_image = self.cv_image.copy()
            self.current_filename = os.path.basename(filepath)
            self.display_image(self.cv_image, self.lbl_original)
            self.display_image(self.processed_image, self.lbl_processed)
            self.set_active_button(None, "original")

    def check_image_loaded(self):
        if self.cv_image is None:
            messagebox.showwarning("Peringatan", "Load gambar terlebih dahulu!")
            return False
        return True

    def to_grayscale(self):
        if not self.check_image_loaded(): return
        self.set_active_button(self.btn_gray, "grayscale")
        self.processed_image = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
        self.display_image(self.processed_image, self.lbl_processed)

    def histogram_equalization(self):
        if not self.check_image_loaded(): return
        self.set_active_button(self.btn_heq, "hist_eq")
        gray = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
        self.processed_image = cv2.equalizeHist(gray)
        self.display_image(self.processed_image, self.lbl_processed)

    def gaussian_filter(self):
        if not self.check_image_loaded(): return
        self.set_active_button(self.btn_gauss, "gaussian")
        self.processed_image = cv2.GaussianBlur(self.cv_image, (15, 15), 0)
        self.display_image(self.processed_image, self.lbl_processed)

    def canny_edge(self):
        if not self.check_image_loaded(): return
        self.set_active_button(self.btn_canny, "canny")
        gray = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
        self.processed_image = cv2.Canny(gray, 100, 200)
        self.display_image(self.processed_image, self.lbl_processed)

    def thresholding(self):
        if not self.check_image_loaded(): return
        self.set_active_button(self.btn_thresh, "threshold")
        gray = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
        _, self.processed_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        self.display_image(self.processed_image, self.lbl_processed)

    def reset_image(self):
        if not self.check_image_loaded(): return
        self.set_active_button(None, "original")
        self.processed_image = self.cv_image.copy()
        self.display_image(self.processed_image, self.lbl_processed)

    def save_image(self):
        if self.processed_image is None:
            messagebox.showwarning("Peringatan", "Tidak ada gambar yang bisa disimpan!")
            return

        # Membuat rekomendasi nama file
        name, ext = os.path.splitext(self.current_filename)
        default_name = f"{name}_{self.current_process}{ext}"
        
        save_path = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            initialfile=default_name,
            defaultextension=ext,
            title="Simpan Gambar Hasil",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")]
        )
        
        if save_path:
            cv2.imwrite(save_path, self.processed_image)
            messagebox.showinfo("Sukses", f"Gambar berhasil disimpan sebagai:\n{os.path.basename(save_path)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()