#Сложение по модулю N
values = {}
alphabet=[
  "А", "Б", "В", "Г", "Д", 
  "Е", "Ж", "З", "И", 
  "Й", "К", "Л", "М", "Н", 
  "О", "П", "Р", "С", "Т", 
  "У", "Ф", "Х", "Ц", "Ч", 
  "Ш", "Щ", "Ъ", "Ы", "Ь", 
  "Э", "Ю", "Я"
]
for i in range(0,32):
    values[i]=alphabet[i]
message='НДЖОБВУ'
gamma='яблочко'
message_data=[]
gamma_data =[]
encrypted_data =[]
output_message = []
#Сложение по модулю N
def encryption(message,gamma):
    for i in message:
        for j in values.values():
            if i == j:
                for k in values.keys():
                    if values[k] == j:
                        message_data.append(k)
    for i in gamma.upper():
        for j in values.values():
            if i == j:
                for k in values.keys():
                    if values[k] == j:
                        gamma_data.append(k)
    list_length = len(message_data)
    for i in range(list_length):
        if message_data[i]+gamma_data[i] >= 32:
            num= (message_data[i]+gamma_data[i])-32
            encrypted_data.append(num)
        else:
            encrypted_data.append(message_data[i]+gamma_data[i])
    return encrypted_data,gamma_data


returned_enc,returned_gamma=encryption(message,gamma)
print(f"Encrypted:{returned_enc}")
encrypted_message=''
for j in encrypted_data:
    encrypted_message+=values[j]
print(f"Encrypted: s{encrypted_message}")
#Сложение по модулю N
def decryption(encrypted_message, key):
    em_numbers=[]
    key_numbers=[]
    decrypted_numbers=[]
    for i in range(len(encrypted_message)):
        if((encrypted_message[i]+32)-key[i]>32):
            decrypted_numbers.append(encrypted_message[i]-key[i])
        else:
            decrypted_numbers.append((encrypted_message[i]+32)-key[i])
    return decrypted_numbers
decrypted=decryption(returned_enc,returned_gamma)
dec_message=''
for j in decrypted:
    dec_message+=values[j]
print(f"decrypted:{dec_message}")



windows_1251_codes = {
  "А": 192, "Б": 193, "В": 194, "Г": 195, "Д": 196,
  "Е": 197, "Ё": 201, "Ж": 198, "З": 199, "И": 200,
  "Й": 202, "К": 203, "Л": 204, "М": 205, "Н": 206,
  "О": 207, "П": 208, "Р": 209, "С": 210, "Т": 211,
  "У": 212, "Ф": 213, "Х": 214, "Ц": 215, "Ч": 216,
  "Ш": 217, "Щ": 218, "Ъ": 219, "Ы": 220, "Ь": 221,
  "Э": 222, "Ю": 223, "Я": 224
}
for key,value in windows_1251_codes.items():
    if(value>201):
        windows_1251_codes[key]=value-1
converted_codes={key: bin(value)[2:].zfill(8) for key, value in windows_1251_codes.items()}
closed_key=[2,3,6,13,27,52,105,210]
n=31

#Алгоритм на основе задачи об укладке ранца
def encryption_second(closed_key,message):
    opened_key=[]
    message_codes=[]
    encrypted=[]
    for num in closed_key:
        opened=(num*n)%420
        opened_key.append(opened)
    print(f"opened_key: {opened_key}")
    for letter in message:
        message_codes.append(converted_codes[letter])
    print(f"message codes: {converted_codes['Н']}")
    for code in message_codes:
        bag=0
        for i in range(len(code)):
            if(code[i]=='1'):
                bag+=opened_key[i]
        encrypted.append(bag)
    return encrypted,opened_key
    print(f"encrypted {encrypted}")
#Алгоритм на основе задачи об укладке ранца
def decryption_second(encrypted,closed_key,opened_key):
    decrypted={}
    for num in encrypted:
        for letter,code in converted_codes.items():
            bag=0
            for i in range(len(code)):
                if(code[i]=='1'):
                    bag+=opened_key[i]
            if(bag==num):
                decrypted[letter]=code
    print(f"Decrypted: {decrypted}")
            
#enc,opened=encryption_second(closed_key,message)
#decryption_second(enc,closed_key,opened)
# Create a dictionary with base-2 representations of Windows-1251 codes
russian_alphabet_base2 = {key: bin(value)[2:].zfill(8) for key, value in windows_1251_codes.items()}

#Алгоритм Эль Гамаля
russian_alphabet_uppercase = [
  "А", "Б", "В", "Г", "Д", 
  "Е", "Ё", "Ж", "З", "И", 
  "Й", "К", "Л", "М", "Н", 
  "О", "П", "Р", "С", "Т", 
  "У", "Ф", "Х", "Ц", "Ч", 
  "Ш", "Щ", "Ъ", "Ы", "Ь", 
  "Э", "Ю", "Я"
]
mapped_values={}
#Алгоритм Эль Гамаля
def encryption_third(message):
    for i in range(0,33):
        mapped_values[russian_alphabet_uppercase[i]]=i+1
    print(mapped_values)
    k=7
    p=23
    g=3
    x=5
    y=pow(g,x)%p
    encrypted=[]
    for i in range(len(message)):
        mapped_num=mapped_values[message[i]]
        b=(pow(y,k)*mapped_num)%p
        encrypted.append(b)
    return encrypted
#Алгоритм Эль Гамаля
def decryption_third(encrypted):
    decrypted=[]
    k=7
    p=23
    g=3
    x=5
    for i in range(len(encrypted)):
        b=encrypted[i]
        a=(pow(g,k))%p
        T=(b*(pow(a,p-1-x)))%p
        decrypted.append(T)
    return decrypted
enc=encryption_third(message)
print(f"Encrypted {enc}")
dec=decryption_third(enc)
print(f"Decrypted: {dec}")



#Шифрование по алгоритму RSA
def encryption(message):
    p=7
    q=13
    n=p*q
    funN=(p-1)*(q-1)
    e=51