class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_count = collections.defaultdict(int)
        for it in cpdomains:
            time, domain = it.split()
            domain_count[domain] += int(time)
            
            while '.' in domain:
                domain = domain[domain.index('.')+1:]
                domain_count[domain] += int(time)
                
        return [str(v) + ' ' + d for d, v in domain_count.items()]