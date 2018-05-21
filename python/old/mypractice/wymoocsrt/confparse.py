# -*- codeding: utf-8 -*-

import configparser
import sys
import os

class client_info(object):
    def __init__(self, file):
        self.file = file
        self.cfg = configparser.ConfigParser()

    def cfg_load(self):
        self.cfg.read(self.file, encoding='utf-8')


    def cfg_dump(self):
        se_list = self.cfg.sections()
        print('====================>')
        for se in se_list:
            print(se)
            print(self.cfg.items(se))
        print('====================>')

    def delete_item(self, se, key):
        self.cfg.remove_option(se, key)

    def delete_section(self, se):
        self.cfg.remove_section(se)

    def add_section(self, se):
        self.cfg.add_section(se)

    def set_item(self, se, key, value):
        self.cfg.set(se, key, value)

    def save(self):
        fd = open(self.file, 'w')
        self.cfg.write(fd)
        fd.close()

    def get_items_dict(self, se):
        dbinfo = self.cfg.items(se)
        # print(dbinfo)
        # print(type(dbinfo))
        dbitems = {}
        for i in range(len(dbinfo)):
            dbitems[dbinfo[i][0]] = dbinfo[i][1]
        return dbitems

    def get_all_itmes_list(self):
        se_list = self.cfg.sections()
        all_list = []
        for se in se_list:
            s_list = self.cfg.items(se)
            all_list.extend(s_list)

        return all_list

    def get_all_items_dict(self):
        se_list = self.cfg.sections()
        all_dict = {}
        for se in se_list:
            s_dict = self.get_items_dict(se)

            all_dict.update(s_dict)

        print(all_dict)
        return all_dict





if __name__ == '__main__':
    info = client_info('conf.ini')
    info.cfg_load()
    info.get_all_items_dict()
    # info.get_all_itmes_list()

    # print(info.get_items_dict('db'))


    # info.add_section('CF')
    # info.set_item('CF', 'name', 'wymoocsrt')
    # info.cfg_dump()
    info.save
