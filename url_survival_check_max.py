#By TeamsSix
#Blog teamssix.com
import sys
import requests
import urllib3
urllib3.disable_warnings()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def ip_check(url_path):
	ip_format_list  = []
	f = open(url_path,'r')
	ip_list = f.readlines()
	f.close()

	for i in ip_list:
		i = i.replace('\n','')
		a = 1
		if 'http' in i:
			try:
				url = i
				r = requests.get(url,headers=headers,timeout=3)
				ip_format_list.append(url)
				print(url)
			except KeyboardInterrupt:
				sys.exit()
			except:
				print(url+' Not Survival')
				i = url.split('//')[1]
				ip_format_list.append(i)
				pass
		else:
			try:
				url = 'http://'+i
				r = requests.get(url,headers=headers,timeout=3)
				ip_format_list.append(url)
				print(url)
			except KeyboardInterrupt:
				sys.exit()
			except:
				print(url+' Not Survival')
				a = a+1
				pass

			try:
				url = 'https://'+i
				r = requests.get(url,headers=headers,verify=False,timeout=3)
				ip_format_list.append(url)
				print(url)
			except KeyboardInterrupt:
				sys.exit()
			except:
				print(url+' Not Survival')
				a = a+1
				pass
			if a == 3:
				ip_format_list.append(i)
		ip_format(ip_format_list)

def ip_format(ip_format_list):
	save_path = 'result_max.txt'
	f = open(save_path,'w')
	for i in ip_format_list:
		f.write(i+'\n')
	f.close()

if __name__ == '__main__':
	try:
		url_path = sys.argv[1]
	except:
		print('python3 url_survival_check_max.py url.txt')
		sys.exit()
	ip_check(url_path)
