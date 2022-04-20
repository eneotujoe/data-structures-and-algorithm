
def time_conversion(s):
    s_list = s.rstrip('PMAM').split(':')
    h = s_list[0]
    if h == '12' and s.endswith('AM'):
        s_list[0] = '00'
    elif h == '12' and s.endswith('PM'):
        s_list[0] = '12'
    else:
        s_list[0] = str(int(h) + 12)

    return str(':'.join(s_list))



if __name__ == '__main__':
    s = '12:01:00AM'
    # time_conversion(s)
    print(time_conversion(s))
