#!/usr/bin/python
from pysimplesoap.client import SoapClient
from time import gmtime, strftime
import threading
import sys
from time import sleep

path = "/opt/fritzmonitor/log/fritz/"
logfile = path+strftime("%Y-%m-%d", gmtime())+"_fritz.log"
fritzbox = "192.168.178.1"
port = "49000"

def wancommonifc(fritzbox, port, debug):
    location = 'http://'+fritzbox+':'+port+'/igdupnp/control/WANCommonIFC1'
    namespace = 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1'
    action = 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1#'

    client = SoapClient(location, action, namespace, trace=debug)

    gclp = client.GetCommonLinkProperties()
    newlayer1upstreammaxbitrate = int(gclp.GetCommonLinkPropertiesResponse.NewLayer1UpstreamMaxBitRate)
    newlayer1downstreammaxbitrate = int(gclp.GetCommonLinkPropertiesResponse.NewLayer1DownstreamMaxBitRate)
    newwanaccesstype = str(gclp.GetCommonLinkPropertiesResponse.NewWANAccessType)
    newphysicallinkstatus = str(gclp.GetCommonLinkPropertiesResponse.NewPhysicalLinkStatus)

    gai = client.GetAddonInfos()
    newbytesendrate = int(gai.GetAddonInfosResponse.NewByteSendRate)
    newbytereceiverate = int(gai.GetAddonInfosResponse.NewByteReceiveRate)
    newpacketsendrate = int(gai.GetAddonInfosResponse.NewPacketSendRate)
    newpacketreceiverate = int(gai.GetAddonInfosResponse.NewPacketReceiveRate)
    newtotalbytessent = int(gai.GetAddonInfosResponse.NewTotalBytesSent)
    newtotalbytesreceived = int(gai.GetAddonInfosResponse.NewTotalBytesReceived)
    newautodisconnecttime = str(gai.GetAddonInfosResponse.NewAutoDisconnectTime)
    newidledisconnecttime = str(gai.GetAddonInfosResponse.NewIdleDisconnectTime)
    newdnsserver1 = str(gai.GetAddonInfosResponse.NewDNSServer1)
    newdnsserver2 = str(gai.GetAddonInfosResponse.NewDNSServer2)
    newvoipdnsserver1 = str(gai.GetAddonInfosResponse.NewVoipDNSServer1)
    newvoipdnsserver2 = str(gai.GetAddonInfosResponse.NewVoipDNSServer2)
    newupnpcontrolenabled = int(gai.GetAddonInfosResponse.NewUpnpControlEnabled)
    newroutedbridgedmodeboth = int(gai.GetAddonInfosResponse.NewRoutedBridgedModeBoth)

    msg = "newlayer1upstreammaxbitrate="+str(newlayer1upstreammaxbitrate)+" newlayer1downstreammaxbitrate="+str(newlayer1downstreammaxbitrate)+" newwanaccesstype="+str(newwanaccesstype)+" newphysicallinkstatus="+str(newphysicallinkstatus)+" newbytesendrate="+str(newbytesendrate)+" newbytereceiverate="+str(newbytereceiverate)+" newpacketsendrate="+str(newpacketsendrate)+" newpacketreceiverate="+str(newpacketreceiverate)+" newtotalbytessent="+str(newtotalbytessent)+" newtotalbytesreceived="+str(newtotalbytesreceived)+" newautodisconnecttime="+str(newautodisconnecttime)+" newidledisconnecttime="+str(newidledisconnecttime)+" newdnsserver1="+str(newdnsserver1)+" newdnsserver2="+str(newdnsserver2)+" newvoipdnsserver1="+str(newvoipdnsserver1)+" newvoipdnsserver2="+str(newvoipdnsserver2)+" newupnpcontrolenabled="+str(newupnpcontrolenabled)+" newroutedbridgedmodeboth="+str(newroutedbridgedmodeboth)
    return msg

def getwandsllink(fritzbox, port, debug):
    location = 'http://'+fritzbox+':'+port+'/igdupnp/control/WANDSLLinkC1'
    namespace = 'urn:schemas-upnp-org:service:WANDSLLinkConfig:1'
    action = 'urn:schemas-upnp-org:service:WANDSLLinkConfig:1#'

    client = SoapClient(location, action, namespace, trace=debug)

    gdslli = client.GetDSLLinkInfo()
    NewLinkType = str(gdslli.NewLinkType)
    NewLinkStatus = str(gdslli.NewLinkStatus)
    gac = str(client.GetAutoConfig().NewAutoConfig)
    gmt = str(client.GetModulationType().NewModulationType)
    gda = str(client.GetDestinationAddress().NewDestinationAddress)
    gatme = str(client.GetATMEncapsulation().NewATMEncapsulation)
    gfcsp = str(client.GetFCSPreserved().NewFCSPreserved)

    msg = "NewLinkType="+str(NewLinkType)+" NewLinkStatus="+str(NewLinkStatus)+" GetAutoConfig="+str(gac)+" GetModulationType="+str(gmt)+" GetDestinationAddress="+str(gda)+" GetATMEncapsulation="+str(gatme)+" GetFCSPreserved="+str(gfcsp)
    return msg

def getwanipconn(fritzbox, port, debug):
    location = 'http://'+fritzbox+':'+port+'/igdupnp/control/WANIPConn1'
    namespace = 'urn:schemas-upnp-org:service:WANIPConnection:1'
    action = 'urn:schemas-upnp-org:service:WANIPConnection:1#'

    client = SoapClient(location, action, namespace, trace=debug)

    gcti = client.GetConnectionTypeInfo()
    NewConnectionType = str(gcti.NewConnectionType)
    NewPossibleConnectionTypes = str(gcti.NewPossibleConnectionTypes)
    gadt = str(client.GetAutoDisconnectTime().NewAutoDisconnectTime)
    gidt = str(client.GetIdleDisconnectTime().NewIdleDisconnectTime)
    gsi = client.GetStatusInfo()
    NewConnectionStatus = str(gsi.NewConnectionStatus)
    NewLastConnectionError = str(gsi.NewLastConnectionError)
    NewUptime = str(gsi.NewUptime)
    gnatrsips = client.GetNATRSIPStatus()
    NewRSIPAvailable = str(gnatrsips.NewRSIPAvailable)
    NewNATEnabled = str(gnatrsips.NewNATEnabled)
    geipa = str(client.GetExternalIPAddress().NewExternalIPAddress)
    geipa6 = client.X_AVM_DE_GetExternalIPv6Address()
    NewExternalIPv6Address = str(geipa6.NewExternalIPv6Address)
    NewPrefixLength = str(geipa6.NewPrefixLength)
    NewValidLifetime = str(geipa6.NewValidLifetime)
    gdnss = client.X_AVM_DE_GetDNSServer()
    NewIPv4DNSServer1 = str(gdnss.NewIPv4DNSServer1)
    NewIPv4DNSServer2 = str(gdnss.NewIPv4DNSServer2)

    msg = "NewConnectionType="+str(NewConnectionType)+" NewPossibleConnectionTypes="+str(NewPossibleConnectionTypes)+" GetAutoDisconnectTime="+str(gadt)+" GetIdleDisconnectTime="+str(gidt)+" NewConnectionStatus="+str(NewConnectionStatus)+" NewLastConnectionError="+str(NewLastConnectionError)+" NewUptime="+str(NewUptime)+" NewRSIPAvailable="+str(NewRSIPAvailable)+" NewNATEnabled="+str(NewNATEnabled)+" GetExternalIPAddress="+str(geipa)+" NewExternalIPv6Address="+str(NewExternalIPv6Address)+" NewPrefixLength="+str(NewPrefixLength)+" NewValidLifetime="+str(NewValidLifetime)+" NewIPv4DNSServer1="+str(NewIPv4DNSServer1)+" NewIPv4DNSServer2="+str(NewIPv4DNSServer2)
    return msg

def getwandsllink(fritzbox, port, debug):
    location = 'http://'+fritzbox+':'+port+'/igd2upnp/control/WANIPv6Firewall1'
    namespace = 'urn:schemas-upnp-org:service:WANIPv6FirewallControl:1'
    action = 'urn:schemas-upnp-org:service:WANIPv6FirewallControl:1#'

    client = SoapClient(location, action, namespace, trace=debug)

    gfs = client.GetFirewallStatus()
    FirewallEnabled = str(gfs.FirewallEnabled)
    InboundPinholeAllowed = str(gfs.InboundPinholeAllowed)

    msg = "FirewallEnabled="+str(FirewallEnabled)+" InboundPinholeAllowed="+str(InboundPinholeAllowed)
    return msg

def writeFile(msg, logfile):
    file = open(logfile,"a")
    file.write(msg)
    file.close

def getFritz(fritzbox, port, debug):
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    ggetwandsllink = getwandsllink(fritzbox, port, debug)
    ggetwanipconn = getwanipconn(fritzbox, port, debug)
    ggetwandsllink = getwandsllink(fritzbox, port, debug)
    wwancommonifc = wancommonifc(fritzbox, port, debug)

    msg = now+" "+ggetwandsllink+" "+ggetwanipconn+" "+ggetwandsllink+" "+wwancommonifc+"\n"
    return msg

def main():
    writeFile(getFritz(fritzbox, port, False),logfile)
    sleep(30)
    writeFile(getFritz(fritzbox, port, False),logfile)
    sys.exit(0)

if __name__ == '__main__':
    main()
