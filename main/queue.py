import queue as q
import concurrent.futures
import logging

status = {
    "error": -1,
    "success": 0
}

class queueHandler():
    def __init__(self, size):
        self.taskQueue = q.Queue(size)
        self.argQueue = q.Queue(size)
        self.data = set()
        self.runningTasks = False

    def feedThreads(self, task, args):
        try:
            self.taskQueue.put(task)
            self.argQueue.put(args)
        except Exception as e:
            logging.warn(e)
            return -1
        return 0
    
    def runTasks(self):
        self.runningTasks = True
        taskMap = dict()
        executor =  concurrent.futures.ThreadPoolExecutor(max_workers = 4)

        while self.runningTasks:
            done, notDone = concurrent.futures.wait(taskMap, timeout=1, returnWhen=concurrent.futures.FIRSTCOMPLETED)

            while not self.taskQueue.empty():
                task = self.taskQueue.get()
                args = self.argQueue.get()

                taskMap[executor.submit(task, args)] = task
            
            for finishedTask in done:
                task = taskMap[finishedTask]

                self.data.append(finishedTask.result())
                logging.info("Task done!")

                taskMap.pop(finishedTask)

            if not taskMap:
                self.runningTasks = False

        executor.shutdown()
        
        return 0