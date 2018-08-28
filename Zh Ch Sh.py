import msvcrt
import random
import time
import winsound
Zh = b"v"
Ch = b"i"
Sh = b"u"

shengmu_list = [b"b",b"p",b"m",b"f",b"g",b"k",b"h",b"j",b"q",b"x",b"d",b"t",b"n",b"l",b"r",b"z",b"c",b"s"]



char_list_name = [ "Zh" , "Ch" , "Sh"]
char_list = [ Zh , Ch , Sh]
random.seed(time.time())

retry = False
all_count = 0
error_count = 0

Qiaosheyin = True
while True:
    if not retry:
        rand_char_index = random.choice([0,1,2])
        Qiaosheyin = random.randint(0,10) < 6
        all_count+=1
        ch = random.choice(shengmu_list)
        ch_qiaosheyin = random.choice(char_list)
    if Qiaosheyin:
        if all_count == 1:
            print("接下来请输入： %s " % ( char_list_name[rand_char_index] ))
        else:
            print("接下来请输入： %s (目前正确率 %d/%d %d%%)  " % (char_list_name[rand_char_index],(all_count-error_count-1),all_count-1,(all_count-error_count-1)/(all_count-1)*100))
    else:
        if all_count == 1:
            print("接下来请输入： %s " % (ch.decode("utf-8")))
        else:
            print("接下来请输入： %s (目前正确率 %d/%d %d%%)  " % (
                ch.decode("utf-8"), (all_count - error_count - 1), all_count - 1,
            (all_count - error_count - 1) / (all_count - 1) * 100))

    char = msvcrt.getche()
    msvcrt.getche()
    if Qiaosheyin:

        if char == char_list[rand_char_index]:
            print("输入正确")
            retry = False
        elif char == b'\x03':
            break
        else:
            print("输入错误，请重试")
            winsound.MessageBeep(winsound.MB_ICONHAND)
            error_count += 1
            retry = True
    else:

        if char == ch:
            print("输入正确")
            retry = False
        elif char == b'\x03':
            break
        else:
            print("输入错误，请重试")
            winsound.MessageBeep(winsound.MB_ICONHAND)
            error_count += 1
            retry = True