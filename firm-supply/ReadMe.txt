Python3 needs to be installed and executable from a console (i.e. Powershell or Bash)

After python is installed, install the required libraries by running the command:
    pip install -r requirements.txt

This program uses Sympy to parse functions provided as input. This requires the functions are input in
Python format. In Python, exponents are entered after a double asterisk. To enter 2y^2, 2*y**2 should be
used. As another example, to input a function such as 2y^3 + 4y^2 + 20y + 10, the input must be in the
format 2*y**3 + 4*y**2 + 20*y + 10. Whitespace doesn't affect Sympy as long as the function is valid.
