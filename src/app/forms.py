"""
forms.py

Module for forms that are in use on the homepage, including the contact section
as well as the comments section for blog posts.
"""


import re


MARKDOWN = re.compile(r'[a-z]|[A-Z]|[\!\.\?\,\:\;\'\[\]\*\-\~\(\)\`\/\#\_]|\s')


def is_message_body_valid(body: str) -> bool:
    """
    Validates the input body for characters.

    Args:
        body: the body text to check.
    Returns:
        bool: True/False whether or not the validation succeeded.
    """
    for char in body:
        if MARKDOWN.search(str(char)) is None:
            return False
    return True


def is_message_title_valid(title: str) -> bool:
    """
    Validates the input title for characters.

    Args:
        title: the title text to check.
    Returns:
        bool: True/False whether or not the validation succeeded.
    """
    for char in title:
        if MARKDOWN.search(str(char)) is None:
            return False
    return True


def is_message_email_valid(email: str) -> bool:
    """
    Validates the input email for characters. The idea is to implement the 80%
    of rules which make up the specification for emails, for 'local-part'
    @'domain'.

    For 'local-part': https://en.wikipedia.org/wiki/Email_address#Local-part
    For 'domain': https://en.wikipedia.org/wiki/Email_address#Domain
    For 'ipv4': https://en.wikipedia.org/wiki/IPv6#IPv4

    Args:
        email: the email text to check.
    Returns:
        bool: True/False whether or not the validation succeeded.
    """

    # handle any members of \s for the whole email; early fail
    if re.search('[ \t\n\r\f\v]', str(email)):
        return False

    # handle multiple '@' appearances
    em_bits = email.split('@')
    if len(em_bits) != 2:
        return False

    local = em_bits[0]
    domain = em_bits[1]

    dbl_dt = r'^[^"\'].+[.][.].+[^"\']$'
    bad_dt_ld = r'^[.]+.*'
    bad_dt_nd = r'.*[.]+$'
    bad_hy_ld = r'^[-]+.*'
    bad_hy_nd = r'.*[-][.].*'
    spc_c = r'["!#$%&\'*+/=?^_`{|}~-]'
    ldh = r'[a-zA-Z0-9.-]'

    hx_c = r'[a-f0-9]{0,4}'
    cln_c0 = r'[:]{0,2}'
    cln_c1 = r'[:]{1,2}'
    ipv6_rg = r'{1,8}'

    dtcm_re = r'({s0}*[.]{s1}*){s3}'.format(s0=ldh, s1=ldh, s3=ipv6_rg)
    ipv4_re = r'\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\]'
    ipv6_re = r'\[({s0}{s1}{s2}{s3}{s4}){s5}\]'.format(s0=cln_c0,
                                                       s1=hx_c,
                                                       s2=cln_c1,
                                                       s3=hx_c,
                                                       s4=cln_c0,
                                                       s5=ipv6_rg)

    local_pt = re.compile(r'{s0}+|{s1}+'.format(s0=ldh, s1=spc_c))
    re_dbl_dt = re.compile(dbl_dt)
    local_pt_dt_ld = re.compile(bad_dt_ld)
    local_pt_dt_nd = re.compile(bad_dt_nd)
    dm_pt_hy_ld = re.compile(bad_hy_ld)
    dm_pt_hy_nd = re.compile(bad_hy_nd)
    dm_ipv4 = re.compile(ipv4_re)
    dm_ipv6 = re.compile(ipv6_re)
    dm_dtcm = re.compile(dtcm_re)

    # handle empty values
    if not local or not domain:
        return False

    # check for awkward local double dot '..' edge cases up front
    if re_dbl_dt.search(str(local)) is not None:
        return False

    # check for leading or trailing dots in local that are invalid
    if local_pt_dt_ld.search(str(local)) is not None:
        return False
    if local_pt_dt_nd.search(str(local)) is not None:
        return False

    # check each character in 'local' against the char whitelist
    for char in local:
        if local_pt.search(str(char)) is None:
            return False

    # check for awkward domain double dot '..' edge cases up front
    if re_dbl_dt.search(str(domain)) is not None:
        return False

    # check for leading or trailing hyphens in domain that are invalid
    if dm_pt_hy_ld.search(str(domain)) is not None:
        return False
    if dm_pt_hy_nd.search(str(domain)) is not None:
        print(str(dm_pt_hy_nd.search(str(domain))))
        return False

    # check 'domain' for possible ipv4, ipv6, and domain formats
    if(dm_ipv4.match(str(domain)) is None and
       dm_ipv6.match(str(domain)) is None and
       dm_dtcm.match(str(domain)) is None):
        return False

    return True
