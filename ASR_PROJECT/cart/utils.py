from datetime import date
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


def generate_receipt(cart_items, total, username):
    template = get_template('cart/receipt.html')
    context = {'cart_items': cart_items, 'total': total, 'fecha': date.today()}
    html = template.render(context)

    file_name = f'media/receipts/receipt{username.__str__()}.pdf'
    file = open(file_name, 'w+b')

    pisa.CreatePDF(html, dest=file)
    file.close()
