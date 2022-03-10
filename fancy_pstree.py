from subprocess import check_output
import graphviz
from re import match, split
from random import randint
processes = check_output(['ps', '-ax']).strip().split(b'\n')[1:]
g = graphviz.Digraph('unix', filename='process_tree.gv')

process = {}
colors = {}
for x in processes:
    temp = match(r'^\d+ *[^ ]+ *[^ ]+', x.decode().strip()).group()
    pid, tty, stat = split(r' +', temp)
    process[pid] = stat
    current_color = colors[stat] if stat in colors else ('#' + ''.join(hex(randint(0, 255))[2:] for i in range(3)))
    colors[stat] = current_color
    g.node(pid, style='filled', color=current_color)
    try:
        ppid = check_output(['ps', '-o', 'ppid=', '-p', pid]).decode().strip()
        g.edge(ppid, pid)
    except:
        pass

g.view()
