import json,sys,traceback
p=r'd:\workes\BoxJs-Hub\store.json'
try:
    with open(p,'r',encoding='utf-8') as f:
        data=json.load(f)
    print('VALID', len(data))
except Exception as e:
    traceback.print_exc()
    sys.exit(1)
