#!/usr/bin/env python3

"""12306网站信息获取

Usage:
  tickets [-gdctkz] [<from>] [<to>] [<date>]

Options:
  -h, --help  显示帮助菜单
  -g          高铁
  -d          动车
  -c          城际
  -t          特快
  -k          快速
  -z          直达

Example:
  tickets 北京 上海 2016-10-10
  tickets -dg 成都 南京 2016-10-10

"""

from docopt import docopt

from stations import stations
from codes import codes

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from prettytable import PrettyTable
from colorama import Fore, init

import time

#init color
init()

class TrainsCollection:
  header = '车次 车站 时间 历时 商务 一等 二等 高软 软卧 硬卧 硬座 无座'.split()
  
  def __init__(self, available_trains, options):
    """查询到的火车班次集合 
    :param available_trains: 一个列表, 包含可获得的火车班次, 每个 火车班次是一个字典
    :param options: 查询的选项, 如高铁, 动车, etc... """
    self.available_trains = available_trains
    self.options = options
    
  def _get_duration(self, train_attr):
    duration = train_attr[10].replace(':', '小时') + '分'
    if duration.startswith('00'):
      return duration[4:]
    if duration.startswith('0'):
      return duration[1:]
    return duration

  def _color(self, n):
    if n is None or n == '':
      return '-'
    elif '无' == n:
      return n
    return Fore.GREEN+n+Fore.RESET
    
  @property 
  def trains(self): 
    for raw_train in self.available_trains: 
      train_attr=raw_train.split('|')
      # print(train_attr)

      train_no = train_attr[3]
      initial = train_no[0].lower()

      if not self.options or initial in self.options: 
        train = [ 
          train_no, 
          '-'.join([Fore.GREEN + codes.get(train_attr[4]) + Fore.RESET, 
            Fore.RED + codes.get(train_attr[5]) + Fore.RESET]), #开始，到站时间 
          '-'.join([Fore.GREEN + train_attr[8] + Fore.RESET,
            Fore.RED + train_attr[9] + Fore.RESET]), #始发、终点
          self._get_duration(train_attr), 
          self._color(train_attr[25]), #商务
          self._color(train_attr[31]), #一等
          self._color(train_attr[30]), #二等
          self._color(train_attr[21]), #高级软卧
          self._color(train_attr[23]), #软卧
          self._color(train_attr[28]), #硬卧
          self._color(train_attr[29]), #硬座
          self._color(train_attr[26]), #无座
        ] 
        yield train 
          
  def pretty_print(self):
    pt = PrettyTable() 
    pt.padding_width = 1
    pt._set_field_names(self.header) 
    for train in self.trains: 
      pt.add_row(train) 
    print(pt)

def cli():
  """
  commend line interface
  """
  args = docopt(__doc__)
  # print(args)
  from_station = args['<from>']
  if from_station is None:
    from_station = '北京'

  to_station = args['<to>']
  if to_station is None:
    to_station = '上海'

  date = args['<date>']
  now = time.strftime('%Y-%m-%d')
  if date is None:
    date = now

  try:
    date = time.strptime(date,'%Y-%m-%d')
  except:
    print('日期不合法，正确格式：2017-12-12')
    return

  if date < time.strptime(now,'%Y-%m-%d'):
    print('无法查询历史车票信息，请输入今天或之后的时间，默认为今天')
    return

  date = time.strftime('%Y-%m-%d',date) #to string

  print('出发地：{}，目的地：{}，出发日期：{}'.format(Fore.GREEN+from_station+Fore.RESET, 
    Fore.GREEN+to_station+Fore.RESET, Fore.GREEN+date+Fore.RESET))

  url = ('https://kyfw.12306.cn/otn/leftTicket/queryZ?'
  'leftTicketDTO.train_date={}&leftTicketDTO.from_station={}'
  '&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(
    date,stations.get(from_station),stations.get(to_station))

  # print('request url = ', url)

  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  r = requests.get(url, verify=False)

  # print('response', r.json())

  try:
    available_trains = r.json()['data']['result']
  except:
    print('没有获取到列车信息')
    return

  # 获取参数 
  options = ''.join([ key for key, value in args.items() if value is True ])
  # print(options)

  TrainsCollection(available_trains,options).pretty_print()


if __name__ == '__main__':
  cli()
