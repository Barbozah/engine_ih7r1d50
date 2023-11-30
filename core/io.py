from core.engine import Object3D, Vertice3D

def load_objects_byu(path):
  with open(path) as fin:
    objects = []
    for raw_line in fin:
      line = raw_line.strip().split(' ')
      if len(line) == 2:
        n_vertex, n_triangle = map(int, line)
        objects.append({
          'n_vertices': n_vertex,
          'n_triangles': n_triangle,
          'vertices': [],
          'triangles': []
        })
      elif len(line) == 3:
        if objects[-1]['n_vertices'] > len(objects[-1]['vertices']):
          objects[-1]['vertices'].append(list(map(float, line)))
        elif objects[-1]['n_triangles'] > len(objects[-1]['triangles']):
          objects[-1]['triangles'].append(list(map(int, line)))
    for o in objects:
      yield Object3D(
        list(map(Vertice3D, o['vertices'])),
        o['triangles']
      )
