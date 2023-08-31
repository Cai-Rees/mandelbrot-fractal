# mandelbrot-fractal
A short project I set out on after becoming interested in computing chaotic and fractal behaviour. 

The purpose of this code is to compute and plot the mandelbrot set. This is a mathematical set of numbers in the complex plane, which forms a infintely complex fractal boundary with the complex numbers outside the set. The set is defined using the following iterative formula:
$$Z_{n+1} = Z_{n}^{2} + Z_{0}$$
Where $Z_{0}$ is the starting point in the complex plane sometimes refered to as $C$. Starting points which lead to a diverging $Z_n$ after iterating are outside the set. Whereas those that do not diverge, either by converging or forming a limit cycle are part of the set. 

Was developed using Python 3.8 and requires the Numpy and Matplotlib.pyplot packages


    
