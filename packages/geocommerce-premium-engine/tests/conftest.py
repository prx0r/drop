import os,tempfile
DB=os.path.join(tempfile.gettempdir(),'geocommerce_pytest.db')
os.environ['GEOCOMMERCE_DB']=DB
os.environ['ADMIN_TOKEN']='test-admin'
try: os.remove(DB)
except FileNotFoundError: pass
