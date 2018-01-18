# -*- coding: utf8 -*- 
 # Filename : var.py
i = 5
print (i)
i = i + 1
print (i)

s = '''This is a multi-line string.
This is the second line.'''
print (s )

################
#呵呵，还忘记了讲注释
#第一个算是完整的程序
################
contact = {}
contact_list = []
while 1:
    contact['name'] = input("please input name: ")
    contact['phone'] = input("please input phone number: ")
    contact_list.append(contact.copy())
    go_on = input("continue?\n")
    if go_on == "yes":
        pass
    elif go_on == "no":
        break
    else:
        print ("you didn't say no\n")
i = 1
for contact in contact_list:
    print ("%d: name=%s" % (i, contact['name']))
    print ("%d: phone=%s" % (i, contact['phone']))
else:
	i = i+1;
	print(i);