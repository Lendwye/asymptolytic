import clang.cindex
clang.cindex.Config.set_library_path('C:')
index = clang.cindex.Index.create()
name = "main.cpp"
translation_unit = index.parse(name, args=['-std=c++17'])
for_amount = 0
for node in translation_unit.cursor.walk_preorder():
    try:
        print(node.kind)
        if node.kind == clang.cindex.CursorKind.FOR_STMT:
            for_amount += 1
    except:
        pass
print(for_amount)