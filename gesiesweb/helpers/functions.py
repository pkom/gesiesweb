import django_auth_ldap.backend

def update_usuario(sender, user=None, ldap_user=None, **kwargs):
    # Remember that every attribute maps to a list of values
    dnis = ldap_user.attrs.get("employeeNumber", [])
    for dni in dnis:
        print dni


#from helpers.functions import update_usuario

#django_auth_ldap.backend.populate_user.connect(update_usuario)    