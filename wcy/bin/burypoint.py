# -*-conding:utf-8-*-
# @author:wangchengyuan
# @time:2019/5/8 11:47 AM
# @desc:

import re

maidian_basic = ['event', 'title', 'time_stamp', 'channel', 'userid_num', 'bi_device_id', 'install_channel',
                 'client_type', 'os_type', 'page', 'scene_type', 'is_show', 'feed_video_playtime',
                 'feed_video_starttime',
                 'feed_video_endtime', 'ad_code', 'ad', 'ad_name', 'secrecy_type', 'feed', 'feed_userid', 'feed_id',
                 'comment_id', 'comment_userid', 'filter_parameter', 'page_index', 'page_index_feed', 'find_user_id',
                 'control_rule', 'comment_index_feed', 'topic_id', 'topic_name', 'set_value', ]
maidian_ext = ['user_id', 'alumnus_card', 'alumnus_user_id']


# 描述打印的埋点种类
def maidian_desc(keyname):
    s = ''
    if keyname == maidian_basic:
        sname = '基础埋点'
    elif keyname == maidian_ext:
        sname = '扩展埋点'
    print(60 * '*')
    print('*' + 58 * '-' + '*')
    print('*' + 26 * ' ' + sname + 25 * ' ' + '*')
    print('*' + 58 * '-' + '*')
    print(60 * '*' + '\n')


# 校验并打印埋点数据
def checkmaidian(keyname, test):
    maidian_desc(keyname)
    for i in keyname:
        rex = '"%s":(.*?),' % i
        content = re.findall(rex, test)
        if len(content) > 0:
            print(i + '数据:   ' + content[0] + '\n')
        else:
            print(i + '数据:   ' + 5 * '-', "\033[1;31m 不存在 \033[0m!", 5 * '-', '\n')


if __name__ == '__main__':
    test = input("请输入买点数据：\n")
    # test=sys.argv[0]
    checkmaidian(maidian_basic, test)
    checkmaidian(maidian_ext, test)