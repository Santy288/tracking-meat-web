import time
from web3 import Web3
from celery import shared_task


@shared_task(name='tasks.check_transactions', ignore_result=False)
def check_transactions(txId):
    from trackingPlatform.models import Lot
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/922ed38024ab46e3bb7e73785e8bcd7b'))
    check_status = False
    expire_time = 60*30
    start = time.time()
    end = time.time()
    state = 0
    while end - start <= expire_time and state == 0:
        try:
            state = w3.eth.get_transaction_receipt(txId)['status']
        except:
            pass

        end = time.time()
        if state != 0:
            check_status = True
        time.sleep(5)

    lot = Lot.objects.filter(txId=txId)
    if check_status:
        lot.update(state="APPROVED")
    else:
        lot.delete()
