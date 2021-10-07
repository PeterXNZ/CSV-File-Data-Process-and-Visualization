import os
import pandas as pd
import csv
for info in os.listdir('''D:\\presen'''):
    domain = os.path.abspath(r'''D:\\presen''')
    info = os.path.join(domain, info)
    path=info
    workspace = '''D:\\presen'''
    with open(path, 'r', newline='') as info:
        csvreader = csv.reader(info)
        #print(a)
        i = j = 0
        for row in csvreader:
            print(row)
            print(f'i is {i}, j is {j}')
            # 每128个就j加1， 然后就有一个新的文件名
            if i % 1035 == 0:
                j += 1
                print(f"csv {j} 生成成功")
            # csv_path = os.path.join('../new_csv_file/', 'development (4)/' + str(j) + '.csv')

            csv_path = os.path.join(workspace, 'part_{}.csv'.format(j))


            # print('/'.join(path.split('/')[:-1]))
            print(csv_path)
            # 不存在此文件的时候，就创建

            if not os.path.exists(os.path.dirname(csv_path)):
                os.makedirs(os.path.dirname(csv_path))
                with open(csv_path, 'w', newline='') as info:
                    csvwriter = csv.writer(info)
                    # csvwriter.writerow(['image_url'])
                    csvwriter.writerow(row)


                i += 1


            # 存在的时候就往里面添加
            else:
                with open(csv_path, 'a', newline='') as info:
                    csvwriter = csv.writer(info)
                    csvwriter.writerow(row)


                i += 1



