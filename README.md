## Overview 
This is an artificial intelligence bot for the 2048 puzzle game.
The file PlayerAI_3.py file contains the code for the bot.  
I used the minimax algorithm combined with alpha-beta pruning to pick the best move in a 200 milisecond time limit.  

The algorithm achieves:  
256:  100%  
512:  100%  
1024:  85%  
2048:  20%  

## Dependencies  
* python 3.5 or later
* git  

The following lines should install python3.5 on your computer,  
```sh
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.5
```
Next we need to install git  
```sh
sudo apt-get install git
```

## Usage  
```sh
git clone https://github.com/spirosbax/2048-ai.git
```
This will create a directory called "2048-ai" containing the repository files, then do 
```sh
cd 2048-ai
```
Then run the file with 
```sh
python3 GameManager_3.py
```

## Development
I am open to suggestions for improving the heuristics, feel free to contribute.  
Want to contribute? Great!  
Fork the repository and start coding!  

## Credits
I used distribution code provided by: https://www.edx.org/course/artificial-intelligence-ai-columbiax-csmm-101x-1

