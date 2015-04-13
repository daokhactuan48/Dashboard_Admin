import requests
import json
from classall import *
# Lay token cua user admin trong tenant admin
def gettoken():
        url = 'http://172.16.69.70:35357/v2.0/tokens'
        #data = {"auth": {"tenantName":"admin","passwordCredentials":{"username":"admin","password":"Welcome123"}}}
        tenant = {}
        nametenant = "admin"
        tenant['tenantName'] =nametenant 
        user = {"username":"admin","password":"Welcome123"}
        tenant['passwordCredentials'] = user
        data  = {}
        data["auth"] = tenant
        a = requests.post(url,json.dumps(data),headers = {'Content-Type':'application/json'})
        if a.status_code !=200:
                raise Exception("Platform9 Login returned %d, body: %s" %(a.status_code,a.text))
        else:
                response = a.json()
                token = response['access']['token']['id']
                return token
# Tra ve list tenant cua. List nay luu tru duoi dang class tenant
def gettenant():
        listtenant = []
        url = 'http://172.16.69.70:35357/v2.0/tenants'
        token = gettoken()
        response = requests.get(url,headers = {'X-Auth-Token':token,'Content-Type':'application/json'})
        repon = response.json()['tenants']
        j = 0
        for i in range(0,len(repon)):
            if repon [i]['name'] != 'invisible_to_admin' and repon [i]['name'] != 'service':
                tenanta = tenant(j,repon[i]['enabled'],repon[i]['description'],repon[i]['id'],repon[i]['name'])
	        listtenant.append(tenanta)
                j = j + 1
        return listtenant

#for tenant in gettenant:
#        print str(tenant.getstt()) + ". " + tenant.getname()

# Lay token user admin tren tenant khac
def gettokentenant(tenantname):
    url = 'http://172.16.69.70:35357/v2.0/tokens'
        #data = {"auth": {"tenantName":"admin","passwordCredentials":{"username":"admin","password":"Welcome123"}}}
    tenant = {}
    tenant['tenantName'] = tenantname 
    user = {"username":"admin","password":"Welcome123"}
    tenant['passwordCredentials'] = user
    data  = {}
    data["auth"] = tenant
    a = requests.post(url,json.dumps(data),headers = {'Content-Type':'application/json'})
    if a.status_code !=200:
        raise Exception("Platform9 Login returned %d, body: %s" %(a.status_code,a.text))
    else:
        response = a.json()
        token = response['access']['token']['id']
        return token

def getlistserver():
    listserver = []
    for idtenant in gettenant():
    	token = gettokentenant(idtenant.getname())
        url = "http://172.16.69.70:8770/v2/" + str(idtenant.getid()) + "/servers/detail"
        response = requests.get(url,headers = {'X-Auth-Token':token,'Content-Type':'application/json'})
        repon = response.json()['servers']
        for i in range(0,len(repon)):
            servera = server(repon[i]['id'],repon[i]['user_id'],repon[i]['name'],repon[i]['tenant_id'],repon[i]['image']['id'])
            listserver.append(servera)
    return listserver
        #for i in range(0,len(repon)):
        #    print repon[i]['name']	

def getlistvnc():
    listserver = getlistserver()
    listvnc = []
    for idtenant in gettenant():
        token = gettokentenant(idtenant.getname())
        for itemserver in listserver:
            if itemserver.gettenantid() == idtenant.getid():
                url = "http://172.16.69.70:8770/v2/" + itemserver.gettenantid() + "/servers/" + itemserver.getid() + "/action"
                data = {"os-getVNCConsole":{"type":"novnc"}}
                response = requests.post(url,json.dumps(data),headers = {'X-Auth-Token':token,'Content-Type':'application/json'})
                repon = response.json()["console"]
                #tam ={"tenmay":itemserver.getname(),"vnc":}
                tam = vnc(repon['url'],itemserver.getname())
                listvnc.append(tam)           
    return listvnc        

#for item in getlistvnc():
#    print item.getservername()

def getlistnetwork():
    lstsubnet  = []
    token = gettokentenant("admin")
    url = "http://172.16.69.70:9696/v2.0/subnets"
    response = requests.get(url,headers = {'X-Auth-Token':token,'Content-Type':'application/json'})
    repon = response.json()['subnets']
    for i in range(0,len(repon)):
        subnet = subnets(i,repon[i]['name'],repon[i]['id'],repon[i]['enable_dhcp'],repon[i]['network_id'],repon[i]['tenant_id'],repon[i]['allocation_pools'][0]['start'],repon[i]['allocation_pools'][0]['end'],repon[i]['gateway_ip'],repon[i]['cidr'])
        lstsubnet.append(subnet)
    return lstsubnet

#for i in getlistnetwork():
#    print i.getname()

def getlistimage():
    lstimage = []
    token = gettokentenant("admin")
    listtenant = gettenant()
    for tenant in listtenant:
        if tenant.getname() == "admin":
            url = "http://172.16.69.70:8770/v2/" + tenant.getid() + "/images"
            response = requests.get(url,headers = {'X-Auth-Token':token,'Content-Type':'application/json'})
            repon = response.json()['images']
            for i in range(0,len(repon)):
                image = images(i,repon[i]['id'],repon[i]['name'])
                lstimage.append(image)
            break
    return lstimage

#for image in getlistimage():
#    print image.getimageid()

def getlistflavor():
    lstflavor = []
    token = gettokentenant("admin")
    listtenant = gettenant()
    for tenant in listtenant:
        if tenant.getname() == "admin":
            url = "http://172.16.69.70:8770/v2/" + tenant.getid() + "/flavors/detail"
            response = requests.get(url,headers = {'X-Auth-Token':token,'Content-Type':'application/json'})
            repon = response.json()['flavors']
            for i in range(0,len(repon)):
                flavor = flavors(i,repon[i]['name'],repon[i]['ram'],repon[i]['vcpus'],repon[i]['disk'],repon[i]['id'])
                lstflavor.append(flavor)
            break
    return lstflavor

def createmayao(tenmayao,flavor,image,network,idtenant,count):
    for tenant in gettenant():
	if tenant.getid() == idtenant:
	    url = "http://172.16.69.70:8770/v2/" + tenant.getid() + "/servers"
	    token = gettokentenant(tenant.getname())
	    break
    listserver = {}
    listserver['name'] = tenmayao
    listserver['imageRef'] = image
    listserver['flavorRef'] = flavor
    listserver['max_count'] = count
    listserver['min_count'] = 1
    dictnetwork = {}
    dictnetwork['uuid'] = network
    listserver['networks'] = [dictnetwork]
    dictsecurity = {}
    dictsecurity['name'] = "default"
    listserver['security_groups'] = [ dictsecurity ]
    listcreateserver = {}
    listcreateserver['server'] = listserver
    response = requests.post(url,json.dumps(listcreateserver),headers = {'X-Auth-Token':token,'Content-Type':'application/json'})
    if response.status_code != 202:
        return False
    else: 
        return response.json()['server']['adminPass']
