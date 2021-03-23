import pyshark
from datetime import datetime



cap = pyshark.FileCapture('pcap_File',only_summaries=True ,display_filter='Filtro')




def indetifier(cap, name,data_do_log):
    #print(cap[100].protocol)
    TCP=0
    DNP3=0
    PANA=0
    UDP=0
    ICMPv6=0
    SNMP=0
    UAUDP=0

    for pkt in cap:
        if pkt.protocol == 'TCP':
            #print(pkt.protocol)
            TCP = TCP + 1
        elif pkt.protocol == 'ICMPv6':
            #print(pkt.protocol)
            ICMPv6 = ICMPv6 + 1
        elif pkt.protocol == 'DNP 3.0':
            #print(pkt.protocol)
            DNP3 = DNP3 + 1
        elif pkt.protocol == 'UDP':
            #print(pkt.protocol)
            UDP = UDP + 1
        elif pkt.protocol == 'SNMP':
            #print(pkt.protocol)
            SNMP = SNMP + 1
        elif pkt.protocol == 'UAUDP':
            #print(pkt.protocol)
            UAUDP = UAUDP + 1
    
    print("Contagem no log ", name)
    print("Quantidade de pacotes TCP:", TCP)
    print("Quantidade de pacotes ICMPv6:", ICMPv6)
    print("Quantidade de pacotes DNP3:", DNP3)
    print("Quantidade de pacotes UDP:", UDP)
    print("Quantidade de pacotes SNMP:", SNMP)
    print("Quantidade de pacotes UAUDP:", UAUDP)


    with open("File_" + name + str(datetime.today().strftime('_%Y_%m_%d')) + "_" + data_do_log + ".txt",'w') as out:
        #out.write("teste")
        out.write("Quantidade de pacotes TCP:" + str(TCP))
        out.write("\n")
        out.write("Quantidade de pacotes ICMPv6:" + str(ICMPv6))
        out.write("\n")
        out.write("Quantidade de pacotes DNP3:" + str(DNP3))
        out.write("\n")
        out.write("Quantidade de pacotes UDP:" + str(UDP))
        out.write("\n")
        out.write("Quantidade de pacotes SNMP:" +str(SNMP))
        out.write("\n")
        out.write("Quantidade de pacotes UAUDP:" +str(UAUDP))
    out.close()







def main():

    data_do_log=input("Qual a data do log(dd_mm) ? ")

    indetifier(cap,"Nome_log",data_do_log)



if __name__=="__main__":
    main()