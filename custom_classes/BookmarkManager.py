from custom_modules.PlatformConstants import SEP, USER
import os
import re

# Constants
BOOKMARKS_HOME = '{}home{}{}{}Documents{}information{}chromebookmarks{}'.format(
    SEP, SEP, USER, SEP, SEP, SEP, SEP)


class BmLister:
    def __init__(this):
        this.__store = {}
        this.__bookmarks = os.listdir(BOOKMARKS_HOME)
        this.__bookmark_count = len(this.__bookmarks)
        this.store_bookmarks()

    def store_bookmarks(this):
        for b in this.__bookmarks:
            x = re.search(r"_[0-9]{1,2}_[0-9]{1,2}_[0-9]{2}", b)
            this.__store.update({'{}'.format(x.group()[1:]): b})

    def get_bookmark(this, key):
        if key in this.__store:
            return {'status': True, 'bookmark': '{}{}'.format(BOOKMARKS_HOME, this.__store[key])}
        else:
            return {'status': False, 'cause': 'bookmark date: {} not found'.format(key.upper())}

    @property
    def print_bookmarks_list(this):
        for i, b in enumerate(this.__bookmarks, start=1):
            print('{}.\t{}'.format(i, b))

    @property
    def print_bookmarks_map(this):
        for k, v in this.__store.items():
            f = re.search(r"[0-9]{1}_[0-9]{1}_[0-9]{2}", k)
            s = re.search(r"[0-9]{1}_[0-9]{2}_[0-9]{2}", k)
            t = re.search(r"[0-9]{2}_[0-9]{1}_[0-9]{2}", k)
            

            if f != None:
                print('{}:\t\t{}'.format(k, v))
            else:
                print('{}:\t{}'.format(k, v))

    @property
    def bookmarks_map(this):
        return this.__store

    @property
    def bookmarks_list(this):
        return this.__bookmarks

    @property
    def get_bookmark_count(this):
        return this.__bookmark_count
