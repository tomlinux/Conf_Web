#_*_ coding: utf-8 _*_

from  django import  template

register = template.Library()

@register.filter(name='userlist_str2')
def userlist_str2(user_list):
    ''' 将用户列表转为str'''
    if len(user_list) < 3:
        return  ' '.join([user.name_cn for user in user_list])
    else:
        return '%s ...' % ''.join([user.name_cn for user in user_list[0:2]])


@register.filter(name='group_str2')
def group_str2(group_list):
    ''' 将角色转换为 str'''
    if len(group_list) < 3:
        return  ' '.join([user.name for user in group_list])
    else:
        return '%s ...' % ''.join([user.name for user in group_list[0:2]])


@register.filter(name='perm_str2')
def perm_str2(perm_list):
    '''将用户或者组权限列表转换为str'''
    if len(perm_list) < 3:
        return  ' '.join([user.codename for user in perm_list])
    else:
        return '%s ...' % ''.join([perm.codename for perm in perm_list[0:2]])


@register.filter(name='bool2str')
def bool2str(is_active):
    if is_active:
        return  '已激活'
    else:
        return '未激活'

