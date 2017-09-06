# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        print('Number of donuts:', count)
    else:
        print('Number of donuts: many')    
    
    #raise NotImplementedError


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s)<2:
        print('')
    else:
        print(s[:2]+s[-2:])
        
    #raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    res = s
    temp = s[0]
    for j in range(1,len(s)):
        if s[j]==temp:
            res = res[0:j] + '*' + res[j+1:]
    
    print(res)
    
    #raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    
    print(b[0:2]+a[2:]+' '+a[0:2]+b[2:])
    
    #raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    
    res = s
    if len(s)>2 and s[-3:]=='ing':
        res = res + 'ly'
    elif len(s)>2 and s[-3:]!='ing':
        res = res + 'ing'
    
    print(res)    
    
    #raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    res = s
    ind1 = s.find('not')
    ind2 = s.find('bad')
    if ind1<ind2:
        res = s[0:ind1] + 'good' + s[ind2+3:]
    
    print(res)
    
    #raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    asize = len(a)
    bsize = len(b)
    #if length of a even
    if asize%2==0:
        afront = a[0:int(asize/2)]
        aback = a[int(asize/2):]
    #if lenght of a odd
    else:
        afront = a[0:int((asize+1)/2)]
        aback = a[int((asize+1)/2):]       

    #if length of b even
    if bsize%2==0:
        bfront = b[0:int(bsize/2)]
        bback = b[int(bsize/2):]
    #if lenght of b odd
    else:
        bfront = b[0:int((bsize+1)/2)]
        bback = b[int((bsize+1)/2):]     
        
    result = afront + bfront + aback + bback
    print(result)
    
    #raise NotImplementedError
