#!/usr/bin/env python3

class File(object):

    FILE_PERMISSIONS = 'rwx'

    def __init__(self, name, owner, size=0, permissions=''):
        self.name = name
        self.owner = owner
        self.size = size
        self.permissions = permissions

    def __str__(self):
        b = []
        b.append('File: {}'.format(self.name))
        b.append('Owner: {}'.format(self.owner))
        if self.permissions:
            b.append('Permissions: {}'.format(''.join(sorted(self.permissions))))
        else:
            b.append('Permissions: null')
        b.append('Size: {} bytes'.format(self.size))
        return '\n'.join(b)

    def has_access(self, user, mode):
        if user == self.owner:
            return True
        else:
            if mode in self.permissions:
                return True
            else:
                return False

    def enable_permission(self, user, mode):
        if user != self.owner:
            print('Access denied')
        elif mode in File.FILE_PERMISSIONS and mode not in self.permissions:
            self.permissions += mode

    def disable_permission(self, user, mode):
        if user != self.owner:
            print('Access denied')
        elif mode in File.FILE_PERMISSIONS and mode in self.permissions:
            perms = list(self.permissions)
            perms.remove(mode)
            self.permissions = ''.join(perms)

    def get_permissions(self):
        return ''.join(sorted(self.permissions))

def main():
    # Display available permissions
    print('-----File permissions: {}'.format(File.FILE_PERMISSIONS))

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('readme.txt', 'max', 1000, 'r')
    f3 = File('secret.txt', 'fred', 100)

    # Display file details
    print('-----File details...')
    print(f1)
    print(f2)
    print(f3)

    # Check access rights
    print('-----Access rights...')
    print(f3.has_access('fred', 'r'))
    print(f3.has_access('mary', 'x'))

    # Enable permissions
    print('-----Enabling permissions...')
    f3.enable_permission('fred', 'x')
    f3.enable_permission('mary', 'w')

    # Check access rights
    print('-----Access rights...')
    print(f3.has_access('mary', 'x'))

    # Disable permissions
    print('-----Disabling permissions...')
    f3.disable_permission('fred', 'x')
    f3.disable_permission('mary', 'w')

    # Check access rights
    print('-----Access rights...')
    print(f3.has_access('mary', 'x'))
    print(f3.has_access('vera', 'w'))

    # Enable permissions
    print('-----Enabling permissions...')
    f3.enable_permission('fred', 'r')
    f3.enable_permission('fred', 'x')
    f2.enable_permission('max', 'w')
    f2.enable_permission('max', 'x')

    # Display permissions
    print('-----Permissions: {}'.format(f3.get_permissions()))
    print('-----Permissions: {}'.format(f2.get_permissions()))

    # Display file details
    print('-----File details...')
    print(f3)

if __name__ == '__main__':
    main()