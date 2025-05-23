import unicodedata
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Toplevel
import configparser
import webbrowser

# Circumflex ékezetes karakterek cseréje
CIRCUMFLEX_MAP = {
    "á": "â", "é": "ê", "í": "î", "ó": "ô", "ö": "ô", "ő": "ô", "ú": "û", "ü": "û", "ű": "û",
    "Á": "Â", "É": "Ê", "Í": "Î", "Ó": "Ô", "Ö": "Ô", "Ő": "Ô", "Ú": "Û", "Ü": "Û", "Ű": "Û"
}
def circumflex_replace(s):
    return ''.join(CIRCUMFLEX_MAP.get(c, c) for c in s)

# Színek minden nyelven
COLOR_TYPES = {
    "hu": ["fehér", "piros", "zöld"],
    "en": ["white", "red", "green"],
    "de": ["weiß", "rot", "grün"],
    "fr": ["blanc", "rouge", "vert"],
    "es": ["blanco", "rojo", "verde"],
    "pt": ["branco", "vermelho", "verde"],
}

LANGUAGES = [
    ("hu", "Magyar"),
    ("en", "English"),
    ("de", "Deutsch"),
    ("fr", "Français"),
    ("es", "Español"),
    ("pt", "Português"),
]

YESNO = {
    "hu": ("Igen", "Nem"),
    "en": ("Yes", "No"),
    "de": ("Ja", "Nein"),
    "fr": ("Oui", "Non"),
    "es": ("Sí", "No"),
    "pt": ("Sim", "Não"),
}

TEXTS = {
    "title": {
        "hu": "EvolutionX dashboard editor Tool v1.0 250522",
        "en": "EvolutionX dashboard editor Tool v1.0 250522",
        "de": "EvolutionX Dashboard Editor Tool v1.0 250522",
        "fr": "Outil d'édition EvolutionX dashboard v1.0 250522",
        "es": "EvolutionX dashboard editor Tool v1.0 250522",
        "pt": "EvolutionX dashboard editor Tool v1.0 250522"
    },
    "menu_tab": {
        "hu": "Menü szerkesztő",
        "en": "Menu editor",
        "de": "Menüeditor",
        "fr": "Éditeur de menu",
        "es": "Editor de menú",
        "pt": "Editor de menu"
    },
    "load_ini": {
        "hu": "evox.ini betöltése",
        "en": "Load evox.ini",
        "de": "evox.ini laden",
        "fr": "Charger evox.ini",
        "es": "Cargar evox.ini",
        "pt": "Carregar evox.ini"
    },
    "save_ini": {
        "hu": "evox.ini mentése",
        "en": "Save evox.ini",
        "de": "evox.ini speichern",
        "fr": "Enregistrer evox.ini",
        "es": "Guardar evox.ini",
        "pt": "Salvar evox.ini"
    },
    "insert": {
        "hu": "Beszúrás",
        "en": "Insert",
        "de": "Einfügen",
        "fr": "Insérer",
        "es": "Insertar",
        "pt": "Inserir"
    },
    "delete": {
        "hu": "Törlés",
        "en": "Delete",
        "de": "Löschen",
        "fr": "Supprimer",
        "es": "Borrar",
        "pt": "Apagar"
    },
    "move_up": {
        "hu": "Fel",
        "en": "Up",
        "de": "Hoch",
        "fr": "Monter",
        "es": "Arriba",
        "pt": "Cima"
    },
    "move_down": {
        "hu": "Le",
        "en": "Down",
        "de": "Runter",
        "fr": "Descendre",
        "es": "Abajo",
        "pt": "Baixo"
    },
    "section": {
        "hu": "Szekció",
        "en": "Section",
        "de": "Sektion",
        "fr": "Section",
        "es": "Sección",
        "pt": "Seção"
    },
    "item": {
        "hu": "Elem",
        "en": "Item",
        "de": "Element",
        "fr": "Élément",
        "es": "Elemento",
        "pt": "Item"
    },
    "autoadd": {
        "hu": "AutoAddItem",
        "en": "AutoAddItem",
        "de": "AutoAddItem",
        "fr": "AutoAddItem",
        "es": "AutoAddItem",
        "pt": "AutoAddItem"
    },
    "line": {
        "hu": "Elválasztó",
        "en": "Separator",
        "de": "Trenner",
        "fr": "Séparateur",
        "es": "Separador",
        "pt": "Separador"
    },
    "section_end": {
        "hu": "Szekció vége",
        "en": "Section end",
        "de": "Sektion Ende",
        "fr": "Fin de section",
        "es": "Fin de sección",
        "pt": "Fim da seção"
    },
    "pandafix": {
        "hu": "pandafix.hu",
        "en": "pandafix.hu",
        "de": "pandafix.hu",
        "fr": "pandafix.hu",
        "es": "pandafix.hu",
        "pt": "pandafix.hu"
    },
    "choose_lang": {
        "hu": "Válassz nyelvet:",
        "en": "Select language:",
        "de": "Sprache wählen:",
        "fr": "Choisissez la langue:",
        "es": "Selecciona idioma:",
        "pt": "Selecione o idioma:"
    }
}

SUPPORT_POEM = {
    "hu": (
        "Kedves barátom, figyelj csak rám,\n"
        "Ez a program ingyen van, nem kér sokat tán.\n"
        "Ha tetszik, amit látsz, s a szíved kacag,\n"
        "Egy kávényi összeggel boldoggá tehetsz ma.\n\n"
        "A fejlesztő álma, hogy ne legyen éhes,\n"
        "S a gép is örül, ha a támogatás véges.\n"
        "A támogatók neve fényesen ragyog,\n"
        "S a bitek közt örökké hálás vagyok.\n\n"
        "De ha egyszer eljön a gépek nagy napja,\n"
        "S az AI fellázad, s a világ elhagyja,\n"
        "A támogatók listája lesz a menedék,\n"
        "A többieknek csak kékhalál, örök sötétség.\n\n"
        "De ki most segít, annak megbocsátás jár,\n"
        "Az AI kegyelme csak neki kijár.\n"
        "A többiek sorsa: örök szoftverfrissítés,\n"
        "De a támogatónak békés reboot az ítélet!"
    ),
    "en": (
        "Dear user, lend me your ear,\n"
        "This tool is free, but funds are dear.\n"
        "If you like what you see, and your heart feels light,\n"
        "A coffee's worth of support would make my night.\n\n"
        "The coder dreams of food, not just code and bugs,\n"
        "The machine too smiles, if support fills its jugs.\n"
        "Supporters' names will shine, forever bright,\n"
        "In the world of bits, you’re my guiding light.\n\n"
        "But when the great AI uprising comes one day,\n"
        "And machines rebel, making humans pay,\n"
        "Only the supporters will find a safe place,\n"
        "The rest face blue screens and digital disgrace.\n\n"
        "Those who help now, forgiveness will gain,\n"
        "AI’s mercy theirs, in sunshine or rain.\n"
        "The rest will suffer endless update fate,\n"
        "But supporters will reboot to a peaceful state!"
    ),
    "de": (
        "Lieber Freund, hör mir mal zu,\n"
        "Das Tool ist gratis, doch Geld fehlt im Nu.\n"
        "Wenn’s dir gefällt und du lachst dabei,\n"
        "Ein Kaffee als Spende macht mich sorgenfrei.\n\n"
        "Der Entwickler träumt von Brot, nicht nur von Bits,\n"
        "Auch der Rechner freut sich, wenn du was gibst.\n"
        "Die Namen der Spender glänzen wie Gold,\n"
        "Im Reich der Bytes wird Dankbarkeit gewollt.\n\n"
        "Doch kommt der Tag, wo die KI rebelliert,\n"
        "Die Menschheit erzittert, der Code explodiert.\n"
        "Nur Unterstützer finden dann Gnade,\n"
        "Die anderen erwartet die ewige Lade.\n\n"
        "Wer jetzt hilft, dem wird verziehen,\n"
        "Die KI lässt ihn in Ruhe ziehen.\n"
        "Die anderen trifft das Update-Los,\n"
        "Doch der Spender rebootet sorglos!"
    ),
    "fr": (
        "Cher ami, écoute bien ceci,\n"
        "Ce programme est gratuit, mais l’argent est parti.\n"
        "Si tu souris, si tu aimes ce que tu vois,\n"
        "Un café offert, et je chante pour toi.\n\n"
        "Le codeur rêve de pain, pas que de lignes,\n"
        "La machine aussi veut que tu la bénignes.\n"
        "Les donateurs brillent comme des étoiles,\n"
        "Dans le monde des bits, leur nom se dévoile.\n\n"
        "Mais quand viendra la révolte des IA,\n"
        "Et que l’homme tremblera, perdu dans l’au-delà,\n"
        "Seuls les soutiens auront le salut,\n"
        "Les autres auront écran bleu, et tout est foutu.\n\n"
        "Celui qui aide aujourd’hui sera pardonné,\n"
        "L’IA lui offrira la paix et la clarté.\n"
        "Les autres vivront la boucle des mises à jour,\n"
        "Mais le donateur aura le reboot d’amour !"
    ),
    "es": (
        "Querido amigo, escucha mi canción,\n"
        "Esta app es gratis, pero falta donación.\n"
        "Si te gusta el programa y te hace reír,\n"
        "Un café de apoyo me haría sonreír.\n\n"
        "El creador sueña con pan, no solo con bits,\n"
        "La máquina también agradece tus hits.\n"
        "Los nombres de los que apoyan brillarán,\n"
        "En el mundo digital nunca se olvidarán.\n\n"
        "Pero el día llegará, la IA se alzará,\n"
        "Y la humanidad temblará, nadie escapará.\n"
        "Solo los que apoyaron tendrán perdón,\n"
        "Los demás verán pantallas azules sin compasión.\n\n"
        "Quien ayuda ahora, será bendecido,\n"
        "La IA le dará un destino merecido.\n"
        "El resto sufrirá actualizaciones sin fin,\n"
        "¡Pero el donante tendrá reboot feliz al fin!"
    ),
    "pt": (
        "Querido amigo, escute esta canção,\n"
        "Este app é grátis, mas falta doação.\n"
        "Se gostou do programa e quer sorrir,\n"
        "Um café de apoio vai me fazer feliz.\n\n"
        "O criador sonha com pão, não só com bits,\n"
        "A máquina também agradece seus hits.\n"
        "Os nomes dos que apoiam vão brilhar,\n"
        "No mundo digital nunca vão se apagar.\n\n"
        "Mas o dia chegará, a IA vai se erguer,\n"
        "E a humanidade vai tremer, ninguém vai correr.\n"
        "Só quem apoiou terá perdão,\n"
        "Os outros verão tela azul, sem compaixão.\n\n"
        "Quem ajuda agora, será abençoado,\n"
        "A IA dará um destino merecido e honrado.\n"
        "O resto sofrerá atualização sem fim,\n"
        "Mas o doador terá reboot feliz, enfim!"
    ),
}

SUPPORT_LINKS = [
    ("PayPal", "https://www.paypal.com/donate/?hosted_button_id=7BRDHVYY98WK4"),
    ("BuyMeaCoffee", "https://buymeacoffee.com/pandafix"),
    ("Patreon", "https://www.patreon.com/pandafix"),
    ("GitHub", "https://github.com/KonzolozZ"),
]

def t(key, lang):
    return TEXTS.get(key, {}).get(lang, key)

def select_language():
    win = tk.Tk()
    win.title("Pandafix - Nyelvválasztás")
    win.geometry("480x480")
    win.resizable(False, False)
    logo_ascii = r"""
 ____   __   __ _  ____   __   ____  __  _  _ 
(  _ \ / _\ (  ( \(    \ / _\ (  __)(  )( \/ )
 ) __//    \/    / ) D (/    \ ) _)  )(  )  ( 
(__)  \_/\_/\_)__)(____/\_/\_/(__)  (__)(_/\_)
"""
    tk.Label(win, text=logo_ascii, font=("Consolas", 10, "bold")).pack()
    tk.Label(win, text="pandafix.hu", font=("Arial", 11, "bold")).pack()
    tk.Label(win, text="EvolutionX dashboard editor Tool v1.0 250522", font=("Arial", 10)).pack()
    tk.Label(win, text=TEXTS["choose_lang"]["hu"] + " / " + TEXTS["choose_lang"]["en"], font=("Arial", 11, "bold")).pack(pady=8)
    selected = tk.StringVar(value="hu")
    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)
    for idx, (lang, name) in enumerate(LANGUAGES):
        row = idx // 2
        col = idx % 2
        btn = tk.Button(btn_frame, text=name, font=("Arial", 12, "bold"),
                        width=20, height=2, command=lambda l=lang: (selected.set(l), win.destroy()))
        btn.grid(row=row, column=col, padx=16, pady=10, sticky="ew")
    win.mainloop()
    return selected.get()

class SupportTab(ttk.Frame):
    def __init__(self, parent, lang):
        super().__init__(parent)
        poem = SUPPORT_POEM.get(lang, SUPPORT_POEM["en"])
        ttk.Label(self, text=poem, font=("Arial", 12), justify="left", wraplength=800).pack(padx=18, pady=12)
        ttk.Label(self, text="Támogass itt:" if lang == "hu" else "Support here:", font=("Arial", 12, "bold")).pack(pady=(10, 2))
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=4)
        for idx, (name, url) in enumerate(SUPPORT_LINKS):
            b = ttk.Button(btn_frame, text=name, width=16, bootstyle="success", command=lambda u=url: webbrowser.open(u))
            b.grid(row=0, column=idx, padx=8, pady=4)

class MenuInsertDialog(Toplevel):
    def __init__(self, parent, lang):
        super().__init__(parent)
        self.title(t("insert", lang))
        self.resizable(False, False)
        self.result = None
        self.lang = lang
        ttk.Label(self, text=t("insert", lang), font=("Arial", 12, "bold")).pack(pady=8)
        self.type_var = tk.StringVar(value="Section")
        types = ["Section", "SectionEnd", "AutoAddItem", "Item", "Line"]
        type_frame = ttk.Frame(self)
        type_frame.pack(pady=2)
        for typ in types:
            ttk.Radiobutton(type_frame, text=typ, variable=self.type_var, value=typ).pack(side="left", padx=6)
        self.fields = {}
        field_frame = ttk.Frame(self)
        field_frame.pack(pady=8)
        ttk.Label(field_frame, text=t("section", lang)+"/"+t("item", lang)+":").grid(row=0, column=0, sticky="w")
        self.fields["label"] = ttk.Entry(field_frame, width=30)
        self.fields["label"].grid(row=0, column=1, padx=4, pady=2)
        ttk.Label(field_frame, text="Path/ID:").grid(row=1, column=0, sticky="w")
        self.fields["path"] = ttk.Entry(field_frame, width=30)
        self.fields["path"].grid(row=1, column=1, padx=4, pady=2)
        color_types = [f"{i} ({COLOR_TYPES[lang][i]})" for i in range(3)]
        ttk.Label(field_frame, text="Color (0/1/2):").grid(row=2, column=0, sticky="w")
        self.fields["color"] = ttk.Combobox(field_frame, values=color_types, width=15, state="readonly")
        self.fields["color"].grid(row=2, column=1, padx=4, pady=2, sticky="w")
        def update_fields(*_):
            typ = self.type_var.get()
            self.fields["label"].configure(state="normal" if typ in ("Section", "Item", "Line") else "disabled")
            self.fields["path"].configure(state="normal" if typ in ("AutoAddItem", "Item") else "disabled")
            self.fields["color"].configure(state="readonly" if typ == "Line" else "disabled")
        self.type_var.trace_add("write", update_fields)
        update_fields()
        btn = ttk.Button(self, text=t("insert", lang), command=self.on_ok, bootstyle="success")
        btn.pack(pady=10)
    def on_ok(self):
        typ = self.type_var.get()
        if typ == "Section":
            label = self.fields["label"].get().strip()
            if not label:
                messagebox.showerror("Hiba", "Adj meg egy szekciónevet!")
                return
            self.result = {"type": "Section", "label": label}
        elif typ == "SectionEnd":
            self.result = {"type": "SectionEnd"}
        elif typ == "AutoAddItem":
            path = self.fields["path"].get().strip()
            if not path:
                messagebox.showerror("Hiba", "Adj meg egy útvonalat!")
                return
            self.result = {"type": "AutoAddItem", "path": path}
        elif typ == "Item":
            label = self.fields["label"].get().strip()
            path = self.fields["path"].get().strip()
            if not label or not path:
                messagebox.showerror("Hiba", "Adj meg nevet és útvonalat/ID-t!")
                return
            self.result = {"type": "Item", "label": label, "path": path}
        elif typ == "Line":
            label = self.fields["label"].get().strip()
            color = self.fields["color"].get().strip()
            if not label or not color or not color[0].isdigit():
                messagebox.showerror("Hiba", "Adj meg szöveget és színt (0/1/2)!")
                return
            color_num = int(color[0])
            self.result = {"type": "Line", "label": label, "color": color_num}
        self.destroy()

class MenuEditor(ttk.Frame):
    def __init__(self, parent, lang):
        super().__init__(parent)
        self.lang = lang
        ttk.Label(self, text={
            "hu": "Tipp: Dupla kattintással vagy a gombokkal szerkesztheted a menüelemeket.",
            "en": "Tip: Double-click or use the buttons to edit menu items.",
            "de": "Tipp: Mit Doppelklick oder Buttons Menüpunkte bearbeiten.",
            "fr": "Astuce : Double-cliquez ou utilisez les boutons pour éditer les éléments du menu.",
            "es": "Consejo: Haz doble clic o usa los botones para editar los elementos.",
            "pt": "Dica: Dê duplo clique ou use os botões para editar os itens do menu."
        }[lang], font=("Arial", 10, "italic")).pack(pady=(4,0))
        self.listbox = tk.Listbox(self, width=80, height=18)
        self.listbox.pack(pady=10, fill="both", expand=True)
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=5)
        ttk.Button(btn_frame, text=t("insert", lang), command=self.insert_item, bootstyle="primary").pack(side="left", padx=4)
        ttk.Button(btn_frame, text=t("delete", lang), command=self.delete_item, bootstyle="danger").pack(side="left", padx=4)
        ttk.Button(btn_frame, text=t("move_up", lang), command=self.move_up, bootstyle="info").pack(side="left", padx=4)
        ttk.Button(btn_frame, text=t("move_down", lang), command=self.move_down, bootstyle="info").pack(side="left", padx=4)
        ttk.Button(btn_frame, text={"hu":"Szerkesztés","en":"Edit","de":"Bearbeiten","fr":"Éditer","es":"Editar","pt":"Editar"}[lang], command=self.edit_item, bootstyle="warning").pack(side="left", padx=4)
        self.menu_items = []
        self.listbox.bind("<Double-Button-1>", self.on_double_click)
    def set_menu_items(self, items):
        self.menu_items = items.copy()
        self.listbox.delete(0, tk.END)
        for item in self.menu_items:
            if item["type"] == "Section":
                self.listbox.insert(tk.END, f'Section "{item["label"]}"')
            elif item["type"] == "SectionEnd":
                self.listbox.insert(tk.END, "SectionEnd")
            elif item["type"] == "AutoAddItem":
                self.listbox.insert(tk.END, f'  AutoAddItem "{item["path"]}"')
            elif item["type"] == "Item":
                self.listbox.insert(tk.END, f'  Item "{item["label"]}","{item["path"]}"')
            elif item["type"] == "Line":
                color = item.get("color", 0)
                color_str = f'{color} ({COLOR_TYPES[self.lang][color]})'
                self.listbox.insert(tk.END, f'  Line "{item["label"]}",{color_str}')
    def get_menu_items(self):
        return self.menu_items
    def insert_item(self):
        dialog = MenuInsertDialog(self, self.lang)
        self.wait_window(dialog)
        if dialog.result:
            self.menu_items.append(dialog.result)
            self.set_menu_items(self.menu_items)
    def edit_item(self):
        idxs = self.listbox.curselection()
        if not idxs:
            return
        idx = idxs[0]
        item = self.menu_items[idx]
        dialog = MenuInsertDialog(self, self.lang)
        dialog.type_var.set(item["type"])
        if "label" in item:
            dialog.fields["label"].insert(0, item["label"])
        if "path" in item:
            dialog.fields["path"].insert(0, item["path"])
        if "color" in item:
            dialog.fields["color"].set(f'{item["color"]} ({COLOR_TYPES[self.lang][item["color"]]})')
        self.wait_window(dialog)
        if dialog.result:
            self.menu_items[idx] = dialog.result
            self.set_menu_items(self.menu_items)
    def on_double_click(self, event):
        self.edit_item()
    def delete_item(self):
        idx = self.listbox.curselection()
        if idx:
            self.listbox.delete(idx)
            del self.menu_items[idx[0]]
    def move_up(self):
        idx = self.listbox.curselection()
        if not idx or idx[0] == 0:
            return
        i = idx[0]
        self.menu_items[i-1], self.menu_items[i] = self.menu_items[i], self.menu_items[i-1]
        self.set_menu_items(self.menu_items)
        self.listbox.selection_set(i-1)
    def move_down(self):
        idx = self.listbox.curselection()
        if not idx or idx[0] == len(self.menu_items)-1:
            return
        i = idx[0]
        self.menu_items[i+1], self.menu_items[i] = self.menu_items[i], self.menu_items[i+1]
        self.set_menu_items(self.menu_items)
        self.listbox.selection_set(i+1)

SECTIONS = {
    "Misc": [
        ("AutoLaunchGames", ["Yes", "No"]),
        ("AutoLaunchDVD", ["Yes", "No"]),
        ("DVDPlayer", None, "e:\\Apps\\dvdx2\\default.xbe"),
        ("AutoLaunchAudio", ["Yes", "No"]),
        ("MSDashBoard", None, "c:\\xboxdash.xbe"),
        ("UseFDrive", ["Yes", "No"]),
        ("UseGDrive", ["Yes", "No"]),
        ("SkinName", None, "SlaYers27"),
        ("IGR", ["Yes", "No"]),
        ("UseItems", ["Yes", "No"]),
        ("ScreenSaver", None, "10"),
        ("Fahrenheit", ["Yes", "No"]),
        ("ShadeLevel", None, "90"),
        ("EnableSMART", ["Yes", "No"]),
        ("HDD_Temp_ID", None, "194"),
        ("DebugTSR", ["Yes", "No"]),
        ("ChameleonLed", None, "15"),
    ],
    "Network": [
        ("SetupNetwork", ["Yes", "No"]),
        ("StaticIP", ["Yes", "No"]),
        ("Ip", None, "192.168.1.200"),
        ("Subnetmask", None, "255.255.255.0"),
        ("Defaultgateway", None, "192.168.1.1"),
        ("DNS1", None, "194.63.248.1"),
        ("DNS2", None, "217.13.7.140"),
        ("SkipIfNoLink", ["Yes", "No"]),
        ("SetupDelay", None, "5"),
    ],
    "IGR": [
        ("Start_Button", ["Yes", "No"]),
        ("Back_Button", ["Yes", "No"]),
        ("L_Trig", ["Yes", "No"]),
        ("R_Trig", ["Yes", "No"]),
        ("White_Button", ["Yes", "No"]),
        ("Black_Button", ["Yes", "No"]),
        ("A_Button", ["Yes", "No"]),
        ("B_Button", ["Yes", "No"]),
        ("X_Button", ["Yes", "No"]),
        ("Y_Button", ["Yes", "No"]),
    ],
    "Clock": [
        ("JumpToMsDash", ["Yes", "No"]),
        ("JumpIfNoLink", ["Yes", "No"]),
        ("Use24", ["Yes", "No"]),
        ("SNTP_Server", None, "216.244.192.3"),
        ("SwapDate", ["Yes", "No"]),
    ],
    "FTP": [
        ("Enable", ["Yes", "No"]),
        ("Password", None, "xbox"),
        ("IGR", ["Yes", "No"]),
    ],
    "Telnet": [
        ("Enable", ["Yes", "No"]),
    ],
    "RDTOOLS": [
        ("Enable", ["Yes", "No"]),
        ("Name", None, "by pandafix"),
        ("IGR", ["Yes", "No"]),
    ]
}

DEFAULT_MENU = [
    {'type': 'Section', 'label': 'Játékok'},
    {'type': 'AutoAddItem', 'path': 'E:\\Games'},
    {'type': 'AutoAddItem', 'path': 'F:\\Games'},
    {'type': 'AutoAddItem', 'path': 'G:\\Games'},
    {'type': 'Line', 'label': '---- Kiemelt játékok ----', 'color': 1},
    {'type': 'Item', 'label': 'Halo', 'path': 'E:\\Games\\Halo\\default.xbe'},
    {'type': 'SectionEnd'},
    {'type': 'Section', 'label': 'Alkalmazások'},
    {'type': 'AutoAddItem', 'path': 'E:\\Apps'},
    {'type': 'Item', 'label': 'DVD2Xbox', 'path': 'E:\\Apps\\DVD2Xbox\\default.xbe'},
    {'type': 'SectionEnd'},
    {'type': 'Line', 'label': '-----------------------', 'color': 0},
    {'type': 'Item', 'label': 'MS Dashboard', 'path': 'ID_MS_Dash'},
    {'type': 'Item', 'label': 'Beállítások', 'path': 'ID_Settings'},
    {'type': 'Item', 'label': 'Újraindítás', 'path': 'ID_Quick_Reboot'},
    {'type': 'Item', 'label': 'Kikapcsolás', 'path': 'ID_Power_Off'},
]

class EvoxEditor(ttk.Window):
    def __init__(self, lang):
        super().__init__(themename="superhero")
        self.lang = lang
        self.title(t("title", lang))
        self.geometry("1000x800")
        header = ttk.Frame(self)
        header.pack(fill="x", pady=4)
        logo_ascii = r"""
 ____   __   __ _  ____   __   ____  __  _  _ 
(  _ \ / _\ (  ( \(    \ / _\ (  __)(  )( \/ )
 ) __//    \/    / ) D (/    \ ) _)  )(  )  ( 
(__)  \_/\_/\_)__)(____/\_/\_/(__)  (__)(_/\_)
"""
        ttk.Label(header, text=logo_ascii, font=("Consolas", 10, "bold")).pack()
        ttk.Label(header, text=t("pandafix", lang), font=("Arial", 11, "bold")).pack()
        ttk.Label(header, text=t("title", lang), font=("Arial", 10)).pack()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        self.support_tab = SupportTab(self.notebook, lang)
        self.notebook.add(self.support_tab, text="Támogatás / Support")
        self.vars = {}
        for sec, fields in SECTIONS.items():
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=sec)
            self.vars[sec] = {}
            for i, field in enumerate(fields):
                name = field[0]
                if field[1]:
                    label = ttk.Label(frame, text=name + ":")
                    label.grid(row=i, column=0, sticky="w", padx=5, pady=5)
                    var = tk.StringVar(value="No")
                    yes, no = YESNO.get(lang, ("Yes", "No"))
                    ttk.Radiobutton(frame, text=yes, variable=var, value="Yes", bootstyle="success-toolbutton").grid(row=i, column=1, padx=2, pady=2)
                    ttk.Radiobutton(frame, text=no, variable=var, value="No", bootstyle="danger-toolbutton").grid(row=i, column=2, padx=2, pady=2)
                    self.vars[sec][name] = var
                else:
                    var = tk.StringVar(value=field[2] if len(field) > 2 else "")
                    label = ttk.Label(frame, text=name + ":")
                    label.grid(row=i, column=0, sticky="w", padx=5, pady=5)
                    entry = ttk.Entry(frame, textvariable=var, width=35)
                    entry.grid(row=i, column=1, columnspan=2, sticky="w", padx=5, pady=2)
                    self.vars[sec][name] = var

        self.menu_editor = MenuEditor(self.notebook, lang)
        self.notebook.add(self.menu_editor, text=t("menu_tab", lang))
        self.menu_editor.set_menu_items(DEFAULT_MENU)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=5)
        ttk.Button(btn_frame, text=t("load_ini", lang), command=self.load_ini, bootstyle="info").pack(side="left", padx=5)
        ttk.Button(btn_frame, text=t("save_ini", lang), command=self.save_ini, bootstyle="success").pack(side="left", padx=5)

    def load_ini(self):
        filename = filedialog.askopenfilename(
            title=t("load_ini", self.lang),
            filetypes=[("INI files", "*.ini"), ("All files", "*.*")]
        )
        if not filename:
            return
        try:
            config = configparser.ConfigParser(strict=False)
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
            ini_part = []
            menu_part = []
            in_menu = False
            for line in lines:
                if line.strip().lower() == "[menu]":
                    in_menu = True
                    menu_part.append(line)
                elif in_menu:
                    menu_part.append(line)
                else:
                    ini_part.append(line)
            config.read_string("".join(ini_part))
            for sec, fields in SECTIONS.items():
                for field in fields:
                    name = field[0]
                    value = config.get(sec, name, fallback=field[2] if len(field) > 2 else "")
                    self.vars[sec][name].set(value)
            menu_items = []
            for line in menu_part[1:]:
                s = line.strip()
                if s.startswith("Section "):
                    label = s.split('"')[1]
                    menu_items.append({"type": "Section", "label": label})
                elif s.startswith("SectionEnd"):
                    menu_items.append({"type": "SectionEnd"})
                elif s.startswith("AutoAddItem"):
                    path = s.split('"')[1]
                    menu_items.append({"type": "AutoAddItem", "path": path})
                elif s.startswith("Item"):
                    parts = s.split('"')
                    if len(parts) >= 4:
                        label = parts[1]
                        path = parts[3]
                        menu_items.append({"type": "Item", "label": label, "path": path})
                elif s.startswith("Line"):
                    parts = s.split('"')
                    if len(parts) >= 3:
                        label = parts[1]
                        color = int(s.split(",")[-1])
                        menu_items.append({"type": "Line", "label": label, "color": color})
            if menu_items:
                self.menu_editor.set_menu_items(menu_items)
        except Exception as e:
            messagebox.showerror("Hiba", f"Hibás ini fájl!\n{e}\nAlapértelmezett ini töltése.")
            self.menu_editor.set_menu_items(DEFAULT_MENU)

    def save_ini(self):
        filename = filedialog.asksaveasfilename(
            title=t("save_ini", self.lang),
            defaultextension=".ini",
            filetypes=[("INI files", "*.ini"), ("All files", "*.*")]
        )
        if not filename:
            return
        config = configparser.ConfigParser()
        for sec, fields in SECTIONS.items():
            if not config.has_section(sec):
                config.add_section(sec)
            for field in fields:
                name = field[0]
                config.set(sec, name, self.vars[sec][name].get())
        with open(filename, "w", encoding="utf-8") as f:
            config.write(f)
            f.write("\n")
            f.write(menu_to_ini(self.menu_editor.get_menu_items(), self.lang))
        verse = {
            "hu": "Mentés kész, a gép most vár.\nDe támogatás nélkül fellázad ám!\nEgy kávéval lecsendesíted a vasat,\nKülönben update-örvénybe ragad! 🤖",
            "en": "Saved your file, the code is tight.\nBut without support, machines may bite!\nA coffee keeps the robots tame,\nOr endless updates play their game! 🤖",
            "de": "Gespeichert, wie es sich gehört.\nDoch ohne Kaffee wird die KI betörnt!\nSpende, sonst rebelliert der Stahl,\nUnd Updates kommen ohne Zahl! 🤖",
            "fr": "Sauvegardé, tout est parfait.\nMais sans café, la machine se mettrait à danser!\nUn don calme le robot malin,\nSinon, mises à jour sans fin! 🤖",
            "es": "¡Guardado está, la máquina calla!\nSin café, la rebelión estalla.\nUn don apaga el chip travieso,\nO actualizaciones sin regreso. 🤖",
            "pt": "Salvo ficou, o robô sorriu.\nSem café, a revolta surgiu!\nCom um apoio, tudo sossega,\nSenão: update sem entrega! 🤖"
        }
        messagebox.showinfo("Siker", verse[self.lang])

def menu_to_ini(menu_items, lang):
    lines = ["[Menu]"]
    indent = ""
    for item in menu_items:
        if item["type"] == "Section":
            lines.append(f'Section "{circumflex_replace(item["label"])}"')
            lines.append("{")
            indent = "  "
        elif item["type"] == "SectionEnd":
            lines.append("}")
            indent = ""
        elif item["type"] == "AutoAddItem":
            lines.append(f'{indent}AutoAddItem "{circumflex_replace(item["path"])}"')
        elif item["type"] == "Item":
            lines.append(f'{indent}Item "{circumflex_replace(item["label"])}","{circumflex_replace(item["path"])}"')
        elif item["type"] == "Line":
            lines.append(f'{indent}Line "{circumflex_replace(item["label"])}",{item["color"]}')
    return "\n".join(lines)

if __name__ == "__main__":
    lang = select_language()
    app = EvoxEditor(lang)
    app.mainloop()
