# Introduction
The script is trying to solve Bloch equations as described in the pdf attached. 
# Equations:
The objective is maximize function `J`:  

<img src="https://latex.codecogs.com/png.image?\dpi{200}&space;\bg_white&space;J&space;=&space;\frac{1}{N}&space;\sum_{j}&space;Y^T_{n&plus;1}&space;U_{n}(w_{j},&space;\theta_{n})&space;...&space;U_{k}(w_{j},&space;\theta_{k})...U_{1}(w_{j},&space;\theta_{1})&space;X_{0}\hspace{20mm}->equ(3)" />  

Where <img src="https://latex.codecogs.com/png.image?\dpi{100}&space;\bg_white&space;U_{k}(w,&space;\theta_{k})&space;" title="\bg_white U_{k}(w, \theta_{k}) " /> is calculated from :  

<img src="https://latex.codecogs.com/png.image?\dpi{200}&space;\bg_white&space;U_{k}(w,&space;\theta_{k})&space;=&space;exp(\delta&space;t(\omega&space;\Omega_{z}&space;&plus;&space;cos(\theta)&space;\Omega_{x}&space;&plus;&space;sin(\theta)&space;\Omega_{y}))\hspace{20mm}&space;->equ&space;(2)" title="\bg_white U_{k}(w, \theta_{k}) = exp(\delta t(\omega \Omega_{z} + cos(\theta) \Omega_{x} + sin(\theta) \Omega_{y}))\hspace{20mm} ->equ (2)" />

X,Y is caluclated from equation 4:  
<img src="https://latex.codecogs.com/png.image?\dpi{200}&space;\bg_white&space;Y^T_{k&plus;1}&space;=&space;Y^T_{n&plus;1}&space;U_{n}(w_{j},&space;\theta_{n})&space;...U_{k&plus;1}(w_{j},&space;\theta_{k&plus;1})\hspace{20mm}->equ(4)" title="\bg_white Y^T_{k+1} = Y^T_{n+1} U_{n}(w_{j}, \theta_{n}) ...U_{k+1}(w_{j}, \theta_{k+1})\hspace{20mm}->equ(4)" />  

<img src="https://latex.codecogs.com/png.image?\dpi{200}&space;\bg_white&space;X^T_{k-1}&space;=&space;&space;U_{n}(w_{j},&space;\theta_{n})&space;...U_{k&plus;1}(w_{j},&space;\theta_{k&plus;1})&space;X_{0}\hspace{20mm}->equ(4)" title="\bg_white X^T_{k-1} = U_{n}(w_{j}, \theta_{n}) ...U_{k+1}(w_{j}, \theta_{k+1}) X_{0}\hspace{20mm}->equ(4)" />  

calculating e from equation 8:  

<img src="https://latex.codecogs.com/png.image?\dpi{200}&space;\bg_white&space;e&space;=&space;\sum_{j}&space;X_{k-1}&space;\times&space;Y_{k&plus;1}\hspace{20mm}->equ(8)" title="\bg_white e = \sum_{j} X_{k-1} \times Y_{k+1}" />  

Where 'X' refers to cross product.

Updating θ from equ:
<img src="https://latex.codecogs.com/png.image?\dpi{200}&space;\bg_white&space;tan\theta&space;=&space;\frac{e_{2}}{e_{1}}" title="\bg_white tan\theta = \frac{e_{2}}{e_{1}}" />  

as:   e = [e1, e2, e3]

# Alogrithms
The optimization algorithm is as follows:
1. Assume θi = 0 (from θ1 to θn)
2. We calculate initial J from equation (3)
3. Calculate all Yk and Xk  as defined in  equation (4) 
4. Using equation (8) we calculate e which should be a three dimensions vector.         
5. Calculate a new set of θk using tan θk = e2/e1
6. Do this for all theta
7. We recalculate new J from equation (3)
8. Repeat steps from 3 to 7
9. We need to get J to reach 1. Only then we can stop the iteration.  
>This method is implemented in git branch `approach A`  
The method was slow and iteration time is over 50 seconds for trial.  
Another approach was tried in the `Master branch`  
1. Assume θi = 0 (from θ1 to θn)
2. Calculate a tensor with (N,n,3,3) dimensions where N: number of random $\omega$ and n is the number of selected $\theta$.
3. Calculate Y, X, and e from the tensor slicing method.
4. Updating θ and recalculate.
This approach reduced the time significantly to less than 3 seconds per trial.
