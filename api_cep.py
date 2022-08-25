import requests

def validate_cep(field):
    cep = "".join(field.replace("-"," ").split())
    if cep.isdigit() and len(cep) == 8:
       return cep
    raise Exception('CEP "{field}" Format Invalid'.format(field=field))



cep = validate_cep('60841130')
api_cep_url = 'https://example.api.findcep.com/v1/cep/{cep}.json'
headers = {'Referer': 'https://your-site.com'}

response = requests.get(api_cep_url.format(cep=cep), headers=headers)
print(response.json())