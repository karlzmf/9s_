# -*- coding: utf-8 -*-
#!/usr/bin/env python
from models import drfOpsClass, drfOpsClassBase, session
import uuid
import itchat
import re

def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

'''test_msg_s = '#S06:00 1740'
test_msg_e = '#E18:00 1859'
'''

classStart = drfOpsClass()
classBaseStart = drfOpsClassBase()
dictStart = to_dict(classStart)
dictBaseSrart = to_dict(classBaseStart)


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    a = msg['Text']
    if a[0] == '#':
        list = a[2:].split()
        if a[1] == 'S' or a[1] == 's':
            cuuid = str(uuid.uuid1())
            duuid = str(uuid.uuid1())
            dictStart['class_id'] = re.sub("-", "", cuuid)
            dictStart['task_id'] = '123456789'
            dictStart['work_date'] = '2018-01-05'
            dictStart['class_order'] = '一班'
            dictStart['create_org_id'] = 'C1000000800073'
            dictStart['creator_id'] = '8a2b82db4b4d1a36014b6d39c3da0e72'
            dictStart['rflag'] = '0'
            dictStart['isondata'] = '2'
            dictBaseSrart['base_id'] = re.sub("-","", duuid)
            dictBaseSrart['class_id'] = dictStart['class_id']
            dictBaseSrart['receive_time'] = list[0]
            dictBaseSrart['receive_well_depth'] = float(list[1])
            dictBaseSrart['create_org_id'] = 'C1000000800073'
            dictBaseSrart['creator_id'] = '8a2b82db4b4d1a36014b6d39c3da0e72'
            dictBaseSrart['rflag'] = '0'
            dictBaseSrart['isodata'] = '2'

        if a[1] == 'E' or a[1] == 'e':
            drfOpsClass1 = drfOpsClass()
            drfOpsClassBase1 = drfOpsClassBase()
            dictBaseSrart['send_time'] = list[0]
            dictBaseSrart['send_well_depth'] = float(list[1])
            dictBaseSrart['drilled_footage'] = float(dictBaseSrart['send_well_depth']-dictBaseSrart['receive_well_depth'])
            for dOClass in drfOpsClass().__table__.columns:
                setattr(drfOpsClass1, dOClass.name, dictStart[dOClass.name])
            for dOClassBase in drfOpsClassBase().__table__.columns:
                setattr(drfOpsClassBase1, dOClassBase.name, dictBaseSrart[dOClassBase.name])
            session.add(drfOpsClass1)
            session.add(drfOpsClassBase1)
            session.commit()

itchat.auto_login(hotReload=True)
itchat.run()



            








