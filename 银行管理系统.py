import codecs
import random
import json
import os

user = {}
ban_user = set()


class bank:
    def open_an_account(self):
        name = input('请输入姓名：')
        ID = int(input('请输入身份证号码：'))
        num = int(input('请输入手机号'))
        pass_num = int(input('请设置您的密码'))
        amount = int(input('请输入预存金额'))
        a = list(range(10))
        random.shuffle(a)
        bank_num = int(''.join(str(i) for i in a[:6]))
        print(f'恭喜开户成功，您的银行卡号为{bank_num}')
        user.update({name: {
            '手机号': num,
            '身份证号': ID,
            '银行卡号': bank_num,
            '密码': pass_num,
            '余额': amount}})

    def select(self):
        for key, value in user.items():
            a = bool
            b = 0
            while True:
                if b != 3:
                    input_bank_num = int(input('请输入要查询的银行卡号:'))
                    input_pass = int(input('请输入密码:'))
                    if input_bank_num in ban_user:
                        print('该账户锁定中')
                        break
                    else:
                        if value['银行卡号'] == input_bank_num and value['密码'] == input_pass:
                            a = True
                            print('查询成功，余额为：', value['余额'])
                            break
                        else:
                            print('账号或密码错误，请重试')
                            b += 1
                else:
                    print('错误次数已用尽，请稍后重试')
                    break

    def take_out(self):
        for key, value in user.items():
            b = 0
            input_bank_num = int(input('请输入要取款的银行卡号:'))
            if input_bank_num in ban_user:
                print('该账户锁定中')
            elif input_bank_num not in user:
                print('该账户不在系统中')
            else:
                while True:
                    if b != 3:
                        input_pass = int(input('请输入密码:'))
                        if value['银行卡号'] == input_bank_num and value['密码'] == input_pass:
                            num = int(input('请输入取款金额'))
                            if value['余额'] < num:
                                print('您的余额不足')
                                break
                            else:
                                value['余额'] -= num
                                break
                        else:
                            print('账号或密码错误，请重试')
                            b += 1
                    else:
                        ban_user.add(input_bank_num)
                        print('错误次数已用尽，该账户已被冻结')
                        break

    def ban(self):
        for key, value in user.items():
            a = bool
            b = 0
            while True:
                if b != 3:
                    input_bank_num = int(input('请输入要锁定的银行卡号:'))
                    input_pass = int(input('请输入密码:'))
                    if value['银行卡号'] == input_bank_num and value['密码'] == input_pass:
                        ban_user.add(input_bank_num)
                        print('锁定成功')
                        a = True
                        break
                    else:
                        print('账号或密码错误，请重试')
                        b += 1
                else:
                    print('错误次数已用尽，请稍后重试')
                    break

    def deposit(self):
        for key, value in user.items():
            a = bool
            b = 0
            while True:
                if b != 3:
                    input_bank_num = int(input('请输入要存入的银行卡号:'))
                    input_pass = int(input('请输入密码:'))
                    if input_bank_num in ban_user:
                        print('该账户锁定中')
                        break
                    else:
                        if value['银行卡号'] == input_bank_num and value['密码'] == input_pass:
                            num = int(input('请输入存入的金额'))
                            value['余额'] += num
                            print(f'已存入{num}元')
                            a = True
                            break
                        else:
                            print('账号或密码错误，请重试')
                            b += 1
                else:
                    print('错误次数已用尽，请稍后重试')
                    break

    def transfer(self):
        for key, value in user.items():
            a = bool
            b = 0
            while True:
                if b != 3:
                    input_bank_num = int(input('请输入要查询的银行卡号:'))
                    input_pass = int(input('请输入密码:'))
                    if input_bank_num in ban_user:
                        print('该账户锁定中')
                        break
                    else:
                        if value['银行卡号'] == input_bank_num and value['密码'] == input_pass:
                            tr_user = int(input('请输入要汇款的账户'))
                            for value in user.items():
                                if tr_user in user:
                                    a = True
                            if user in ban_user:
                                print('您输入的账户已锁定，请解锁后重试')
                                break
                            elif a != True:
                                print('您输入的账户不在系统中')
                            else:
                                num = int(input('请输入汇款金额'))
                                if num > value['余额']:
                                    print('您的余额不足')
                                else:
                                    value['余额'] -= num
                                    user[tr_user]['余额'] += num
                                    print('汇款成功')
                                    print(f"您目前余额为：{value['余额']}")
                            a = True
                            break
                        else:
                            print('账号或密码错误，请重试')
                            b += 1
                else:
                    print('错误次数已用尽，请稍后重试')
                    break

    def Unlock(self):
        num = int(input('请输入要解锁的账户'))
        if num in user:
            if num in ban_user:
                ban_user.remove(num)
                print('解锁成功')
            else:
                print('此账户并未锁定')
        else:
            print('您输入的账户不在系统中')

    def save(self):
        for key, value in user.items():
            a = bool
            b = 0
            while True:
                if b != 3:
                    input_bank_num = int(input('请输入要查询的银行卡号:'))
                    input_pass = int(input('请输入密码:'))
                    if input_bank_num in ban_user:
                        print('该账户锁定中')
                        break
                    else:
                        if value['银行卡号'] == input_bank_num and value['密码'] == input_pass:
                            json_data = json.dumps(value, ensure_ascii=False, indent=4)
                            filename = str(key).replace("/", "").replace(".", "").replace("\\", "").replace(":", "") \
                                .replace("*", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "") \
                                .replace("|", "")
                            with codecs.open(f"{filename}.txt", "w", "utf-8") as f:
                                f.write(json_data)
                            print(f"文件已保存到：{os.path.abspath(filename + '.txt')}")
                            a = True
                            break
                        else:
                            print('账号或密码错误，请重试')
                            b += 1
                else:
                    print('错误次数已用尽，请稍后重试')
                    break


while True:
    use = bank()
    a = int(input('欢迎使用本银行系统，请选择服务：' + '\n' +
                  '1、开户' + '\n' +
                  '2、查询' + '\n' +
                  '3、取款' + '\n' +
                  '4、存款' + '\n' +
                  '5、转账' + '\n' +
                  '6、锁定' + '\n' +
                  '7、解锁' + '\n' +
                  '8、存盘' + '\n' +
                  '9、退出' + '\n'))
    if a == 1:
        use.open_an_account()
    elif a == 2:
        use.select()
    elif a == 3:
        use.take_out()
    elif a == 4:
        use.deposit()
    elif a == 5:
        use.transfer()
    elif a == 6:
        use.ban()
    elif a == 7:
        use.Unlock()
    elif a == 8:
        use.save()
    else:
        break
