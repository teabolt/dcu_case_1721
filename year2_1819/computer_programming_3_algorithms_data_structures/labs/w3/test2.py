from Queue import Queue

#
#  Test a queue
#
def main():
   q = Queue()

   command = input()
   while len(command) > 0:
      print(command + ":", end="")
      if command[0] == 'a': # add
         item = command.split()[1]
         q.enqueue(int(item));
      elif command[0] == 'r': # remove
         print(q.dequeue(), end="");
      else:
         print("Unknown command!")
      print(" _" if q.isempty() else " *")
      command = input()
   print()


if __name__ == "__main__":
   main()