#!/usr/bin/env python3

import utils


### sphaghetti code down below !!!


class Task(object):

    def __init__(self, task_id, description, duration, predecessors, et, lt, successors):
        self.task_id = task_id
        self.description = description
        self.duration = duration
        self.predecessors = predecessors
        self.et = et
        self.lt = lt
        self.successors = successors

    def __str__(self):
        return '{}: duration: {}, predecessors: {}, successors: {}, et: {}, lt: {}'.format(
               self.task_id, self.duration, self.predecessors, self.successors, self. et, self.lt)


def earliest_start_date(task_idx, task_order):
    if not task_order[task_idx].predecessors:
        return 0
    else:
        return max(earliest_start_date(indexOf(task_id, task_order), task_order)
                   + findById(task_id, task_order)[0].duration
                   for task_id in task_order[task_idx].predecessors)


def latest_start_date(task_idx, task_order, construction_duration):
    successors = get_successors(task_order[task_idx], task_order)
    # print([t.task_id for t in task_order], task_order[task_idx].task_id, [s.task_id for s in successors], sep='\n', end='\n\n')
    if task_idx == 0:
        return 0
    elif not successors:
        return construction_duration - task_order[task_idx].duration
    else:
        return min(latest_start_date(indexOf(task.task_id, task_order), task_order, construction_duration) -
                   task_order[task_idx].duration
                   for task in successors)


def get_successors(task, task_order):
    successors = []
    for t in task_order:
        if task.task_id in t.predecessors:
            successors.append(t)
    return successors


#### work in progress code

def add_successors(tasks):
    order = []
    for task in tasks:
        print("good until this1")
        if(task.predecessors):
            print("good until this2")
            new_task = find_Successors(task,tasks)
            print("good until this3") # not good
            order+=new_task
    return order

def find_Successors(task,tasks):
    suc_slave=0
    task_id_list=[]
    for task in tasks:
        task_id_list.append(task.task_id)

    for task in tasks:
        for predecessor in task.predecessors:
            for task_id in task_id_list:
                if(predecessor == task_id):
                    suc_master = find_task_by_task_id(task_id,tasks)
                    suc_master.successors.append(predecessor)
                    print(suc_master.successors)

def find_task_by_task_id(task_id,tasks):
    for task in tasks:
        if(task_id == task.task_id):
            return task
    return 0

        #suc_master=find_by_id1(predecessor,tasks)
        #suc_added_task = task.successors.append(suc_master)
    # return suc_added_task

# def find_by_id1(predecessor, all_tasks):
#     #print(predecessor)s
#     for task in all_tasks:
#         for pre in task.predecessors:
#             if(pre == predecessor):
#                 #task.successors.append(predecessor) 
#                 #print(task.task_id)
#                 #print(predecessor)
#                 find_by_id2(pre,task.task_id,all_tasks)
#                 print(task)

# def find_by_id2(suc_master,suc_slave,all_tasks):
#     give_successors=[]
#     for task in all_tasks:
#         if(suc_master == task.task_id):
#             suc_master.successors.append(suc_slave)
#             print(suc_master)

def Latest_Start_Date(task_idx, task_order):
    if not task_order[task_idx].successors:
        return 0
    else:
        find_Successors(task_order)
        return min(Latest_Start_Date(indexOf(task_id, task_order), task_order)+findById(task_id, task_order)[0].duration
                  for task_id in task_order[task_idx].successors)

def find_by_id(predecessor, all_tasks):
    #print(predecessor)
    for task in all_tasks:
        for pre in task.predecessors:
            if(pre == predecessor):
                task.successors.append(predecessor)
                print(task)

####


def findById(task_id, tasks):
    return [t for t in tasks if t.task_id == task_id]


def construction_duration(earliest_start_dates, task_order):
    return earliest_start_dates[-1] + task_order[-1].duration


def getMpmOrder(tasks):
    order = []
    i = 0
    while len(order) < len(tasks):
        if i >= len(tasks)+1:
            utils.error('Could not produce a list of tasks. There seems to be a cycle or incorrect dependencies!')
        new = findMatching(tasks, order)
        new = sortFound(new)
        order += new
        i += 1
    return order


def findMatching(tasks, current_order):
    return [task for task in tasks if canBeStarted(task, current_order)]


def canBeStarted(task, current_order):
    return task not in current_order and (all([findById(p, current_order) for p in task.predecessors]) or not task.predecessors)


def indexOf(task_id, tasks): 
    for i, task in enumerate(tasks):
        if task_id == task.task_id:
            return i
    return -1


def sortFound(found):
    found = sorted(found, key=lambda task: (task.duration, task.task_id))
    return found
