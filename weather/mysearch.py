import urllib.request
import json
import pickle

# 二进制打开文件
pickle_file = open('city_data.pkl', 'rb')
# 加载文件
city = pickle.load(pickle_file)

password = input('请输入城市:')
# 通过键值对列表中输入的城市比对获取列表中的编码
name = city[password]
# 通过request打开设置参数的网址
File1= urllib.request.urlopen('http://www.weather.com.cn/data/sk/'+ name +'.html')

#读取打开的url
weatherHTML = File1.read().decode('utf-8')

#创建json对象,解析获得的HTML
weatherJSON = json.JSONDecoder().decode(weatherHTML)

#解析获得列表中的天气对象数据
weatherInfo = weatherJSON['weatherinfo']

#强转温度类型变成float类型方便使用
temperature_temp = float(weatherInfo['temp'])

#最高温度
max_temp = int(temperature_temp*(1+0.17))
#最低温度
min_temp = int(temperature_temp*(1-0.17))

#打印信息
print('城市：',weatherInfo['city'])
print('时间：',weatherInfo['time'])
print('24小时天气：')
print('当前温度：',weatherInfo['temp'],'°C')

print("最高温度：",max_temp,'°C')
print("最低温度：",min_temp,'°C')

print('风速：',weatherInfo['WD'])
print('紫外线：',weatherInfo['WS'])


# print('48小时天气：')
# print('温度：',weatherInfo['temp2'])
# print('天气：',weatherInfo['weather2'])
# print('风速：',weatherInfo['wind2'])
# print('紫外线：',weatherInfo['index48_uv'])
# print('穿衣指数：',weatherInfo['index48_d'])
#
# print('72小时天气：')
# print('温度：',weatherInfo['temp3'])
# print('天气：',weatherInfo['weather3'])
# print('风速：',weatherInfo['wind3'])


input('按任意键退出')



