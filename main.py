import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--upper', type=int, required=True)
parser.add_argument('--lower', type=int, required=True)
args = parser.parse_args()

t = args.lower
b = args.upper



for num in range(t, b + 1):

   order = len(str(num))

   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)