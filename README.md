# beautiful_crawler   

Beautiful Crawler is a simple web crawler developed in six or less days for a job application.   
Heavily based on [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) Python library.

## Usage   

I used [pip](https://pip.pypa.io/en/stable/) to create a virtual enviroment and install requirements.txt   

```bash
python3 -m venv DEV  
. DEV/bin/activate  
python3 -m pip install --upgrade pip  
pip install -r requirements.txt
```    

And after that, run the imprime.py script   

```bash
python imprime.py
```

## My favorite git rotine at github:   

```bash
git pull origin main # first things first  
git checkout -b [working-feature] # if needed  
# work, code, fix, do awesome software  
git add .  
git commit -m "<type>[optional scope]: <description>" # from Conventional Commits  
git push origin [working-feature]  
```   
When done, open a PR.  
After merge, delete the branch:  
```bash
git branch -D [working-feature] # or in github button at PR page  
```


## References   

[Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)  
[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)   
[pip](https://pip.pypa.io/en/stable/)
