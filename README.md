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

## One time setup steps
`pre-commit install` and `nbstripout --install` have been run once manually. Because the changes from these commands persist in the `.git` directory, the commands do not need to be executed if the docker container is rebuilt.
