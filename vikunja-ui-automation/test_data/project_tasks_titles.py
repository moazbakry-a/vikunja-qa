from uuid import uuid4

run_id = uuid4().hex[:3]

project_title = f"Test Project {run_id}"
project_edited_title = f"Edited Project {run_id}"

task1 = f"Task 1 - {run_id}"
task2 = f"Task 2 - {run_id}"
task3 = f"Task 3 - {run_id}"
tasks = [task1, task2, task3]

task1_edited = f"Task 1 edited - {run_id}"
task2_edited = f"Task 2 edited - {run_id}"
task3_edited = f"Task 3 edited - {run_id}"