from typing import Union, List

from fastapi import FastAPI, Depends
from .utils import import_data, Validate
from .dependencies import get_session
from .models import Bill, Org, Service
from sqlalchemy import select
from sqlalchemy.orm import Session
from .schemas import BillModel
app = FastAPI()



@app.get('/dataload')
async def load_data(session: Session = Depends(get_session)):
    bills = import_data('C:\\Project\\main_lab_testwork\\app\\bills.csv')

    for bill in bills:
        if not Validate(bill).process():
            continue

        with session.begin():
            org = False
            service = False

            org_check = (session.execute(select(Org).where(Org.org_name == bill['client_org']))).fetchone()
            service_check = (session.execute(select(Service).where(Service.service_title == bill['service']))).fetchone()

            if org_check:
                org = org_check[0].id

            if service_check:
                service = service_check[0].id

            if not org:
                new_org = Org(org_name=bill['client_org'])
                session.add(new_org)
                session.flush()
                org = new_org.id
                

            if not service:
                new_service = Service(service_title=bill['service'])
                session.add(new_service)
                session.flush()
                service = new_service.id
                

            bill['client_org'] = org
            bill['service'] = service
            bill['num'] = bill.pop('№')

            try:
                session.add(Bill(**bill))
                session.commit()
            except:
                print('UNIQUE ERROR')

    return {'status': 'data loaded'}


@app.get('/bills', response_model=List[BillModel])
def get_bills(client: Union[str, None] = None, org: Union[str, None] = None, session: Session = Depends(get_session)):
    query = session.query(Bill).join(Org).join(Service)
    if client:
        query = query.filter(Bill.client_name == client)
    if org:
        query = query.filter(Org.org_name == org)

    result = query.all()

    response_bills = []
    for res in result:
        bill = {
            'client_name': res.client_name,
            'client_org': res.orgs.org_name,
            'num_bill': res.num,
            'sum_bill': res.sum,
            'date_bill': res.date,
            'service': res.services.service_title
        }
    
        response_bills.append(bill)

    return response_bills
