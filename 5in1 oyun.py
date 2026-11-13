import random
import time
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

# --- GLOBAL STİL AYARLARI ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class Mega20in1ArcadeStudio(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.title("Mega 20-in-1 Arcade Studio & Game Enterprise Suite v10.0")
    self.geometry("1200x800")
    self.minsize(1100, 720)

    # Oyuncu Profili ve Ekonomi Verileri
    self.profile_data = {
        "username": "Commander_Batuhan",
        "gold": 2500,
        "gems": 120,
        "level": 25,
        "xp": 7800,
        "total_wins": 112,
        "unlocked_badges": [
            "Pythonista",
            "Matematikçi",
            "Zar Kralı",
            "Elit Oyuncu",
        ],
    }

    # Ana Izgara Yerleşimi
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    # --- 1. SOL MENÜ (20 OYUN İÇİN SCROLLABLE KONTROL) ---
    self.build_sidebar()

    # --- 2. SAĞ İÇERİK ALANI ---
    self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
    self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
    self.content_frame.grid_rowconfigure(0, weight=1)
    self.content_frame.grid_columnconfigure(0, weight=1)

    # Başlangıç Ekranı
    self.show_dashboard()

  def build_sidebar(self):
    self.sidebar = ctk.CTkFrame(self, width=280, corner_radius=0)
    self.sidebar.grid(row=0, column=0, sticky="nsew")
    self.sidebar.grid_rowconfigure(1, weight=1)

    self.logo_lbl = ctk.CTkLabel(
        self.sidebar,
        text="🎮 MEGA ARCADE 20-in-1",
        font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
    )
    self.logo_lbl.grid(row=0, column=0, padx=15, pady=(20, 10))

    # Kaydırılabilir Menü Alanı (20 oyun sığması için)
    self.nav_scroll = ctk.CTkScrollableFrame(
        self.sidebar, fg_color="transparent", width=250
    )
    self.nav_scroll.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    nav_items = [
        ("🏠 1. Ana Komuta Merkezi", self.show_dashboard),
        ("🎯 2. Sayı Avcısı (Tahmin)", self.show_sayi_tahmin),
        ("✂️ 3. Taş Kağıt Makas", self.show_tas_kagit),
        ("🔤 4. Kelime Labirenti", self.show_adam_asmaca),
        ("⚡ 5. Matematik Sprint", self.show_matematik),
        ("🎲 6. Kraliyet Zar Düellosu", self.show_zar_duellosu),
        ("❌ 7. XOX Strateji Savaşı", self.show_xox),
        ("🪙 8. Kripto Borsa Sim.", self.show_borsa),
        ("🎰 9. Şans Çarkı", self.show_cark),
        ("🐍 10. Retro Yılan (Snake)", self.show_yilan),
        ("🧱 11. Blok Kırıcı (Arcade)", self.show_blok),
        ("🪙 12. Yazı Tura Atışı", self.show_yazi_tura),
        ("🧠 13. Hafıza Kartı Eşleme", self.show_hafiza),
        ("🏎️ 14. Hız Testi (Refleks)", self.show_refleks),
        ("💣 15. Mayın Tarlası Lite", self.show_mayin),
        ("🧮 16. Sayı Bulmaca (2048)", self.show_sayi_2048),
        ("🧙 17. Zindan RPG Macerası", self.show_rpg),
        ("🚀 18. Galaksi Tıklayıcısı", self.show_clicker),
        ("🏆 19. Başarımlar & Profil", self.show_profil),
        ("⚙️ 20. Sistem & Ayarlar", self.show_ayarlar),
    ]

    for idx, (txt, cmd) in enumerate(nav_items):
      btn = ctk.CTkButton(
          self.nav_scroll,
          text=txt,
          anchor="w",
          font=ctk.CTkFont(family="Helvetica", size=11, weight="bold"),
          fg_color="transparent",
          text_color=("gray10", "gray90"),
          hover_color=("gray70", "gray30"),
          height=30,
          command=cmd,
      )
      btn.pack(fill="x", pady=2, padx=5)

    # Sol Alt Profil Bilgileri
    self.profile_box = ctk.CTkFrame(self.sidebar, fg_color="transparent")
    self.profile_box.grid(row=2, column=0, padx=15, pady=15, sticky="ew")

    self.sb_gold = ctk.CTkLabel(
        self.profile_box,
        text=f"🪙 Altın: {self.profile_data['gold']}",
        font=ctk.CTkFont(size=11, weight="bold"),
        text_color="#f1c40f",
    )
    self.sb_gold.pack(anchor="w")

    self.sb_gem = ctk.CTkLabel(
        self.profile_box,
        text=f"💎 Elmas: {self.profile_data['gems']}",
        font=ctk.CTkFont(size=11, weight="bold"),
        text_color="#3498db",
    )
    self.sb_gem.pack(anchor="w")

    self.sb_lvl = ctk.CTkLabel(
        self.profile_box,
        text=f"⭐ Seviye: {self.profile_data['level']}",
        font=ctk.CTkFont(size=10),
        text_color="gray",
    )
    self.sb_lvl.pack(anchor="w")

  def clear_content(self):
    for widget in self.content_frame.winfo_children():
      widget.destroy()

  def sync_stats(self):
    self.sb_gold.configure(text=f"🪙 Altın: {self.profile_data['gold']}")
    self.sb_gem.configure(text=f"💎 Elmas: {self.profile_data['gems']}")
    self.sb_lvl.configure(text=f"⭐ Seviye: {self.profile_data['level']}")

  # ==========================================
  # 🏠 1. ANA KOMUTA MERKEZİ
  # ==========================================
  def show_dashboard(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)

    ctk.CTkLabel(
        wrap,
        text=f"Hoş Geldin, {self.profile_data['username']}!",
        font=ctk.CTkFont(size=22, weight="bold"),
    ).pack(anchor="w", pady=(5, 5))
    ctk.CTkLabel(
        wrap,
        text=(
            "20'si 1 arada mega arcade stüdyosu aktif. Sol menüden mod"
            " seçebilirsin."
        ),
        text_color="gray",
        font=ctk.CTkFont(size=12),
    ).pack(anchor="w", pady=(0, 15))

    grid = ctk.CTkFrame(wrap, fg_color="transparent")
    grid.pack(fill="x", pady=5)

    cards = [
        ("Toplam Zafer", f"{self.profile_data['total_wins']} Maç", "#2ecc71"),
        ("Cüzdan Altın", f"{self.profile_data['gold']} Altın", "#f1c40f"),
        ("Özel Elmas", f"{self.profile_data['gems']} Adet", "#3498db"),
        ("Aktif Rütbe", "Efsanevi Komutan", "#9b59b6"),
    ]

    for title, val, color in cards:
      c = ctk.CTkFrame(grid, corner_radius=8)
      c.pack(side="left", padx=6, expand=True, fill="both")
      ctk.CTkLabel(
          c, text=title, font=ctk.CTkFont(size=10), text_color="gray"
      ).pack(pady=(10, 0))
      ctk.CTkLabel(
          c,
          text=val,
          font=ctk.CTkFont(size=16, weight="bold"),
          text_color=color,
      ).pack(pady=(5, 10))

    ctk.CTkLabel(
        wrap,
        text="Canlı Sistem Tanılama Konsolu",
        font=ctk.CTkFont(size=13, weight="bold"),
    ).pack(anchor="w", pady=(15, 5))
    self.db_log = ctk.CTkTextbox(
        wrap, height=220, corner_radius=8, font=("Consolas", 11)
    )
    self.db_log.pack(fill="x", pady=5)
    self.db_log.insert(
        "end",
        "[OK] 20 Modül başarıyla belleğe yüklendi.\n[OK] Ekonomi ve Cüzdan"
        " senkronize.\n[READY] Komuta merkezi kullanıcı girdisi bekliyor...\n",
    )
    self.db_log.configure(state="disabled")

  # ==========================================
  # 🎯 2. SAYI AVCISI (TAHMİN)
  # ==========================================
  def show_sayi_tahmin(self):
    self.clear_content()
    self.st_num = random.randint(1, 100)
    self.st_hak = 7
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🎯 Sayı Avcısı (1-100 Tahmin)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.st_lbl = ctk.CTkLabel(
        wrap,
        text=f"Kalan Hak: {self.st_hak}",
        font=ctk.CTkFont(size=13, weight="bold"),
        text_color="#3498db",
    )
    self.st_lbl.pack(anchor="w", pady=5)
    row = ctk.CTkFrame(wrap, fg_color="transparent")
    row.pack(anchor="w", pady=10)
    self.st_ent = ctk.CTkEntry(row, placeholder_text="Tahmin...", width=150)
    self.st_ent.pack(side="left", padx=(0, 10))
    ctk.CTkButton(row, text="Tahmin Et", command=self.run_st).pack(side="left")
    self.st_box = ctk.CTkTextbox(
        wrap, height=200, corner_radius=8, font=("Consolas", 11)
    )
    self.st_box.pack(fill="x", pady=10)
    self.st_box.insert("end", "Oyun başladı! 1-100 arası bir sayı tahmin et.\n")
    self.st_box.configure(state="disabled")

  def run_st(self):
    try:
      v = int(self.st_ent.get())
    except:
      return
    self.st_hak -= 1
    self.st_ent.delete(0, "end")
    self.st_box.configure(state="normal")
    if v == self.st_num:
      self.st_box.insert("end", f"Tebrikler bildin! Sayı: {self.st_num}\n")
      self.profile_data["gold"] += 50
      self.sync_stats()
      messagebox.showinfo("Zafer", "+50 Altın Kazandın!")
      self.show_sayi_tahmin()
    elif self.st_hak == 0:
      messagebox.showwarning("Bitti", f"Hak bitti! Sayı: {self.st_num}")
      self.show_sayi_tahmin()
    elif v < self.st_num:
      self.st_box.insert("end", f"{v}: Daha BÜYÜK bir sayı söyle.\n")
    else:
      self.st_box.insert("end", f"{v}: Daha KÜÇÜK bir sayı söyle.\n")
    self.st_lbl.configure(text=f"Kalan Hak: {self.st_hak}")
    self.st_box.configure(state="disabled")

  # ==========================================
  # ✂️ 3. TAŞ KAĞIT MAKAS
  # ==========================================
  def show_tas_kagit(self):
    self.clear_content()
    self.tkm_p = 0
    self.tkm_c = 0
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="✂️ Taş Kağıt Makas Arena",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.tkm_score = ctk.CTkLabel(
        wrap,
        text="Skor -> Sen: 0 | PC: 0 (İlk 3 olan kazanır)",
        font=ctk.CTkFont(size=13, weight="bold"),
        text_color="#e67e22",
    )
    self.tkm_score.pack(anchor="w", pady=5)
    row = ctk.CTkFrame(wrap, fg_color="transparent")
    row.pack(anchor="w", pady=10)
    for c in ["Taş", "Kağıt", "Makas"]:
      ctk.CTkButton(
          row, text=c, width=100, command=lambda x=c: self.run_tkm(x)
      ).pack(side="left", padx=(0, 10))
    self.tkm_box = ctk.CTkTextbox(
        wrap, height=200, corner_radius=8, font=("Consolas", 11)
    )
    self.tkm_box.pack(fill="x", pady=10)
    self.tkm_box.insert("end", "Arena hazır!\n")
    self.tkm_box.configure(state="disabled")

  def run_tkm(self, p):
    cc = random.choice(["Taş", "Kağıt", "Makas"])
    pl, cl = p.lower(), cc.lower()
    self.tkm_box.configure(state="normal")
    if pl == cl:
      res = "Berabere!"
    elif (
        (pl == "taş" and cl == "makas")
        or (pl == "kağıt" and cl == "taş")
        or (pl == "makas" and cl == "kağıt")
    ):
      res = "Kazandın!"
      self.tkm_p += 1
    else:
      res = "PC Kazandı!"
      self.tkm_c += 1
    self.tkm_box.insert("end", f"Sen: {p} | PC: {cc} -> {res}\n")
    self.tkm_score.configure(text=f"Skor -> Sen: {self.tkm_p} | PC: {self.tkm_c}")
    self.tkm_box.configure(state="disabled")
    if self.tkm_p == 3:
      messagebox.showinfo("Zafer", "Maçı kazandın! +40 Altın")
      self.profile_data["gold"] += 40
      self.sync_stats()
      self.show_tas_kagit()
    elif self.tkm_c == 3:
      messagebox.showwarning("Yenilgi", "Bilgisayar maçı kazandı!")
      self.show_tas_kagit()

  # ==========================================
  # 🔤 4. KELİME LABİRENTİ (ADAM ASMACA)
  # ==========================================
  def show_adam_asmaca(self):
    self.clear_content()
    words = ["python", "algoritma", "bilgisayar", "yazılım", "donanım", "oyun"]
    self.aa_w = random.choice(words)
    self.aa_g = ["_"] * len(self.aa_w)
    self.aa_l = 5
    self.aa_u = []
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🔤 Kelime Labirenti (Adam Asmaca)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.aa_lbl = ctk.CTkLabel(
        wrap,
        text=" ".join(self.aa_g),
        font=ctk.CTkFont(size=22, weight="bold"),
        text_color="#2ecc71",
    )
    self.aa_lbl.pack(anchor="w", pady=10)
    self.aa_st = ctk.CTkLabel(wrap, text=f"Can: {self.aa_l} | Kullanılan: Yok")
    self.aa_st.pack(anchor="w", pady=5)
    row = ctk.CTkFrame(wrap, fg_color="transparent")
    row.pack(anchor="w", pady=10)
    self.aa_ent = ctk.CTkEntry(row, placeholder_text="Harf...", width=100)
    self.aa_ent.pack(side="left", padx=(0, 10))
    ctk.CTkButton(row, text="Tahmin Et", command=self.run_aa).pack(side="left")
    self.aa_box = ctk.CTkTextbox(
        wrap, height=180, corner_radius=8, font=("Consolas", 11)
    )
    self.aa_box.pack(fill="x", pady=10)
    self.aa_box.insert("end", "Bulmaca başladı!\n")
    self.aa_box.configure(state="disabled")

  def run_aa(self):
    let = self.aa_ent.get().lower()
    self.aa_ent.delete(0, "end")
    if len(let) != 1 or not let.isalpha() or let in self.aa_u:
      return
    self.aa_u.append(let)
    self.aa_box.configure(state="normal")
    if let in self.aa_w:
      for i, c in enumerate(self.aa_w):
        if c == let:
          self.aa_g[i] = let
      self.aa_lbl.configure(text=" ".join(self.aa_g))
      self.aa_box.insert("end", f"Doğru: {let}\n")
      if "_" not in self.aa_g:
        messagebox.showinfo("Tebrikler", "Kelimeyi buldun! +45 Altın")
        self.profile_data["gold"] += 45
        self.sync_stats()
        self.show_adam_asmaca()
        return
    else:
      self.aa_l -= 1
      self.aa_box.insert("end", f"Yanlış: {let}\n")
    self.aa_st.configure(
        text=f"Can: {self.aa_l} | Kullanılan: {', '.join(self.aa_u)}"
    )
    self.aa_box.configure(state="disabled")
    if self.aa_l == 0:
      messagebox.showwarning("Kaybettin", f"Kelime: {self.aa_w}")
      self.show_adam_asmaca()

  # ==========================================
  # ⚡ 5. MATEMATİK SPRINT
  # ==========================================
  def show_matematik(self):
    self.clear_content()
    self.m_score = 0
    self.m_idx = 0
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="⚡ Hızlı Matematik Sprint",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.m_qlbl = ctk.CTkLabel(
        wrap, text="Yükleniyor...", font=ctk.CTkFont(size=16, weight="bold")
    )
    self.m_qlbl.pack(anchor="w", pady=15)
    row = ctk.CTkFrame(wrap, fg_color="transparent")
    row.pack(anchor="w", pady=10)
    self.m_ent = ctk.CTkEntry(row, placeholder_text="Cevap...", width=120)
    self.m_ent.pack(side="left", padx=(0, 10))
    ctk.CTkButton(row, text="Cevapla", command=self.run_m).pack(side="left")
    self.m_box = ctk.CTkTextbox(
        wrap, height=180, corner_radius=8, font=("Consolas", 11)
    )
    self.m_box.pack(fill="x", pady=10)
    self.next_m()

  def next_m(self):
    if self.m_idx < 5:
      self.ms1 = random.randint(5, 30)
      self.ms2 = random.randint(2, 12)
      self.mop = random.choice(["+", "-", "*"])
      self.mans = (
          self.ms1 + self.ms2
          if self.mop == "+"
          else (
              self.ms1 - self.ms2 if self.mop == "-" else self.ms1 * self.ms2
          )
      )
      self.m_qlbl.configure(
          text=f"Soru {self.m_idx+1}/5: {self.ms1} {self.mop} {self.ms2} = ?"
      )
    else:
      messagebox.showinfo("Bitti", f"Doğru sayısı: {self.m_score}/5")
      self.profile_data["gold"] += self.m_score * 15
      self.sync_stats()
      self.show_matematik()

  def run_m(self):
    try:
      ans = int(self.m_ent.get())
    except:
      return
    self.m_ent.delete(0, "end")
    self.m_box.configure(state="normal")
    if ans == self.mans:
      self.m_score += 1
      self.m_box.insert("end", f"Soru {self.m_idx+1}: Doğru!\n")
    else:
      self.m_box.insert(
          "end", f"Soru {self.m_idx+1}: Yanlış (Doğru: {self.mans})\n"
      )
    self.m_idx += 1
    self.m_box.configure(state="disabled")
    self.next_m()

  # ==========================================
  # 🎲 6. ZAR DÜELLOSU
  # ==========================================
  def show_zar_duellosu(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🎲 Kraliyet Zar Düellosu",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.zar_st = ctk.CTkLabel(
        wrap,
        text=f"Altın: {self.profile_data['gold']}",
        font=ctk.CTkFont(size=13, weight="bold"),
        text_color="#f1c40f",
    )
    self.zar_st.pack(anchor="w", pady=5)
    row = ctk.CTkFrame(wrap, fg_color="transparent")
    row.pack(anchor="w", pady=10)
    ctk.CTkLabel(row, text="Bahis: ").pack(side="left", padx=(0, 5))
    self.zar_ent = ctk.CTkEntry(row, width=100)
    self.zar_ent.insert(0, "20")
    self.zar_ent.pack(side="left", padx=(0, 10))
    ctk.CTkButton(row, text="Zar At!", command=self.run_zar).pack(side="left")
    self.zar_box = ctk.CTkTextbox(
        wrap, height=200, corner_radius=8, font=("Consolas", 11)
    )
    self.zar_box.pack(fill="x", pady=10)
    self.zar_box.insert("end", "Zar düellosuna hoş geldin.\n")
    self.zar_box.configure(state="disabled")

  def run_zar(self):
    try:
      bet = int(self.zar_ent.get())
    except:
      return
    if bet <= 0 or bet > self.profile_data["gold"]:
      return
    pr = random.randint(1, 6) + random.randint(1, 6)
    cr = random.randint(1, 6) + random.randint(1, 6)
    self.zar_box.configure(state="normal")
    if pr > cr:
      self.profile_data["gold"] += bet
      res = f"Kazandın! (+{bet})"
    elif pr < cr:
      self.profile_data["gold"] -= bet
      res = f"Kaybettin! (-{bet})"
    else:
      res = "Berabere!"
    self.zar_box.insert("end", f"Sen: {pr} | PC: {cr} -> {res}\n")
    self.zar_st.configure(text=f"Altın: {self.profile_data['gold']}")
    self.sync_stats()
    self.zar_box.configure(state="disabled")

  # ==========================================
  # ❌ 7. XOX STRATEJİ SAVAŞI (AKILLI AI)
  # ==========================================
  def show_xox(self):
    self.clear_content()
    self.xox_g = [""] * 9
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="❌ XOX Strateji Savaşı (Akıllı Rakip)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    grid_f = ctk.CTkFrame(wrap, fg_color="transparent")
    grid_f.pack(pady=10)
    self.x_btns = []
    for i in range(9):
      b = ctk.CTkButton(
          grid_f,
          text="",
          width=70,
          height=70,
          font=ctk.CTkFont(size=22, weight="bold"),
          command=lambda idx=i: self.run_xox(idx),
      )
      b.grid(row=i // 3, column=i % 3, padx=4, pady=4)
      self.x_btns.append(b)

  def run_xox(self, idx):
    if self.xox_g[idx] != "":
      return
    self.xox_g[idx] = "X"
    self.x_btns[idx].configure(text="X", text_color="#3498db")
    if self.check_xox("X"):
      messagebox.showinfo("Zafer", "XOX Kazandın! +35 Altın")
      self.profile_data["gold"] += 35
      self.sync_stats()
      self.show_xox()
      return
    if "" not in self.xox_g:
      messagebox.showinfo("Berabere", "Oyun bitti!")
      self.show_xox()
      return
    # Akıllı AI
    ai_m = self.ai_xox()
    if ai_m is not None:
      self.xox_g[ai_m] = "O"
      self.x_btns[ai_m].configure(text="O", text_color="#e74c3c")
      if self.check_xox("O"):
        messagebox.showwarning("Yenilgi", "Bilgisayar kazandı!")
        self.show_xox()
        return

  def ai_xox(self):
    for i in range(9):
      if self.xox_g[i] == "":
        self.xox_g[i] = "O"
        if self.check_xox("O"):
          self.xox_g[i] = ""
          return i
        self.xox_g[i] = ""
    for i in range(9):
      if self.xox_g[i] == "":
        self.xox_g[i] = "X"
        if self.check_xox("X"):
          self.xox_g[i] = ""
          return i
        self.xox_g[i] = ""
    if self.xox_g[4] == "":
      return 4
    empty = [i for i, v in enumerate(self.xox_g) if v == ""]
    return random.choice(empty) if empty else None

  def check_xox(self, s):
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(
        self.xox_g[a] == s and self.xox_g[b] == s and self.xox_g[c] == s
        for a, b, c in wins
    )

  # ==========================================
  # 🪙 8. KRİPTO BORSA SİMÜLATÖRÜ
  # ==========================================
  def show_borsa(self):
    self.clear_content()
    self.cp = 100
    self.co = 0
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🪙 PythonCoin (PYC) Borsa Simülatörü",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.b_st = ctk.CTkLabel(
        wrap,
        text=f"Fiyat: {self.cp} Altın | PYC: {self.co}",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#f39c12",
    )
    self.b_st.pack(anchor="w", pady=10)
    row = ctk.CTkFrame(wrap, fg_color="transparent")
    row.pack(anchor="w", pady=10)
    ctk.CTkButton(
        row, text="Satın Al", fg_color="#27ae60", command=self.b_buy
    ).pack(side="left", padx=(0, 10))
    ctk.CTkButton(
        row, text="Sat", fg_color="#c0392b", command=self.b_sell
    ).pack(side="left", padx=(0, 10))
    ctk.CTkButton(row, text="Piyasayı Güncelle", command=self.b_up).pack(
        side="left"
    )
    self.b_box = ctk.CTkTextbox(
        wrap, height=200, corner_radius=8, font=("Consolas", 11)
    )
    self.b_box.pack(fill="x", pady=10)
    self.b_box.insert("end", "Borsa açıldı. Başlangıç: 100 Altın.\n")
    self.b_box.configure(state="disabled")

  def b_up(self):
    self.cp = max(10, self.cp + random.randint(-12, 15))
    self.b_box.configure(state="normal")
    self.b_box.insert("end", f"Yeni Fiyat: {self.cp} Altın\n")
    self.b_box.configure(state="disabled")
    self.b_st.configure(text=f"Fiyat: {self.cp} Altın | PYC: {self.co}")

  def b_buy(self):
    if self.profile_data["gold"] >= self.cp:
      self.profile_data["gold"] -= self.cp
      self.co += 1
      self.sync_stats()
      self.b_st.configure(text=f"Fiyat: {self.cp} Altın | PYC: {self.co}")
      messagebox.showinfo("Başarılı", "1 PYC alındı!")

  def b_sell(self):
    if self.co > 0:
      self.profile_data["gold"] += self.cp
      self.co -= 1
      self.sync_stats()
      self.b_st.configure(text=f"Fiyat: {self.cp} Altın | PYC: {self.co}")
      messagebox.showinfo("Başarılı", "1 PYC satıldı!")

  # ==========================================
  # 🎰 9. ŞANS ÇARKI
  # ==========================================
  def show_cark(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🎰 Şans Çarkı",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.c_lbl = ctk.CTkLabel(
        wrap,
        text="Çevirmek için tıkla (Bedel: 20 Altın)",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#f1c40f",
    )
    self.c_lbl.pack(anchor="w", pady=20)
    ctk.CTkButton(wrap, text="Çarkı Çevir", command=self.spin_c).pack(anchor="w")

  def spin_c(self):
    if self.profile_data["gold"] < 20:
      return
    self.profile_data["gold"] -= 20
    rew = [
        ("50 Altın", 50, "g"),
        ("100 Altın", 100, "g"),
        ("5 Elmas", 5, "e"),
        ("Boş", 0, "n"),
    ]
    t, v, ty = random.choice(rew)
    if ty == "g":
      self.profile_data["gold"] += v
    elif ty == "e":
      self.profile_data["gems"] += v
    self.sync_stats()
    messagebox.showinfo("Çark Sonucu", f"Kazandığın: {t}")

  # ==========================================
  # 🐍 10. RETRO YILAN (SNAKE SİMÜLATÖRÜ)
  # ==========================================
  def show_yilan(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🐍 Retro Yılan Oyunu (Simülasyon Arena)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.s_scr = 0
    self.s_lbl = ctk.CTkLabel(
        wrap,
        text="Skor: 0 | Yem Topla!",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#2ecc71",
    )
    self.s_lbl.pack(anchor="w", pady=10)
    ctk.CTkButton(wrap, text="Yemi Ye (+ Skor & Altın)", command=self.eat_snake).pack(
        anchor="w", pady=10
    )
    self.s_box = ctk.CTkTextbox(
        wrap, height=180, corner_radius=8, font=("Consolas", 11)
    )
    self.s_box.pack(fill="x", pady=10)
    self.s_box.insert("end", "Yılan simülasyonu aktif.\n")
    self.s_box.configure(state="disabled")

  def eat_snake(self):
    self.s_scr += 10
    self.profile_data["gold"] += 10
    self.sync_stats()
    self.s_lbl.configure(text=f"Skor: {self.s_scr} | Harika!")
    self.s_box.configure(state="normal")
    self.s_box.insert("end", f"Yem yendi! Güncel Skor: {self.s_scr}\n")
    self.s_box.configure(state="disabled")

  # ==========================================
  # 🧱 11. BLOK KIRICI
  # ==========================================
  def show_blok(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🧱 Blok Kırıcı (Arcade Modülü)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.b_score = 0
    self.b_lbl = ctk.CTkLabel(
        wrap,
        text="Kırılan Blok: 0",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#3498db",
    )
    self.b_lbl.pack(anchor="w", pady=10)
    ctk.CTkButton(
        wrap, text="Topu Fırlat & Blok Kır", command=self.hit_block
    ).pack(anchor="w", pady=10)

  def hit_block(self):
    self.b_score += 1
    self.profile_data["gold"] += 5
    self.sync_stats()
    self.b_lbl.configure(text=f"Kırılan Blok: {self.b_score}")

  # ==========================================
  # 🪙 12. YAZI TURA
  # ==========================================
  def show_yazi_tura(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🪙 Yazı Tura Atışı",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    row = ctk.CTkFrame(wrap, fg_color="transparent")
    row.pack(anchor="w", pady=15)
    ctk.CTkButton(
        row, text="Yazı", command=lambda: self.yt("Yazı"), width=100
    ).pack(side="left", padx=(0, 10))
    ctk.CTkButton(
        row, text="Tura", command=lambda: self.yt("Tura"), width=100
    ).pack(side="left")
    self.yt_box = ctk.CTkTextbox(
        wrap, height=180, corner_radius=8, font=("Consolas", 11)
    )
    self.yt_box.pack(fill="x", pady=10)

  def yt(self, cho):
    res = random.choice(["Yazı", "Tura"])
    self.yt_box.configure(state="normal")
    if cho == res:
      self.profile_data["gold"] += 25
      self.sync_stats()
      self.yt_box.insert("end", f"Seçimin: {cho} | Gelen: {res} -> Kazandın!\n")
    else:
      self.yt_box.insert("end", f"Seçimin: {cho} | Gelen: {res} -> Kaybettin!\n")
    self.yt_box.configure(state="disabled")

  # ==========================================
  # 🧠 13. HAFIZA KARTI
  # ==========================================
  def show_hafiza(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🧠 Hafıza Kartı Eşleme",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    ctk.CTkButton(wrap, text="Kartları Eşleştir", command=self.hf_win).pack(
        anchor="w", pady=15
    )

  def hf_win(self):
    self.profile_data["gold"] += 40
    self.sync_stats()
    messagebox.showinfo("Başarılı", "Tüm kartlar eşleşti! +40 Altın")

  # ==========================================
  # 🏎️ 14. REFLEKS TESTİ
  # ==========================================
  def show_refleks(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🏎️ Hız ve Refleks Testi",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    ctk.CTkButton(
        wrap, text="Refleks Testini Başlat", command=self.ref_test
    ).pack(anchor="w", pady=15)

  def ref_test(self):
    ms = random.randint(180, 450)
    self.profile_data["gold"] += 30
    self.sync_stats()
    messagebox.showinfo(
        "Sonuç", f"Tepki Süren: {ms} ms! Harika reflex. +30 Altın"
    )

  # ==========================================
  # 💣 15. MAYIN TARLASI
  # ==========================================
  def show_mayin(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="💣 Güvenli Alan Bulma (Mayın Tarlası Lite)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    ctk.CTkButton(
        wrap, text="Güvenli Kutuyu Aç", command=self.mayin_click
    ).pack(anchor="w", pady=15)

  def mayin_click(self):
    if random.random() > 0.3:
      self.profile_data["gold"] += 50
      self.sync_stats()
      messagebox.showinfo("Güvenli!", "Mayına basmadın! +50 Altın")
    else:
      messagebox.showwarning("BOOM!", "Mayına bastın! Şansına küs.")

  # ==========================================
  # 🧮 16. SAYI BİRLEŞTİRME (2048 LITE)
  # ==========================================
  def show_sayi_2048(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🧮 Sayı Birleştirme (2048 Stüdyo)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    ctk.CTkButton(
        wrap, text="Hamle Yap (Sayıları Birleştir)", command=self.n2048
    ).pack(anchor="w", pady=15)

  def n2048(self):
    self.profile_data["gold"] += 35
    self.sync_stats()
    messagebox.showinfo("Hamle", "Sayılar birleşti! +35 Altın")

  # ==========================================
  # 🧙 17. ZİNDAN RPG
  # ==========================================
  def show_rpg(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🧙 Zindan RPG Macerası",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    ctk.CTkButton(wrap, text="Canavarla Savaş", command=self.rpg_fight).pack(
        anchor="w", pady=15
    )

  def rpg_fight(self):
    self.profile_data["gold"] += 60
    self.profile_data["gems"] += 2
    self.sync_stats()
    messagebox.showinfo(
        "Zafer", "Canavar alt edildi! +60 Altın, +2 Elmas kazandın."
    )

  # ==========================================
  # 🚀 18. GALAKSİ TIKLAYICISI
  # ==========================================
  def show_clicker(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🚀 Galaksi Tıklayıcısı",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    self.cl_score = 0
    self.cl_lbl = ctk.CTkLabel(
        wrap,
        text="Tıklama: 0",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#9b59b6",
    )
    self.cl_lbl.pack(anchor="w", pady=10)
    ctk.CTkButton(wrap, text="Evrene Tıkla!", command=self.click_evren).pack(
        anchor="w", pady=10
    )

  def click_evren(self):
    self.cl_score += 1
    self.profile_data["gold"] += 2
    self.sync_stats()
    self.cl_lbl.configure(text=f"Tıklama: {self.cl_score}")

  # ==========================================
  # 🏆 19. PROFİL & BAŞARIMLAR
  # ==========================================
  def show_profil(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="🏆 Oyuncu Profili ve Rozetler",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    info = f"""
    Kullanıcı Adı : {self.profile_data['username']}
    Seviye        : {self.profile_data['level']}
    Toplam Zafer  : {self.profile_data['total_wins']} Maç
    Altın Bakiyesi: {self.profile_data['gold']} Altın
    Elmas Bakiyesi: {self.profile_data['gems']} Elmas
    """
    ctk.CTkLabel(
        wrap, text=info, font=ctk.CTkFont(size=13), justify="left"
    ).pack(anchor="w", pady=10)
    ctk.CTkLabel(
        wrap, text="Rozetler:", font=ctk.CTkFont(weight="bold")
    ).pack(anchor="w", pady=(10, 5))
    for b in self.profile_data["unlocked_badges"]:
      ctk.CTkLabel(wrap, text=f"✔ {b}", text_color="#2ecc71").pack(anchor="w")

  # ==========================================
  # ⚙️ 20. SİSTEM & AYARLAR
  # ==========================================
  def show_ayarlar(self):
    self.clear_content()
    wrap = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    wrap.pack(fill="both", expand=True)
    ctk.CTkLabel(
        wrap,
        text="⚙️ Gelişmiş Sistem Ayarları",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=10)
    ctk.CTkLabel(wrap, text="Tema Seçimi:").pack(anchor="w", pady=(15, 5))
    ctk.CTkOptionMenu(
        wrap,
        values=["Dark", "Light", "System"],
        command=lambda m: ctk.set_appearance_mode(m),
    ).pack(anchor="w", pady=5)
    ctk.CTkButton(
        wrap,
        text="Tüm Verileri Sıfırla",
        fg_color="#e74c3c",
        command=self.reset_all,
    ).pack(anchor="w", pady=(30, 5))

  def reset_all(self):
    if messagebox.askyesno("Onay", "Tüm oyun verileri sıfırlanacak?"):
      self.profile_data = {
          "username": "Commander_Batuhan",
          "gold": 500,
          "gems": 10,
          "level": 1,
          "xp": 0,
          "total_wins": 0,
          "unlocked_badges": ["Çaylak"],
      }
      self.sync_stats()
      messagebox.showinfo("Başarılı", "Sıfırlandı.")
      self.show_dashboard()


if __name__ == "__main__":
  app = Mega20in1ArcadeStudio()
  app.mainloop()