# Introduction
The script is trying to solve Bloch equations as described in the pdf attached. 
# Equations:
The objective is maximize function $J$:  

$$
\begin{equation}
\tag{3}
\displaystyle J = \frac{1}{N} \sum_j Y_{n+1}^T U_n\left(\omega_j, \theta_n\right)\cdots U_k\left(\omega_j, \theta_k\right)\cdots U_1\left(\omega_j, \theta_1\right)X_0.
\end{equation}
$$


Where $U_k\left(\omega, \theta_k\right)$ is calculated from :  

$$
\begin{equation}
\tag{2}
\displaystyle U_k\left(\omega, \theta_k\right) = exp\left(\partial t\left(\omega\Omega_z+cos\left(\theta\right) \Omega_x + sin\left(\theta\right)\Omega_y\right)\right).
\end{equation}
$$

$X,Y$ is caluclated from equation 4:  

$$
\begin{equation}
\tag{4}
\displaystyle Y_{k+1}^T = Y_{n+1}^T U_n\left(\omega_j, \theta_n\right) \cdots U_{k+1}\left(\omega_j, \theta_{k+1}\right).
\end{equation}
$$

$$
\begin{equation}
\tag{4}
\displaystyle X_{k-1}^T = U_n \left(\omega_j, \theta_n\right)\cdots U_{k+1}\left(\omega_j, \theta_k+1\right) X_0.
\end{equation}
$$


calculating $e$ from equation 8:  

$$
\begin{equation}
\tag{8}
\displaystyle e = \sum_j X_{k-1} \times Y_{k+1}.
\end{equation}
$$

Where $X$ refers to $cross\ product$.

Updating $\theta$ from equ:

$$
\displaystyle tan\left(\theta\right) := \frac{e_2}{e_1}.
$$

  

as:   
```math
e = \begin{pmatrix}e_1 \cr e_2 \cr e_3 \cr \end{pmatrix}.
```

# Alogrithms
The optimization algorithm is as follows:
1. Assume $θ_i = 0$ (from $\theta_1$ to $\theta_n$).
2. We calculate initial $J$ from $equation (3)$.
3. Calculate all $Y_k$ and $X_k$  as defined in  $equation (4)$. 
4. Using $equation (8)$ we calculate $e$ which should be a three dimensions vector.         
5. Calculate a new set of $\theta_k$ using $tan(\theta_k) = \frac{e_2}{e_1}$.
6. Do this for all $\theta$.
7. We recalculate new $J$ from $equation (3)$.
8. Repeat steps from 3 to 7.
9. We need to get J to reach 1. Only then we can stop the iteration.  
>This method is implemented in git branch `approach A`  
The method was slow and iteration time is over 50 seconds for trial.  
Another approach was tried in the `Master branch`  
1. Assume $θ_i = 0$ (from $θ_1$ to $θ_n$)
2. Calculate a tensor with `(N,n,3,3)` dimensions where `N`: number of random $\omega$ and `n` is the number of selected $\theta$.
3. Calculate Y, X, and e from the tensor slicing method.
4. Updating $\theta$ and recalculate.
This approach reduced the time significantly to less than 3 seconds per trial.
