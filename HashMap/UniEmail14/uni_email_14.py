class Solution:
    def numUniqueEmails(self, emails):

        '''
        Parameters
        ----------
            emails: List[str]
        Returns
        -------
            int
            ⇨ return the number of different addresses that actually receive mails.
        '''
        
        # 固有のアドレスを記録する
        mails = set()
        
        for email in emails:
            # local_nameとdomain_nameに分割
            local_name, domain_name = email.split('@')[0], email.split('@')[1]
            # '+'が存在すれば、
            if '+' in local_name:
                # '+'以降のlocal_nameの部分を省く
                local_name = local_name.split('+')[0]
            # '.'が存在すれば、
            if '.' in local_name:
                # '.'を取り除く
                local_name = ''.join(local_name.split('.'))
            # emailアドレスの形式に変換
            mail = local_name + '@' + domain_name
            mails.add(mail)
            
        return len(mails)