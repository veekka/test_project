from django.shortcuts import render
from .models import CreditApplication, Contract
import sqlite3


def index(request):
    return render(request, 'getidapp/index.html')


def list(request):
    list_manuf = []
    contract = request.GET['id']
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    cur.execute(f"SELECT DISTINCT m.id_manufacturer FROM getidapp_manufacturer as m WHERE m.id in "
                f"(SELECT p.id FROM getidapp_product as p WHERE p.application_id in "
                f"(SELECT ap.id FROM getidapp_creditapplication as ap WHERE ap.contract_id in "
                f"(SELECT c.id FROM getidapp_contract as c WHERE c.id={contract})));")
    results = cur.fetchall()

    for i in range(len(results)):
        list_manuf.append(results[i][0])

    return render(request, 'getidapp/list.html', {'manufacturers': list_manuf, 'contract_id': contract})