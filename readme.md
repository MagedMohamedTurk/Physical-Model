# Introduction
The script is trying to solve Bloch equations as described in the pdf attached. 
# Equations:
The objective is maximize function `J`:  
$$J = \frac{1}{N} \sum_{j} Y^T_{n+1} U_{n}(w_{j}, \theta_{n}) ... U_{k}(w_{j}, \theta_{k})...U_{1}(w_{j}, \theta_{1}) X_{0}-> equ(3)$$
Where $U_{k}(w, \theta_{k})$ is calculated from :  
$$U_{k}(w, \theta_{k}) = exp(\delta t(\omega \Omega_{z} + cos(\theta) \Omega_{x} + sin(\theta) \Omega_{y})) ->equ (2)$$

X,Y is caluclated from equation 4:  
$$Y^T_{k+1} = Y^T_{n+1} U_{n}(w_{j}, \theta_{n}) ...U_{k+1}(w_{j}, \theta_{k+1})$$  
$$X^T_{k-1} =  U_{n}(w_{j}, \theta_{n}) ...U_{k+1}(w_{j}, \theta_{k+1}) X_{0}$$

calculating e from equation 8:  
$$e = \sum_{j} X_{k-1} \times Y_{k+1}$$
Where $\times$ refers to cross product.

Updating $\theta$ from equ:
$$tan\theta = \frac{e_{2}}{e_{1}}$$
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
4. Update the $\Theta$ and recalculate.
This approach reduced the time significantly to less than 3 seconds per trial.
