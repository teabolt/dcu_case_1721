#!/usr/bin/env python3

import sys
import utils
import mpm


def main():
    argc = len(sys.argv)
    if argc != 2:
        utils.error('Missing command line argument.')
    else:
        if sys.argv[1] == '-h':
            print(utils.help())
        else:
            filename = sys.argv[1]
            try:
                tasks = utils.parse_tasks(filename)
            except FileNotFoundError:
                utils.error('File "%s" could not be found' % filename)
            if not tasks:
                utils.error('No tasks found.')
            order = mpm.getMpmOrder(tasks)

            earliest_start_dates = [mpm.earliest_start_date(i, order) for i, task in enumerate(order)]

            construction_duration = mpm.construction_duration(earliest_start_dates, order)
            print('Total duration of construction: {} weeks'.format(construction_duration))
            print()

            latest_start_dates = [mpm.latest_start_date(i, order, construction_duration) for i, task in enumerate(order)]
            for i, task in enumerate(order):
                earliest = earliest_start_dates[i]
                latest = latest_start_dates[i]
                if earliest == latest:
                    print('{} must begin at t={}'.format(task.task_id, earliest))
                else:
                    print('{} must begin between t={} and t={}'.format(task.task_id, earliest, latest))
            print()

            for i, task in enumerate(order):
                task_fluctuation = latest_start_dates[i] - earliest_start_dates[i]
                task_schedule = ' '*earliest_start_dates[i] + '='*task.duration
                print('{}\t({})\t{}'.format(task.task_id, task_fluctuation, task_schedule))


if __name__ == '__main__':
    main()
  