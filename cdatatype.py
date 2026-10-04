name=input('enter your name: ')
gadget=input('enter you favorite gadget: ')
num=6
speed=10.0
mission=3
height=1.7
isactive=True
print('name: ',type(name))
print('favorite gadget: ',type(gadget))
print('agent number: ',type(num))
print('agent speed: ',type(speed))
print('mission number: ',type(mission))
print('agents height: ',type(height))
print('active fr inactive: ',type(isactive))
print('********************************************************')

anum=str(num)
amission=str(mission)
aspeed=str(speed)
astatus=str(isactive)

print(anum,amission,aspeed,astatus)

print('**************************')

first=name[1:4]
last=name[-1:]
code=first+last
print('secret code name: ',code)

rgadget='reversed gadget name: ' + gadget[::-1]

badge1= 'AGENT: '+code.upper()
badge2= 'ID: ' + anum + amission
badge3= 'SPEED: ' +aspeed + 'STATUS: ' + astatus
badge4= 'SECRET GADGET CODE: '+ rgadget

print('SECRET AGENT BADGE')
print(f'{badge1},\n{badge2},\n{badge3},\n{badge4}')









