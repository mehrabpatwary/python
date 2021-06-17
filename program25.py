try:
    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result)
    print('Done')
except ZeroDivisionError:  # except IndexError:
    print('Dividing by zero is not possible')


finally:  # finally keyword block must be work if there any error
    print("Successful")

'''except (ZeroDivisionError, IndexError):
    print('Dividing by zero is not possible')'''
