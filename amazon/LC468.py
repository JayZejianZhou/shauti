class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        # check if it's IPV4 or IPV6
        add_type = ""
        for i in range(len(IP)):
            if IP[i] == ".": 
                add_type = "IPv4"
                break
            if IP[i] == ":":
                add_type = "IPv6"
                break
        if not add_type: return "Neither"
        
        ip_list = IP.split(".") if add_type=="IPv4" else IP.split(":")
        
        if add_type=="IPv4" and not len(ip_list) == 4: return "Neither"
        if add_type=="IPv6" and not len(ip_list) == 8: return "Neither"
        
        if add_type=="IPv4": 
            for i in range(len(ip_list)):
                if not ip_list[i]: return "Neither"
                if ip_list[i][0]=="0" and len(ip_list[i])>1: return "Neither"                
                for jt in ip_list[i]:
                    if jt<"0" or jt>"9": return "Neither"
                if int(ip_list[i])<0 or int(ip_list[i])>255: return "Neither"
        
        if add_type=="IPv6":
            for i in range(len(ip_list)):
                # if ip_list[i][0]=="0": return "Neither"
                if len(ip_list[i])<1 or len(ip_list[i])>4: return "Neither"
                for jt in ip_list[i]:
                    if not ((jt>="0" and jt<="9") or (jt>="a" and jt<="f") or (jt>="A" and jt<="F")): return "Neither"
        
        return add_type