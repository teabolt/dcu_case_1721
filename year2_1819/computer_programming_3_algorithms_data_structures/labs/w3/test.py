from Queue import Queue
# from print_queue import print_queue

def main():
   size = int(input())
   q = Queue(size)

   print('...Start: data {}, front {}, back {}'.format(q.data, q.front, q.back))
   command = input()
   while len(command) > 0:
      if command[0] == 'a': # add
         item = command.split()[1]
         q.enqueue(int(item))
         print('...Added: {}'.format(item))
         print('...Now: data {}, front {}, back {}'.format(q.data, q.front, q.back))
      elif command[0] == 'r': # remove
         item = q.dequeue();
         print('...Removed: {}'.format(item))
         print('...Now: data {}, front {}, back {}'.format(q.data, q.front, q.back))
      else:
         print("Unknown command!")
      command = input()

   print('...Final: data {}, front {}, back {}'.format(q.data, q.front, q.back))
   print_queue(q.data, q.front, q.back)

if __name__ == "__main__":
   main()