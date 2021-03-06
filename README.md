# Programmierbeleg: Weblogo
WebLogo is a tool to graphically represent a nucleic acid or amino acid multiple sequence 
alignment (MSA). A WebLogo consists of x-axis and y-axis. The x-axis represents the position 
number of given MSA-Sequence, whereas the y-axis indicates the information content at that 
position in bits. The most conserved nucleic or amino acid is located at the upper position 
of each column. <br/>
WebLogo is precise, easy to read and provides rich information on the information content 
and conservation of each element of the MSA. 

> References:
> [WebLogo Berkeley](https://weblogo.berkeley.edu/)

## Installation
To plot the graph, a package `dmslogo` must be installed. 
`dmslogo` is a Python package written by the Bloom lab
The easiest way to install it is with `pip install dmslogo`.
This package can be then installed in the current Project Interpreter (_File/Settings/Project Interpreter_).

For more information visit [Bloom Laboratory](https://jbloomlab.github.io/dmslogo/index.html).

> References:
> [Bloom Laboratory](https://jbloomlab.github.io/dmslogo/index.html)


 
## How to use
### Input
A file with MSA is provided by the user by entering the file name
 after the program runs:<br/> `Enter the MSA file name` 
### Output
The height for each nucleic or amino acid is calculated and saved in a data frame, 
its values are plotted in the `dmslogo`.


* A .png file as output

![Beispiel](https://user-images.githubusercontent.com/50204636/60206203-43e06e00-9853-11e9-91ee-32905911c3cf.png)
![Beispiel2](https://user-images.githubusercontent.com/50204636/60206194-4216aa80-9853-11e9-97fd-dcf39a845d7a.png)


### Color Scheme
This WebLogo uses `dmslogo` default coloring scheme. 

## Acknowledgements
WebLogo was created by: 

Stýblová, Sabrina<br/>
Faculty Applied Computer Sciences & Biosciences<br/>
Hochschule Mittweida



