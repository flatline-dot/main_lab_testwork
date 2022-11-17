import csv
from datetime import datetime


def import_data(path):
    with open (path, 'r', encoding='utf-8') as f:
        fields = [
            'client_name', 'client_org', '№', 'sum', 'date', 'service'
        ]
        reader = csv.DictReader(f, fieldnames=fields, delimiter=',', )
        return [i for i in reader][1:]


class Validate():
    def __init__(self, data):
        self.data = data

    def valid_sum(self):
        if isinstance(self.data['sum'], int):
            return True
        else:
            try:
                self.data['sum'] = int(self.data['sum'])
                return True
            except:
                return False

    def valid_service(self):
        if  not self.data['service'] or self.data['service'] == '-':
            return False
        return True
    
    def valid_date(self):

        try:
            self.data['date'] = datetime.strptime(self.data['date'], "%d.%m.%Y")
            return True
        except:
            return False

    def valid_num(self):
        print(self.data['№'])
        if isinstance(self.data['№'], int):
            return True
        else:
            try:
                self.data['№'] = int(self.data['№'])
                return True
            except:
                return False

    def valid_client_org(self):
        if self.data['client_name'] and self.data['client_org']:
            return True
        return False

    def process(self):
        return all([self.valid_sum(),
                    self.valid_service(),
                    self.valid_date(),
                    self.valid_num(),
                    self.valid_client_org()
                   ]
        )

test = import_data('C:\\Project\\main_lab_testwork\\app\\bills.csv')
a = Validate(test[1]).process()
print(a)



    

    

