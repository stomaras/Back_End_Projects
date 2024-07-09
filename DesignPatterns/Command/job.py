import time

#Command
class Command:
    def execute(self):
        pass

#receiver
class Job:
    def __init__(self, name):
        self.name = name
        
    def execute(self):
        print(f"Executing job: {self.name}")
        time.sleep(1)
        
        
# concrete command
class ScheduleJobCommand(Command):
    def __init__(self, job):
        self.job = job
        
    def execute(self):
        self.job.execute()
        
        
# Invoker
class JobScheduler:
    def __init__(self):
        self.jobs = []
        
    def schedule_job(self, command):
        command.execute()
        self.jobs.append(command)
        
# client code
job_scheduler = JobScheduler()

job1 = Job("Job 1")
job2 = Job("Job 2")
job3 = Job("Job 3")


schedule_command1 = ScheduleJobCommand(job1)
schedule_command2 = ScheduleJobCommand(job2)
schedule_command3 = ScheduleJobCommand(job3)

job_scheduler.schedule_job(schedule_command1)
job_scheduler.schedule_job(schedule_command2)
job_scheduler.schedule_job(schedule_command3)  

# invoker receive the receiver and concrete commands 