class server(object):
    def __init__(self,itemid,itemmuserid,itemname,itemtenantid,itemidimage,):
        self.id = itemid
        self.userid = itemmuserid
        self.name = itemname
        self.tenantid = itemtenantid
    def getid(self):
        return self.id
    def getuserid(self):
        return self.userid
    def getname(self):
        return self.name
    def gettenantid (self):
        return self.tenantid

class vnc(object):
    def __init__(self,itemurl,servername):
        self.url = itemurl
        self.servername = servername
    def geturl(self):
        return self.url
    def getservername(self):
        return self.servername

class tenant(object):
    def __init__(self,itemstt,itemenabled,itemdescription,itemid,itemname):
        self.enabled = itemenabled
        self.description = itemdescription
        self.id = itemid
        self.name = itemname
        self.stt = itemstt   
    def getenabled(self):
        return self.enabled
    def getname(self):
        return self.name
    def getid (self):
        return self.id
    def getdescription(self):
        return self.description
    def getstt(self):
        return self.stt

class subnets(object):
    def __init__(self,itemstt,itemname,itemid,itemenable_dhcp,itemnetwork_id,itemtenant_id,itemallocation_start,itemallocation_end,itemgateway,itemcidr):
        self.name = itemname
        self.id = itemid
        self.enable_dhcp = itemenable_dhcp
        self.network_id = itemnetwork_id
        self.tenant_id = itemtenant_id
        self.allocation_start = itemallocation_start
        self.allocation_end = itemallocation_end
        self.gateway = itemgateway
        self.stt = itemstt
        self.cidr = itemcidr
    def getname(self):
        return self.name
    def getid(self):
        return self.id
    def getenable_dhcp(self):
        return self.enable_dhcp
    def getnetwork_id(self):
        return self.network_id
    def gettenant_id(self):
        return self.tenant_id
    def getallocation_start(self):
        return self.allocation_start
    def getallocation_end(self):
        return self.allocation_end
    def getgateway(self):
        return self.gateway
    def getstt(self):
        return self.stt
    def getcidr(self):
        return self.cidr

class images(object):
    def __init__(self,itemstt,itemid,itemname):
        self.stt = itemstt
        self.name = itemname
        self.imageid = itemid
    def getname (self):
        return self.name
    def getimageid(self):
        return self.imageid
    def getstt(self):
        return self.stt

class flavors(object):
    def __init__(self,itemstt,itemname,itemram,itemvcpus,itemdisk,itemid):
        self.stt = itemstt
        self.flavorname = itemname
        self.ram = itemram
        self.vcpu = itemvcpus
        self.disk = itemdisk
        self.flavorid = itemid
    def getstt(self):
        return self.stt
    def getflavorid(self):
        return self.flavorid
    def getflavorname(self):
        return self.flavorname
    def getram(self):
        return self.ram
    def getvcpu(self):
        return self.vcpu
    def getdisk(self):
        return self.disk









