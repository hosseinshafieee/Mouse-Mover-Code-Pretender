# Mouse Mover and Code Pretender
## Description:
This is a mouse mover and coding pretender for the times that you are not coding. for example, eating a meal or thinking in restroom while your PC is on.   
This is a small script to deceive some tracing applications or extensions that installed to monitor your coding activity for any organization.  
###### **Warning:** we do not recommend to use this for cheating at work, this is just a fun project. 


## Steps 
#### First: install required libraries
You need to install these libraries to start using this ...  

    # Copy and paste these commands in your terminal

    $ pip install argparse
    $ pip install time
    $ pip install pynput

#### Second: run the project
For running the project run ```cd Mouse-Mover-Code-Pretender/``` command.  

    # Copy and paste in your terminal

    $ python3 main.py

For writing in your editor and moving the mouse:

    $ python3 main.py -m both

# Default values
By default we just use mouse to keep the PC awake
You can find a good guide by typing ``` $ python3 main.py -h``` in your terminal

**AFK time:** 2m 
**Random write time:** 1m 

## Customize the running

``` -s ``` or ``` --seconds ``` : for detecting AFK time 

    $ python3 main.py -s 50

> Means detect if I am not on computer after 50 seconds

-------------------------------------------------------

``` -m ``` or ``` --mode ``` : for choosing the keyboard mode or mouse moving mode or both of them

    $ python3 main.py -m mouse
    $ python3 main.py -m keyboard
    $ python3 main.py -m both

-------------------------------------------------------

``` -r ``` or ``` --random ``` : for random typing time

    $ python3 main.py -r 60

> Using more than 60 seconds not recommended

-------------------------------------------------------

``` -p ``` or ``` --pixels ``` : for the moving pixels

    $ python3 main.py -p 50

## Full customization
for running full customization according to above documentation, you can use the below command to customize your running
    
    $ python3 main.py -p 70 -r 10 -s 20 -m both