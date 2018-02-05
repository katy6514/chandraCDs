# Compiling Results CDs

One of my tasks at the Center for Astrophysics was to gather various lists of proposals and put them onto CDs for distribution within the center. Before I joined the team, the process was un-automated and time-consuming. I sped up the process significantly by writing a series of python scripts to automate the task.

### Gather.py
Takes an input list of science proposals and copies them to a directory.

### Compare.py
Compares the list of proposals returned from a DB query to what's been successfully copied.

### Unique.py
Sanity check script
