from unittest.mock import MagicMock

def args_based_return(*args, **kwargs):
    if args == (10, 10):
        return 20
    elif args == (20, 20):
        return 40
    else:
        raise Exception("An exception occurred")

# Create a MagicMock with the side_effect set to args_based_return
m = MagicMock(side_effect=args_based_return)

try:
    result1 = m(10, 10)
except Exception as e:
    result1 = e

try:
    result2 = m(40, 40)
except Exception as e:
    result2 = e

print("Result 1:", result1) 
print("Result 2:", result2) 
