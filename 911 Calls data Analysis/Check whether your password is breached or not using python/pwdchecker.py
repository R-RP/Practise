import requests
import hashlib


def get_request(hashfirst_pwd,tail,password):
    url = 'https://api.pwnedpasswords.com/range/' + hashfirst_pwd
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Status code is {response.status_code} please check API request')
    return find_count(response.text,tail,password)


def hash_converter(password):
    hash_pwd = hashlib.sha1(password.encode())
    hash_pwd = hash_pwd.hexdigest()        
    head,tail = hash_pwd[:5],hash_pwd[5:]
    return get_request(head,tail,password)


def find_count(hash_text,tail,password):
    hash_lines = hash_text.splitlines()
    result = {}
    for line in hash_lines:
        key,count = line.split(':')
        result[key] = count
    #print(result)
    final = tail.upper() 
    final.strip()
    #print(tail,final)
    #print(password)
    if final in result:
        print(f"Your password '{password}' has been found {result[final]} times")
    else:
        print(f"your password '{password}' is secure")
    return 'success' 
def main():
    fh = open('password.txt')
    txt = fh.readlines()
    for line in txt:
        line = line.strip()
        #print('line',line)
        hash_converter(line)        
    print('All done')

if __name__ == '__main__':
    main()

    
    
    