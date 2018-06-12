from stations import stations

from pprint import pprint 

dict_ori = stations
dict_new = {value:key for key,value in dict_ori.items()}

pprint(dict_new, indent=4)