"""
Number letter counts
========================================================================================================================
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
========================================================================================================================
"""
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
           11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
           18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
           70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 0: ''}

s = 0
for i in range(1, 1001):
    if i < 100:
        if not i in numbers:
            name = numbers[int(str(i)[0]+'0')] + numbers[int(str(i)[1])]
            numbers[i] = name
        s += len(numbers[i])
    else:
        if i < 1000:
            num = 100
        else:
            num = 1000
        name = numbers[int(str(i)[0])] + numbers[num]
        if any(map(lambda x: x != '0', str(i)[1:])):
            name += 'and' + numbers[int(str(i)[1:])]
        s += len(name)
print s