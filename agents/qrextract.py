from pyzbar.pyzbar import decode
from PIL import Image


class QRExtractionAgent:

    @staticmethod
    def extract(qr_path):

        decoded = decode(Image.open(qr_path))

        if not decoded:
            return None

        return decoded[0].data.decode("utf-8")