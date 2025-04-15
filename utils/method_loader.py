import importlib

def load_and_bind_methods(instance, methods_map):
    for method_name, module_path in methods_map.items():
        try:
            module_name, func_name = module_path.rsplit('.', 1)
            module = importlib.import_module(module_name)
            func = getattr(module, func_name)
            bound_func = func.__get__(instance)
            setattr(instance, method_name, bound_func)

            #  Register the method in the dictionary
            if hasattr(instance, "bind_method"):
                instance.bind_method(method_name, bound_func)
                
        except Exception as e:
            print(f"[!] Could not bind method `{method_name}` from `{module_path}`: {e}")
