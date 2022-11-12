
from PIL import Image, ImageTk

def get_photo_image(path: str, new_size):

    return ImageTk.PhotoImage(Image.open(path).resize(new_size))

#Mit dieser Funktion wird das Bild der Uno Karte erzeugt, sie wird aber erst wenn sie in Main.py aufgerufen wird wirksam


