from django.shortcuts import render
from .models import CreditApplication, Contract


def index(request):
    return render(request, 'getidapp/index.html')

def list(request):
    list_manuf = []
    attributs = []
    contract = request.GET['id']
    if Contract.objects.filter(id_contract=contract).exists():
        con = Contract.objects.get(id_contract=contract)

        for contract_id in con.get_id.all():
            aplication = CreditApplication.objects.get(id_application=contract_id)
            for product in aplication.product_set.all():
                m = product.manufacturer_set.all()
                attr = getattr(*m, 'id_manufacturer')
                if attr not in attributs:
                    list_manuf.append(*m)
                    attributs.append(attr)

    return render(request, 'getidapp/list.html', {'manufacturers': list_manuf, 'contract_id': contract})


