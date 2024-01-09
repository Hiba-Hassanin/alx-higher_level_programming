#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("main", "./main.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

a = getattr(module, "a")
print(a)
