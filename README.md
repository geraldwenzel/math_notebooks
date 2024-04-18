## Jupyter notebook content:
- examples of how to solve common math problems using sympy and numpy  
- examples of how to graph functions  
- notes regarding mathematical theorems and properties  

This repo is basically my math cheatsheet.  

## Pylance undefined variable warnings

`set_notebook.py` is ran in the first cell of notebooks to set imports and variables. When these notebooks are run in vscode with the Pylance extension, undefined variable warnings appear. This error is suppressed with the following override in `.vscode/settings.json`:
```json
{
    "python.analysis.diagnosticSeverityOverrides": {
        "reportUndefinedVariable": "none"
    }
}
```

