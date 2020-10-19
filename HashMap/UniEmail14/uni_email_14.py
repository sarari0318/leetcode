class Solution:
    def numUniqueEmails(self, emails):
        
        if emails is None:
            return 0
        
        mails = set()
        
        for email in emails:
            local_name, domain_name = email.split('@')[0], email.split('@')[1]
            if "+" in local_name:
                local_name = local_name.split("+")[0]
            if "." in local_name:
                local_name = ''.join(local_name.split('.'))
            mail = local_name + "@" + domain_name
            mails.add(mail)
            
        return len(mails)