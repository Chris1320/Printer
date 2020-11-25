# Printer

## Description

Lazy module for making console outputs somewhat pretty

## Usage

```python
import printer

a = printer.Printer()
a.init()

a.print_with_status("Test Info #1", 0)
a.print_with_status("Test Warn #1", 'warn')
a.print_with_status("Test Err #1", 2)
a.print_with_status("Test Critical #1", 3)
a.print_with_status("Test Question #1", 'que')
a.print_with_status("Test Debug #1", 'deb')

a.print_with_status("This is a sentence with more than 40 characters.", 'inf', 30)

moduleoutput = a.print_with_status("This is from the Printer module.", 1, return_output=True)
print(moduleoutput)
```
