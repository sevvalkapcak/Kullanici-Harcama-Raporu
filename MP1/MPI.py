import tkinter.filedialog as fd
import tkinter as tk

from LabIII import VisualInterface as VI
import pyexcel as pe


class ListeEkrani(VI):
    """ VisualInterface sinifindan (LABIII) turetilen ListeEkrani
    """

    def __init__(self, parent):
        super().__init__(parent)
    
    def initUI(self):
        """ Visual interface sinifinin initUI fonksiyonunun genisletilmis hali.

            Parent sinifdan butun degiskenleri ve butonlari kullanip (super), ustune excel'e aktarma butonunu ekledik
        """
        super().initUI()
        self.buton_excel = tk.Button(self, text="2Excel", command=self.excel_kaydet)
        self.buton_excel.pack(side=tk.RIGHT)
    
    def excel_kaydet(self):
        """ Excel dosyasina iceri aktarilmis listeyi aktarir.
        """
        records = []
        for harcama in self.harcamalar.values():
            records.append({'veri': harcama})

        pe.save_as(records=records, dest_file_name='output.xls')

        


class GirisEkrani(tk.Frame):
    
    def __init__(self, parent, liste_ekrani, kategoriler):
        """ Giris Ekrani icin __init__ tanimi.

            Daha once olusturulmus liste ekranina yeni degerler girebilmek icin arguman olarak aliyor.

            Args:
                parent: root tk nesnesi
                liste_ekrani: daha onceden yaratilmis listeekrani nesnesi
                kategoriler: Kategori listesi
        """
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.liste_ekrani = liste_ekrani
        self.kategoriler = kategoriler
        self.initGui()

    def initGui(self):
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.var_tarih =  tk.StringVar()
        self.var_isim =  tk.StringVar()
        self.var_miktar =  tk.StringVar()
        self.text_tarih = tk.Entry(self, textvariable = self.var_tarih)
        self.text_isim = tk.Entry(self, textvariable = self.var_isim)
        self.text_miktar = tk.Entry(self, textvariable = self.var_miktar)
        self.list_kategori = tk.Listbox(self, selectmode="single")
        self.ekle_buton = tk.Button(self, text="Ekle", command=self.girdi_oku)
        self.label_tarih = tk.Label(self, text="Tarih Ekle:")
        self.label_isim = tk.Label(self, text="Isim Ekle:")
        self.label_kategori = tk.Label(self, text="Kategori Sec:")
        self.label_miktar = tk.Label(self, text="Miktar Ekle:")

        for i, v in enumerate(self.kategoriler):
            self.list_kategori.insert(i,v)

        # Yukseklik gereginden daha buyuk olmasin
        self.list_kategori.config(height=0)

        self.pack(fill=tk.BOTH,  expand=True)

        row_no_ilk = 1
        row_no_iki = 2
        self.label_tarih.grid(row = row_no_ilk, column = 0)
        self.text_tarih.grid(row = row_no_iki, column=0, sticky="EW")

        self.label_isim.grid(row = row_no_ilk, column = 1)
        self.text_isim.grid(row = row_no_iki, column=1)

        self.label_kategori.grid(row = row_no_ilk, column = 2)
        self.list_kategori.grid(row = row_no_iki, column=2)

        self.label_miktar.grid(row = row_no_ilk, column = 3)
        self.text_miktar.grid(row = row_no_iki, column=3)

        self.ekle_buton.grid(row = row_no_iki, column=4)

        
    def girdi_oku(self):
        self.secili = self.kategoriler[self.list_kategori.curselection()[0]]
        serit = "{}, {}, {}, {}".format(self.var_tarih.get(), self.var_isim.get(), self.secili, self.var_miktar.get())
        self.liste_ekrani.lb.insert(tk.END, serit)
        self.text_tarih.delete(0, 'end')
        self.text_isim.delete(0, 'end')
        self.text_miktar.delete(0, 'end')

class App(tk.Tk):

    def __init__(self):
        kategoriler = ["Yiyecek", "Icecek", "Giyim", "Ev", "Elektronik"]
        root = tk.Tk()
        root.title("Harcama Raporu")
        root.geometry("600x350+300+300")
        liste_ekrani = ListeEkrani(root)
        GirisEkrani(root, liste_ekrani, kategoriler)
        
        
        root.mainloop()

def main():
  
    App()

main()





