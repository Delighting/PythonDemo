import requests

r = requests.get('http://www.baidu.com')

print(r.status_code)

print(r.text)

def downurl(url):
  r = requests.get(url)

  if r.status_code == 404:
    print("web site not exist")
    return

#last / is filename
  filename = url.split('/')[-1]+'.html'

  with open(filename,'wb') as furl:
    furl.write(r.content)
  print('download over')

if __name__ == '__main__':
  url = input('enter a url: ')
  downurl(url)