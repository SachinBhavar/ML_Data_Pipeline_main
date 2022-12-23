
import os

#cloud api details
API_KEY ="3ZIFEBVHYYI6E6TM"# os.getenv('API_KEY',None)
API_SECRET_KEY ="64CI6nWCXrcQG3aO/1/akLRJ3fDMw4+LmQTlmSLHFZcpahUuWZbPO4LDolCem2Y6"# os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER ="pkc-6ojv2.us-west4.gcp.confluent.cloud:9092"# os.getenv('BOOTSTRAP_SERVER',None)


#Authentication related variables
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)

SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

#schema related variables
ENDPOINT_SCHEMA_URL  ="https://psrc-znpo0.ap-southeast-2.aws.confluent.cloud"# os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY = "4QRMKZMFERF6FLUV"#os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET ="nQ24RBCH18FImBn8D2L8s5P4GZQkUzkPQJQK+2lzS088VWPc2ZYNsYX7yHdOIWuU" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

