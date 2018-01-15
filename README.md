# No longer maintained. Use https://github.com/elypter/filter_processor instead

# generic_annoying_stickybar_filter
A generic filter for adblockers that keeps annoying header and footer bars from filling up your screen.

generic_header_list.txt is the actual filter list. it is 3.1Mb which is a lot for a filter list but i havent noticed any slowdown

generic_header_filter.py is the script used to create the filterlist. due to limitations in ublock it is not possible to use this type of cosmetic filters for all pages so the list has to have a rule for each top level domain. thats why this filter only works for the 20 most used top level domains. more can be used by adjusting the value in the script

prefixes.txt and suffixes.txt are lists of frequently used words that when combined make up names for classes or styles of annoying sticky elements like header bars.

License: GPL-3.0
