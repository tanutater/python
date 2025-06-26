def print_builtin_function_docs():
  """
  prints the documention (syntax,description,etc.)of all python built in function
  """
import builtins
# get all the attributrs in buitins modules 
builtins_item = dir(builtins)

print("documentation of nuilt in function\n")
for item in builtins_item:
  obj=getattr(builtins,item)
  if callable(obj):
    print(f"{'-* 40'}\n function ;{item}\n{'_'* 40}")
    help(obj)
  if item=="_main_":
    print_builtin_function_docs