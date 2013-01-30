emailviz
========

CS467 email visualization


How to find the IP in mbox file
-------------------------------
Find the line starts from 'Received', it is usually the following:

    Received: from local.domain.name (global.domain.name [192.17.105.204])

Note that sometimes the global.domain.name is missing, e.g.,

    Received: from [192.168.3.102] ([183.55.233.71])

so we have to carefully extract the IP address in the brackets.
The current way is to match an IP as 183.55.233.71]), and remove the tail '])'
by regular expression grouping.
