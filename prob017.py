#!/usr/bin/python

def num_to_str(n):
    ret = ''
    ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
            'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if n >= 100:
        x = n % 1000 / 100
        ret += ones[x - 1] + 'hundred'
        if n % 100 > 0: ret += 'and'
    if n % 100 / 10 >= 2:
        x = n % 100 / 10
        ret += tens[x - 2]
    if 1 <= n % 100 < 20:
        ret += ones[n % 100 - 1]
    elif n % 10 > 0:
        ret += ones[n % 10 - 1]
    return len(ret)

print sum([num_to_str(x) for x in range(1, 1000)]) + len('onethousand')
