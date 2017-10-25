# dict = {'Name': 'Zara', 'Age': 27}
#
#
# print(dict.get('Age'))
#
# a='cmd'
# actions = {
#     'cmd': cmd.CMD,
#     'state':state.State
# }
#
# print(actions.get('cmd'))
#
# module_name ='state.State'
# mod_name,mod_method = module_name.split('.')
#
# print(mod_method,mod_name)

# print(actions.get(a))

class test():
    name = "xiaohua"
    def run(self):
        return "HelloWord"


t=test()
a=hasattr(t,'name')

print(a)


b=getattr(t,'run')
print(b())
print(b)