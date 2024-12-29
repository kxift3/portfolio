if __name__=='__main__':
    mark_1 = int(input ('Enter the first mark:  '))
    mark_2 = int(input ('Enter the second mark: '))
    mark_3 = int(input ('Enter the third mark:  '))
    mark_4 = int(input ('Enter the fourth mark: '))
    mark_5 = int(input ('Enter the fifth mark:  '))

    avg_mark = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) / 5
    max_mark = max(mark_1, mark_2, mark_3, mark_4, mark_5)
    min_mark = min(mark_1, mark_2, mark_3, mark_4, mark_5)

    print (f'Average Mark: {avg_mark}')
    print (f'Max Mark: {max_mark}')
    print(f'Min Mark: {min_mark}')