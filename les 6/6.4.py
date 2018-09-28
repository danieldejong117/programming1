def new_password(oldpassword, newpassword):
    if oldpassword not in newpassword and len(newpassword) >= 6:
        return True
    else:
        return False

oldpassword = ('pythoniscool')
newpassword = ('hebhetgemaakt')
print (new_password(oldpassword, newpassword))