# How to get private clone of a public github repository
for example consider a scenario which we are trying to clone public repo of `ton-community/tsc5` to the private repo that I've created in `arashnm80/ts5-private`. we can use commands like this:
```
git clone --bare https://github.com/ton-community/tsc5
cd tsc5.git
git push --mirror https://github.com/arashnm80/ts5-private
```
