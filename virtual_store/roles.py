from rolepermissions.roles import AbstractUserRole

class Client(AbstractUserRole):
    available_permissions = {
        'client_permissions': True,
    }
class Member(AbstractUserRole):
    available_permissions = {
        'edit_home_page': True,
        'client_permissions': True,
    }
class MasterMember(AbstractUserRole):
    available_permissions = {
        'edit_home_page': True,
        'client_permissions': True,
        'edit_all_page': True,
    }