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
        users.append({'name':name,'id':id,'email':email,'phone':phone,'books':[],'username':username,'password':password})

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

def add_book():
    if len(veh)==0:
        id=101
    else:
        id=veh[-1]['id']+1
    f=0
    for i in lib:
        if i['id']==id:
            f=1
            add_book()
    if f==0:
        name=str(input("enter the book name : "))
        price=int(input("enter the price : "))
        stock=int(input("enter the stock : "))
        veh.append({'id':id,'name':name,'price':price,'stock':stock})

def view_book():
    for i in veh:
        print(i)

def update_book():
    id=int(input("enter the id : "))
    f=0
    for i in veh:
        if i['id']==id:
            f=1
            price=int(input("enter the price : "))
            stock=int(input("enter the stock : "))
            i['price']=price
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
    
def lend_book(cust):
    id=int(input("enter the id : "))
    f=0
    for i in veh:
        if i['id']==id:
            f=1
            i['stock']-=1
            cust['books'].append(id)
            print('book added')
    if f==0:
        print("invalid id")

def return_book(cust):
    id=int(input("enter the id : "))
    f=0
    for i in veh:
        if i['id']==id and id in cust['books']:
            f=1
            i['stock']+=1
            cust['books'].remove(id)
            print('book returned')
    if f==0:
        print('invalid id')


def books_in_hand(cust):
    print(cust['books'])

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
                1.add book
                2.view book
                3.update books
                4.delete
                5.view user
                6.exit
                ''')
                sub_choice=int(input("enter the choice : "))
                if sub_choice==1:
                    add_book()
                elif sub_choice==2:
                    view_book()
                elif sub_choice==3:
                    update_book()
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
                2.view book
                3.update profile
                4.lend book
                5.return book
                6.books in hand
                7.exit
                ''')
                sub_ch=int(input("enter the choice : "))
                if sub_ch==1:
                    view_profile(cust)
                elif sub_ch==2:
                    view_book()
                elif sub_ch==3:
                    update_pro(cust)
                elif sub_ch==4:
                    lend_book(cust)
                elif sub_ch==5:
                    return_book(cust)
                elif sub_ch==6:
                    books_in_hand(cust)
                elif sub_ch==7:
                    break
                else:
                    print("invalid choice")
        else:
            print('invalid username or password')
    elif choice==3:
        break
    else:
        print('invalid')