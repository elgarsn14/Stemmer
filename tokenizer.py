import re

Text = """Kami belajar tanpa LELAH tanpa NGELUH
kami& tidak tidak tidur teratur bukan karena game (wkwk)
kami kuliah dengan sangat giat.
kami tega mengorbankan masa muda.
itu karena kami ingin kelak istri dan anak kami bahagia"""

def tokenize (text):
    text = text.lower()
    # jika udah pake lower, ga pake flags gpp
    text = re.sub(r'[^a-z0-9 -]', ' ', text, flags = re.IGNORECASE|re.MULTILINE)
    text = re.sub(r'( +)', ' ', text, flags = re.IGNORECASE|re.MULTILINE)
    tokens = text.split(" ")
    return tokens

print(tokenize(Text))