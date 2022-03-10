from subprocess import check_output
import graphviz

processes = check_output(['ps', '-ax']).strip().split(b'\n')[1:]
g = graphviz.Digraph('unix', filename='process_tree.gv')

process = []
for x in processes:
    temp = x.decode().strip()
    temp = temp[:temp.index(' ')]
    try:
        parent_of_temp = check_output(['ps', '-o', 'ppid=', '-p', temp]).decode().strip()
        g.edge(parent_of_temp, temp)
    except:
        pass

g.view()
