# Developer Logs

### Main commandline references

#### Check open ports
```ps1
netstat -ano
```

#### Check specific port
```ps1
netstat -ano | findstr ":{port_number}"
```

### Git References

#### Clone
```ps1
git clone https://github.com/pcollins425/dgs_universal_application C:/Users/Paul Collins/dgs_universal_application
```

#### Stage
```ps1
git add .
```

#### Commit
```ps1
git commit
```

If commit opens in command line, type commit comments, followed by `esc` and `:wq`, then enter.

#### Push
```ps1
git push origin {branch}
```

#### Check active branch
```ps1
git branch
```

#### Remove Clone Repository
```ps1
rm -Recurse -Force dgs_universal_application
```