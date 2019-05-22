from chalice import Chalice

app = Chalice(app_name='uuid-api')

uuid_dict = {'01122334-4556-6778-899A-ABBCCDDEEFF0': {'car_no': '1000'},
             '00000000-0000-0000-0000-000000000000': {'car_no': '9999'}}
car_no_dict = {'1000': {'uuid':'01122334-4556-6778-899A-ABBCCDDEEFF0'},
               '9999': {'uuid':'00000000-0000-0000-0000-000000000000'}}

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/info_from_uuid/{uuid}')
def info_from_uuid(uuid):
    return uuid_dict.get(uuid, {'car_no':'-'})

@app.route('/info_from_car_no/{car_no}')
def info_from_car_no(car_no):
    return car_no_dict.get(car_no,{'uuid':'-'})
