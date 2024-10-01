users=[]
veh=[]
def register():
    if len(users)==0:
        id=1
    else:
        id=user[-1]['id']+1
    

    email=str(input("enter the email :"))
    f=0
    for i in users:
        if i['email']==email:
            f=1
            register()
    if f==0:
        name=str(input("enter the name :"))
        username=email
        phone=int(input("enter the no :"))
        password=str(input("enter password :"))
        users.append({'name':name,'id':id,'email':email,'phone':phone,'veh':[],'username':username,'password':password})

def login():
    uname=input("enter uname : ")
    passw=input("enter passw : ")
    f=0
    if uname == 'admin' and passw == 'admin':
        f=1
    cust=''
    for i in users:
        if uname == i['email'] and passw == i['password']:
            f=2
            cust=i
    return f,cust

def add_veh():
    if len(veh)==0:
        id=101
    else:
        id=veh[-1]['id']+1
    f=0
    for i in veh:
        if i['id']==id:
            f=1
            add_veh()
    if f==0:
        name=str(input("enter the  name : "))
        brand=str(input("enter the brand : "))
        model=int(input("enter the model : "))
        fueltype=str(input("enter the fueltype : "))
        mileage=int(input("enter the mileage : "))
        insurance=int(input("enter insurance : "))
        stock=int(input("enter the stock : "))
        veh.append({'name':name,'id':id,'brand':brand,'model':model,'fueltype':fueltype,'mileage':mileage,'insurance':insurance,'stock':stock})


def view_veh():
    for i in veh:
        print(i)

def update_veh():
    id=int(input("enter the id : "))
    f=0
    for i in veh:
        if i['id']==id:
            f=1
            fueltype=str(input("enter the fueltype : "))
            insurance=int(input("enter the insurance : "))
            stock=int(input("enter the stock"))
            i['fueltype']=fueltype
            i['insurance']=insurance
            i['stock']=stock
    if f==0:
        print('invalid id')

def delete():
    id=int(input("enter the id : "))
    f=0
    for i in veh: 
        if i['id']==id:
            f=1
            veh.remove(i)
    if f==0:
        print('invalid id')

def view_user():
    for i in users:
        print('name',i['name'])
        print('id',i['id'])
        print('email',i['email'])
        print('phone',i['phone'])

def view_profile(cust):
    print(users)


def update_pro(cust):
    name=str(input("enter the name : "))
    phone=int(input("enter phone : "))
    cust['name']=name
    cust['phone']=phone
    
def buy_veh(cust):
    id=int(input("enter the id : "))
    f=0
    for i in veh:
        if i['id']==id:
            f=1
            i['stock']-=1
            cust['veh'].append(id)
            print('veh added')
    if f==0:
        print("invalid id")


def veh_in_hand(cust):
    print(cust['veh'])

while True:
    print('''
    1.register
    2.login
    3.exit 
''')
    choice=int(input("enter the choice :"))
    if choice==1:
        register()
    elif choice==2:
        f,cust=login()
        if f==1:
            while True:
                print('''
                1.add veh
                2.view veh
                3.update veh
                4.delete
                5.view user
                6.exit
                ''')
                sub_choice=int(input("enter the choice : "))
                if sub_choice==1:
                    add_veh()
                elif sub_choice==2:
                    view_veh()
                elif sub_choice==3:
                    update_veh()
                elif sub_choice==4:
                    delete()
                elif sub_choice==5:
                    view_user()
                elif sub_choice==6:
                    break
                else:
                    print('invalid choice')
        elif f==2:
            while True:
                print('''
                1.view profile
                2.view veh
                3.update profile
                4.buy veh
                5.veh in hand
                6.exit
                ''')
                sub_ch=int(input("enter the choice : "))
                if sub_ch==1:
                    view_profile(cust)
                elif sub_ch==2:
                    view_veh()
                elif sub_ch==3:
                    update_pro(cust)
                elif sub_ch==4:
                    buy_veh(cust)
                elif sub_ch==5:
                    veh_in_hand(cust)
                elif sub_ch==6:
                    break
                else:
                    print("invalid choice")
        else:
            print('invalid username or password')
    elif choice==3:
        break
    else:
        print('invalid')