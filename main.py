import clang.cindex

asympto = []

def debug_info(node, depth):
    indent = '  ' * depth
    print(f"{indent}{node.kind.name}: {node.spelling or node.displayname}")

def walk_ast(node, depth=0, met_cycles=False):
    debug_info(node, depth)
    if node.kind == clang.cindex.CursorKind.FOR_STMT and met_cycles:
        asympto.append("O(n^2)")
        return True
    res = False
    for child in node.get_children():
        if node.kind == clang.cindex.CursorKind.FOR_STMT:
            res = res or walk_ast(child, depth + 1, True)
        else:
            res = res or walk_ast(child, depth + 1, met_cycles)
    if node.kind == clang.cindex.CursorKind.FOR_STMT and not res:
        asympto.append("O(n)")
    return res

def parse_code(filename):
    clang.cindex.Config.set_library_path('C:')
    index = clang.cindex.Index.create()
    tu = index.parse(filename)
    for_tree = dict()
    walk_ast(tu.cursor)

parse_code('main.cpp')
print(asympto)