from app import create_app
import os
import json

app = create_app()

if __name__ == "__main__":
    #app.config['SERVER_NAME'] = '0.0.0.0:5000'
    #with app.app_context():
        #f = open('resources/crm_api_postman_v1.json', 'w')
        #f.write(json.dumps(api.as_postman(urlvars=False, swagger=True)))
        #f = open('resources/crm_api_swagger.json', 'w')
        #f.write(json.dumps(api.__schema__))

    app.run(
        host='0.0.0.0',
        port='5000',
        debug=True
    )