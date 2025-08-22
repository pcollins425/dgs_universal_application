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

#### Push
```ps1
git push origin {branch}
```

#### Check active branch
```ps1
git branch
```