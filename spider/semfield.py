import csv

# print("insert into domain_sem_field(`type`,`real_id`,`text`,`parent_id`,`level`) values ")

# sql2 = "( '%s','0','1' )"
# file = open('C:\\Users\\baqianxin\\Documents\\asdasd.csv','r')
# file.readline()

# for i in file.readlines():
#     data = i.strip()
#     data = data.replace('360','1')
#     data = data.replace('baidu','2')
#     data = data.replace(',','\',\'')
#     print(sql2 % data,',')

print("insert into domain_sem_field(`type`,`parent_id`,`real_id`,`text`,`level`) values ")

sql2 = "( '%s','3' )"
# file = open('C:\\Users\\baqianxin\\Documents\\jihuadanyuan.csv', 'r')
file = open('C:\\Users\\baqianxin\\Documents\\danyuankeywords.csv', 'r')
file.readline()

for i in file.readlines():
    data = i.strip().split(",")
    if('360' in data[0]):
        data[0] = "1"
    else:
        data[0] = "2"

    del data[2]
    print(sql2 % "','".join(data), ',')
