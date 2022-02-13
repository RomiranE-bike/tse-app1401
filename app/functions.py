import re
# ------------------------------------------------------------------
def chang_num(number):
    # number = str(number)
    number = number.split(',')
    number = ''.join(number)
    number = number.strip()
    try:
        if 'B' in number:
            number = number.strip('B')
            number = float(number) * 1000000000
        elif 'M' in number:
            number = number.strip('M')
            number = float(number) * 1000000
        else:
            number = number.replace("'", "")
            # print(number,type(number))
            number = float(number)
    except:pass
    return number

# ------------------------------------------------------------------------
def convert (num):
    temp = num.replace(",", "")
    intnum=int(float(temp))
    return intnum
# 3 functio for reverse data list----------------------
# ---------------------------1-------------------------
# Reversing a list using reversed()  built-in function 1
def Reverse(list):
    return [item for item in reversed(list)]

# print(Reverse(index_item))
# ---------------------------2-------------------------

# Reversing a list using reverse()  built-in function 2
def Reverse(list):
    list.reverse()
    return list

# print(Reverse(index_item))
# ----------------------------3------------------------

# Reversing a list using slicing technique 3
def Reverse(list):
    new_list = list[::-1]
    return new_list
# 3 functio for reverse data list----------------------

# ----------------------# find the group number using regex-------------------
def get_group_num(text):
    if re.search('\d+', text):
        group_num= re.findall('\d+', text)[0]
    else:
        group_num = '0'

    return group_num
# ----------------------# find the group number using regex-------------------

# ----------------------var name----------------------------------------------
# name = 'Elon'
# exec("%s = %d" % (name,100))
# print(Elon)
#
# for i in range(1,11):
#     var_name = 'group_list{}'.format(i)
#     locals()[var_name] = i
#
#     print('group_list{}'.format(i))
# ----------------------var name----------------------------------------------
# ---------------------------auto var name creator-----------------------------
group_list=[]
group={}
for i in range(10):
    group['group_{}'.format(i)]=i
    # group_list.append(group.copy())
    group_list.append(group)
    # print(dict)

# print(group_list)

# {% for i in range(array|length) %}
#           array[i]
# {% endfor %}
# ---------------------------auto var name creator-----------------------------