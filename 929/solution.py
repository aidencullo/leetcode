class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def remove_plus(s):
            i = s.find('+')
            if i == -1:
                return s
            return s[:i]

        def clean(email):
            local, domain = email.split('@')
            local_without_periods = local.replace('.', '')
            local_without_plus = remove_plus(local_without_periods)
            cleaned_email = local_without_plus + '@' + domain
            return cleaned_email

        cleaned = set(map(clean, emails))
        return len(cleaned)
