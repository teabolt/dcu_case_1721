#!/usr/bin/env python3

import sys
from mpm import Task


HELP_MESSAGE = """USAGE
\t./305construction file

DESCRIPTION
\tfile\tfile describing the tasks"""


def help():
    return HELP_MESSAGE


def error(message):
    sys.stderr.write(message+'\n')
    sys.exit(84)


def parse_tasks(filename):
    tasks = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                error('Task line is empty.')
            tokens = line.split(';')
            if len(tokens) < 3:
                error('Not enough task information: {}'.format(tokens))
            task_id, description, duration, predecesors = *tokens[:3], tokens[3:]
            try:
                duration = int(duration)
            except ValueError:
                error('Could not parse the duration field as a number.')
            if duration < 0:
                error('Duration is negative: %d' % duration)
            et=0
            lt=0
            successors=[]

            #task = Task(task_id, description, duration, predecesors)
            task = Task(task_id, description, duration, predecesors,et,lt,successors)
            tasks.append(task)
    return tasks
