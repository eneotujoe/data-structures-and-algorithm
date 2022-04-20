
def time_conversion(s):
    # s_list = s.rstrip('PMAM').split(':')
    # h = s_list[0]
    # if h == '12' and s.endswith('AM'):
    #     s_list[0] = '00'
    # elif h == '12' and s.endswith('PM'):
    #     s_list[0] = '12'
    # else:
    #     s_list[0] = str(int(h) + 12)

    # return str(':'.join(s_list))


    s_list = list(s)
    hh = s_list[0] + s_list[1]
    am_pm = (s_list[-2] + s_list[-1]).upper()
    s_list.pop(0)

    if hh == '12' and am_pm == 'AM':
        s_list[0] = '00'
    elif hh == '12' and am_pm == 'PM':
        s_list[0] = '12'
    else:
        s_list[0] = str(int(hh) + 12)

    return str(''.join(s_list))



if __name__ == '__main__':
    s = '12:01:00PM'
    # time_conversion(s)
    print(time_conversion(s))
