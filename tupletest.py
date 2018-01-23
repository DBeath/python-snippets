
def return_tuple(boolean):
    if boolean:
        return True, False
    else:
        return None


try:
    values = return_tuple(False)
    if values:
        trueval, falseval = values
except Exception as e:
    print(e)

print(trueval)
print(falseval)
