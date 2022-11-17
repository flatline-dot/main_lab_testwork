from fastapi import FastAPI, Depends
from .utils import import_data, Validate
from .dependencies import get_session, AsyncSession
from .models import Bill, Org, Service
app = FastAPI()





@app.get('/')
async def load_data(session: AsyncSession = Depends(get_session)):
    data = import_data('C:\\Project\\main_lab_testwork\\app\\bills.csv')


    for item in data:
        if not Validate(item).process():
            continue

        async with session.begin() as conn:
            org = Org(org_name='tdsdsddfdsdsfsd')
            session.add(org)
            await session.flush()



